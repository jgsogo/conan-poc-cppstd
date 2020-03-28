from conans import ConanFile, tools, cppstd
from conans.errors import ConanInvalidCppstd


class Recipe(ConanFile):
    """
    This package doesn't compile using C++17 and no other C++ standard would be ABI
    compatible with it (probably this is not a real scenario)
    """

    name = "cppstd_invalid"
    settings = "os", "arch", "compiler", "build_type"

    cppstd_compatibility = [(cppstd.CPPSTD_98, cppstd.CPPSTD_11, cppstd.CPPSTD_14, cppstd.CPPSTD_20)]

    def configure(self):
        self.output.info("This package compile for all the C++ standards, but c++17 (and it has no compatible for it)")

    def package_id(self):
        self.output.info("This package is compatible for C++ standards inside some groups")
