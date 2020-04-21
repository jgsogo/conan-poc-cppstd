import os
import sys
import subprocess
import tempfile
from collections import namedtuple

from conans.client.build.cppstd_flags import cppstd_default
from conans.cppstd import ALL_CPPSTD
from conans.client.conf import get_default_settings_yml
from conans.model.settings import Settings


def main(recipe, reference):
    settings = Settings.loads(get_default_settings_yml())
    settings.os = 'Macos'
    settings.arch = 'x86_64'
    settings.compiler = 'apple-clang'
    settings.compiler.version = '11.0'
    settings.compiler.libcxx = 'libc++'
    settings.build_type = 'Release'

    # Iterate all the 'cppstd' (start with the default one) to discover which one to build
    #   - first the default, then the rest
    default_cppstd = cppstd_default(settings)
    cppstd_to_iterate = [it for it in ALL_CPPSTD if it != default_cppstd] + [default_cppstd, ]
    cppstd_to_iterate.reverse()

    list_to_compile = []
    already_seen = set()
    for it in cppstd_to_iterate:
        #   - run 'conan package_id' for each profile
        sys.stdout.write(f"=== Running with CPPSTD: {it}\n")
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as profile:
            profile.write("[settings]\n")
            for key, value in settings.items():
                profile.write(f"{key}={value}\n")
            profile.write(f"compiler.cppstd={it}\n")
            profile.close()
            profile_file = profile.name

            out, err = subprocess.Popen(['conan', 'package_id', recipe, '--profile', profile_file], stdout=subprocess.PIPE, shell=False).communicate()
            if not out:
                continue
            out = out.decode('utf-8')
            os.unlink(profile_file)

        #   - get 'package_id' and compatible ones
        own_pkg_id = None
        compatible = []
        print(out)
        for line in out.splitlines():
            if line.startswith("Package ID:"):
                own_pkg_id = line.split(":", 1)[1].strip()
            elif line.startswith(" - "):
                compatible.append(line[3:].strip())
        
        sys.stdout.write(f"   + {own_pkg_id}\n")
        sys.stdout.write(f"   + {', '.join(compatible)}\n")

        if not own_pkg_id in already_seen:
            list_to_compile.append(it)

        already_seen.add(own_pkg_id)
        already_seen.update(compatible)

        sys.stdout.write(f"   >> to compile: {', '.join(list_to_compile)}\n")
        sys.stdout.write(f"   >> already seen: {', '.join(already_seen)}\n")

    sys.stdout.write("-"*20 + "\n")
    if reference:
        for it in list_to_compile:
            sys.stdout.write(f"conan create {recipe} {reference} --profile=profiles/cpp{it}\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Computation of profiles to build in C3i.')
    parser.add_argument('path_to_recipe', type=str, help='recipe to work with')
    parser.add_argument('reference', type=str, help='reference (only for CLI suggestion at the end)')
    args = parser.parse_args()

    sys.stdout.write("Work on recipe '{}'\n".format(args.path_to_recipe))
    main(args.path_to_recipe, args.reference)
