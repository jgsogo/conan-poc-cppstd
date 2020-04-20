import os
import re
from conans import ConanFile, tools, cppstd, CMake
from conans.errors import ConanInvalidConfiguration, ConanException, ConanInvalidCppstd



class Recipe(ConanFile):
    python_requires = "pyreq/0.1@user/testing"
    python_requires_extend = "pyreq.BaseRecipe"
