from conans import ConanFile, tools, cppstd


class Recipe(ConanFile):
    name = "compatible_groups"
    settings = "os", "arch", "compiler", "build_type"

    cppstd_compatibility = [(cppstd.CPPSTD_98), 
                            (cppstd.CPPSTD_11, cppstd.CPPSTD_14, cppstd.CPPSTD_17),
                            (cppstd.CPPSTD_20)]

    def configure(self):
        self.output.info("This package works for all the C++ standards")

    def package_id(self):
        self.output.info("This package is compatible for C++ standards inside some groups")
