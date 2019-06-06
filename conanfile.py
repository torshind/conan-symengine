from conans import ConanFile, CMake, tools


class SymEngineConan(ConanFile):
    name = "SymEngine"
    version = "0.4.0"
    license = "MIT"
    url = "https://github.com/symengine/symengine"
    description = "Fast symbolic manipulation library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/symengine/symengine.git", "v" + self.version)

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["INTEGER_CLASS"] = "boostmp"
        cmake.definitions["BUILD_TESTS"] = "OFF"
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["symengine"]
