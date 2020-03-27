from conans import ConanFile, tools, cppstd
from conans.errors import ConanInvalidConfiguration


class Recipe(ConanFile):
    name = "valid_range"
    settings = "os", "arch", "compiler", "build_type"

    cppstd_compatibility = [(cppstd.CPPSTD_11, cppstd.CPPSTD_14, cppstd.CPPSTD_17)]

    def configure(self):
        self.output.info("This package works only for some C++ standards: 11, 14 and 17")

    def package_id(self):
        self.output.info("This package is compatible for all the C++ standards")
