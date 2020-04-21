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
    name = "consumer"

    def init(self):
        base = self.python_requires["pyreq"].module.BaseRecipe
        self.exports_sources = base.exports_sources + ('src/consumer.cpp', )

    def requirements(self):
        self.requires("boost/poc@user/testing")
        self.requires("bleeding_edge/poc@user/testing")