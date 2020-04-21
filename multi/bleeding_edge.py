import os
import re
from conans import ConanFile, tools, cppstd, CMake
from conans.errors import ConanInvalidConfiguration, ConanException, ConanInvalidCppstd


class Recipe(ConanFile):
    python_requires = "pyreq/poc@user/testing"
    python_requires_extend = "pyreq.BaseRecipe"
    _apis = ['14', '17',]
    _abis = ['14', '17',]

    # Recipe starts here
    name = "bleeding_edge"

    cppstd_compatibility = [(cppstd.CPPSTD_14, ), 
                            (cppstd.CPPSTD_17, )]

    def init(self):
        base = self.python_requires["pyreq"].module.BaseRecipe
        self.exports_sources = base.exports_sources + ('src/bleeding_edge.cpp', )

    def requirements(self):
        self.requires("zlib/poc@user/testing")