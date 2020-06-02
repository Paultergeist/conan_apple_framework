from conans import ConanFile, CMake, tools


class AppleframeworkConan(ConanFile):
    name = "hello_framework"
    version = "1.0.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Appleframework here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self, generator="Xcode")
        cmake_system_name = {
            "Macos" : "Darwin",
            "iOS" : "iOS",
            "tvOS" : "tvOS",
            }[str(self.settings.os)] # workaround for already documented #4550
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
        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)
        self.run("otool -L %s/lib/hello.framework/hello" % self.build_folder)
        self.run("otool -L %s/hello.framework/hello" % self.package_folder)
        self.run(f"lipo -info {self.build_folder}/lib/hello.framework/hello")
        self.run(f"lipo -info {self.package_folder}/hello.framework/hello")
        self.run(f"otool -arch arm64 -l {self.package_folder}/hello.framework/hello | grep -A4 'VERSION_MIN\|LC_BUILD_VERSION' || true")
        self.run(f"otool -arch x86_64 -l {self.package_folder}/hello.framework/hello | grep -A4 'VERSION_MIN\|LC_BUILD_VERSION' || true")

    #def package(self):
    #    self.copy("*.h", dst="include", src="src")
    #    self.copy("*.lib", dst="lib", keep_path=False)
    #    self.copy("*.dll", dst="bin", keep_path=False)
    #    self.copy("*.dylib*", dst="lib", keep_path=False)
    #    self.copy("*.so", dst="lib", keep_path=False)
    #    self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if tools.is_apple_os(self.settings.os):
            self.cpp_info.frameworkdirs.append(self.package_folder)
            self.cpp_info.frameworks.append("hello")
        else:
            self.cpp_info.libs = ["hello"]

    # def package_info(self):
    #     if tools.is_apple_os(self.settings.os):
    #         self.cpp_info.sharedlinkflags = ["-framework hello"]
    #     else:
    #         self.cpp_info.libs = ["hello"]

