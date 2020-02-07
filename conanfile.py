from conans import ConanFile, CMake, tools


class AppleframeworkConan(ConanFile):
    name = "apple_framework"
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
        cmake = CMake(self)
        xcrun = tools.XCRun(self.settings)
        cmake.definitions.update({
            'CMAKE_OSX_SYSROOT' : xcrun.sdk_path,
            'CMAKE_OSX_ARCHITECTURES' : tools.to_apple_arch(self.settings.arch),
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

