import os
from conans import ConanFile, tools, cppstd, CMake
from conans.errors import ConanInvalidConfiguration


class Recipe(ConanFile):
    name = "compatible"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "../src/*"

    def configure(self):
        self.output.info("This package works for all the C++ standards")

    def build(self):
        cmake = CMake(self)
        settings = "|".join(map(str, [self.settings.os, self.settings.compiler, self.settings.compiler.cppstd]))
        cmake.definitions["MESSAGE:STRING"] = settings
        cmake.definitions["OUTPUT_NAME:STRING"] = self.name
        cmake.configure()
        cmake.build()
    
    def package(self):
        self.copy(f"{self.name}*", src="", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        self.output.info("This package is compatible for all the C++ standards")
