from conans import ConanFile, CMake


class SymEngineConan(ConanFile):
    name = "SymEngine"
    version = "0.4.0"
    license = "MIT"
    homepage = "https://github.com/symengine/symengine/"
    url = "https://github.com/torshind/conan-symengine/"
    description = "Fast symbolic manipulation library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        self.run("git clone --branch v"
                 + self.version
                 + " https://github.com/symengine/symengine.git")

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["INTEGER_CLASS"] = "boostmp"
        cmake.definitions["BUILD_TESTS"] = "OFF"
        cmake.configure(source_folder="symengine")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["symengine"]
