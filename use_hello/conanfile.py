from conans import ConanFile, CMake, tools


class AppleFrameworkConan(ConanFile):
    name = "apple_use_framework"
    version = "1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of AppleApp here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "src/*"


    def requirements(self):
        self.requires('apple_framework/1.0.0@test/test')

    def build(self):
        cmake = CMake(self, generator="Xcode")
        cmake_system_name = {"Macos" : "Darwin", "iOS" : "iOS", "tvOS" : "tvOS"}[str(self.settings.os)]
        archs = {
            "Macos" : "x86_64",
            "iOS" : "arm64;x86_64",
            "tvOS" : "arm64;x86_64",
            }[str(self.settings.os)]
        xcrun = tools.XCRun(self.settings)
        cmake.definitions.update({
            'CMAKE_OSX_SYSROOT' : xcrun.sdk_path,
            'CMAKE_OSX_ARCHITECTURES' : archs,
            'CMAKE_OSX_DEPLOYMENT_TARGET' : self.settings.os.version,
            'CMAKE_SYSTEM_NAME' : cmake_system_name,
            'CMAKE_IOS_INSTALL_COMBINED' : True,
            'CMAKE_XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH' : False,
        })
        cmake.configure(source_folder="src")
        cmake.build()
        cmake.install()

