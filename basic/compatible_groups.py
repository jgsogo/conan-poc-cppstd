import os
from conans import ConanFile, tools, cppstd, CMake
from conans.errors import ConanInvalidConfiguration


class Recipe(ConanFile):
    name = "compatible_groups"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "../src/*"
    generators = "cmake"

    cppstd_compatibility = [(cppstd.CPPSTD_98), 
                            (cppstd.CPPSTD_11, cppstd.CPPSTD_14, cppstd.CPPSTD_17),
                            (cppstd.CPPSTD_20)]

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
        self.copy(f"{self.name}*", src="bin", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        self.output.info("This package is compatible for C++ standards inside some groups")
