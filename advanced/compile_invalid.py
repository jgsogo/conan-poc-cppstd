from conans import ConanFile, tools, cppstd
from conans.errors import ConanInvalidCppstd


class Recipe(ConanFile):
    """
    This package doesn't compile using C++17, but its ABI is compatible with 11, 14 and 17 (is this real/possible?)
    Maybe, it doesn't compile because of this specific os/arch/compiler/compiler.version, shit happens!
    """

    name = "compile_invalid"
    settings = "os", "arch", "compiler", "build_type"

    cppstd_compatibility = [(cppstd.CPPSTD_98), 
                            (cppstd.CPPSTD_11, cppstd.CPPSTD_14, cppstd.CPPSTD_17),
                            (cppstd.CPPSTD_20)]

    def configure(self):
        self.output.info("This package compile for all the C++ standards, but c++17")
        cppstd_value, _ = cppstd.get_cppstd(self)
        if cppstd_value == cppstd.CPPSTD_17:
            raise ConanInvalidCppstd("Cannot compile using c++17")  # ConanInvalidCppstd will raise in build method

    def package_id(self):
        self.output.info("This package is compatible for C++ standards inside some groups")
