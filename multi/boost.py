import os
import re
from conans import ConanFile, tools, cppstd, CMake
from conans.errors import ConanInvalidConfiguration, ConanException, ConanInvalidCppstd


class Recipe(ConanFile):
    python_requires = "pyreq/poc@user/testing"
    python_requires_extend = "pyreq.BaseRecipe"
    _apis = ['98', '11', '14', '17',]
    _abis = ['98', '11', '14', '17',]

    # Recipe starts here
    name = "boost"

    def init(self):
        base = self.python_requires["pyreq"].module.BaseRecipe
        self.exports_sources = base.exports_sources + ('src/boost.cpp', )
        self.options.update({'icu': [True, False]})
        self.default_options.update({'icu': False})

    def requirements(self):
        self.requires("zlib/poc@user/testing")
        if self.options.icu:
            self.requires("icu/poc@user/testing")
