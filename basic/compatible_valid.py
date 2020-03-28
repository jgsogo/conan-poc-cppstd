from conans import ConanFile, tools, cppstd
from conans.errors import ConanInvalidConfiguration


class Recipe(ConanFile):
    name = "compatible_valid"
    settings = "os", "arch", "compiler", "build_type"

    cppstd_compatibility = [(cppstd.CPPSTD_98), 
                            (cppstd.CPPSTD_11, cppstd.CPPSTD_14, cppstd.CPPSTD_17),
                            (cppstd.CPPSTD_20)]

    def configure(self):
        self.output.info("This package compile for all the C++ standards, but c++17")
        cppstd_value, _ = cppstd.get_cppstd(self)
        if cppstd_value == cppstd.CPPSTD_17:
            raise ConanInvalidConfiguration("Cannot compile using c++17")

    def package_id(self):
        self.output.info("This package is compatible for C++ standards inside some groups")
