import os
import re
from conans import ConanFile, tools, cppstd, CMake
from conans.errors import ConanInvalidConfiguration, ConanException, ConanInvalidCppstd


class Recipe(ConanFile):
    python_requires = "pyreq/1.0@user/testing"
    python_requires_extend = "pyreq.BaseRecipe"

    name = "api111417_abi111417"
    version = "1.0"
