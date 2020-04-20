import os
import re
from conans import ConanFile, tools, cppstd, CMake
from conans.errors import ConanInvalidConfiguration, ConanException, ConanInvalidCppstd


def std_from_name(name):
    m = re.match(r'^[a-z]+(\d+)_[a-z]+(\d+)$', name)
    if not m:
        raise ConanException(f"name '{name}' doesn't match pattern")
    
    public = m.group(1)
    private = m.group(2)

    def get_cppstds(group):
        t = list(zip(group[::2], group[1::2]))
        t = ["".join(p) for p in t]
        return t
    
    return get_cppstds(public), get_cppstds(private)


def write_header(ofstream, apis):
    ofstream.write("#pragma once\n\n")
    # mymachine dict:
    cplusplus = {'98': '199711L', '11': '201103L', '14': '201402L', '17': '201703'}
    if_checks = " && ".join([f"__cplusplus != {cplusplus[it]}" for it in apis])
    ofstream.write(f"#if {if_checks}\n")
    ofstream.write(f"    #error C++ standard not supported\n")
    ofstream.write(f"#endif\n\n")

    ofstream.write(f"int secret_of_life();")


class Recipe(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "src/*"
    generators = "cmake"
    options = {'shared': [True, False]}
    default_options = {'shared': False}

    def configure(self):
        self.output.info(f"Compatibility for {self.name}:")
        self._apis, self._abis = std_from_name(self.name)
        self.output.info(f" - API compatible: {', '.join(self._apis)}")
        self.output.info(f" - ABI compatible: {', '.join(self._abis)}")
        # Private part has to be equal or more restrictive than public
        assert all([it in self._apis for it in self._abis]), "All from ABI are not contained in ABIS"

        cppstd_value, _ = cppstd.get_cppstd(self)
        self.output.info(f"Profile is using {cppstd_value}")

        if cppstd_value not in self._apis:
            raise ConanInvalidConfiguration(f"API incompatible with '{cppstd_value}' (requires: {', '.join(self._apis)})")
        if cppstd_value not in self._abis:
            raise ConanInvalidCppstd(f"Cannot compile using '{cppstd_value}' (requires: {', '.join(self._abis)})")

    def build(self):
        with open(os.path.join("src", "header.h"), "w") as f:
            write_header(f, self._apis)
        cmake = CMake(self)
        settings = "|".join(map(str, [self.settings.os, self.settings.compiler, self.settings.compiler.cppstd]))
        cmake.definitions["MESSAGE:STRING"] = settings
        cmake.definitions["OUTPUT_NAME:STRING"] = self.name
        for it in self._abis:
            cmake.definitions[f"WORKS_CPP{it}:BOOL"] = True
        cmake.configure(source_folder="src")
        cmake.build()
    
    def package(self):
        self.copy(f"{self.name}*", src="bin", dst="bin", keep_path=False)
        self.copy(f"*.h", src="src", dst="include", keep_path=True)
        self.copy(f"*library*", src="bin", dst="bin", keep_path=False)
        self.copy(f"*library*", src="lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['library', ]
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        self.output.info("This package is compatible for all the C++ standards")
