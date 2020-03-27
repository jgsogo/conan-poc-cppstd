from conans import ConanFile, tools, cppstd


class Recipe(ConanFile):
    name = "compatible"
    settings = "os", "arch", "compiler", "build_type"

    def configure(self):
        self.output.info("This package works for all the C++ standards")

    def package_id(self):
        self.output.info("This package is compatible for all the C++ standards")
