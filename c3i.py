import os
import sys
import subprocess
import tempfile

from conans.client.build.cppstd_flags import cppstd_default
from conans.cppstd import ALL_CPPSTD


def main(recipe):
    settings = {'os': 'Linux',
                'arch': 'x86_64',
                'compiler': 'gcc',
                'compiler.version': '8',
                'compiler.libcxx': 'libstdc++11',
                'build_type': 'Release'}
    # Iterate all the 'cppstd' (start with the default one) to discover which one to build
    #   - first the default, then the rest
    default_cppstd = cppstd_default(settings['compiler'], settings['compiler.version'])
    cppstd_to_iterate = [it for it in ALL_CPPSTD if it != default_cppstd] + [default_cppstd, ]
    cppstd_to_iterate.reverse()

    list_to_compile = []
    already_seen = set()
    for it in cppstd_to_iterate:
        #   - run 'conan package_id' for each profile
        sys.stdout.write(f" - cppstd: {it}\n")
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as profile:
            profile.write("[settings]\n")
            for key, value in settings.items():
                profile.write(f"{key}={value}\n")
            profile.write(f"compiler.cppstd={it}\n")
            profile.close()
            profile_file = profile.name

            out, _ = subprocess.Popen(['conan', 'package_id', recipe, '--profile', profile_file], stdout=subprocess.PIPE, shell=False).communicate()
            out = out.decode('utf-8')
            os.unlink(profile_file)

        #   - get 'package_id' and compatible ones
        own_pkg_id = None
        compatible = []
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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Computation of profiles to build in C3i.')
    parser.add_argument('recipe', type=str, help='recipe to work with')
    args = parser.parse_args()

    recipe = os.path.abspath(args.recipe)
    sys.stdout.write("Work on recipe '{}'\n".format(recipe))
    main(recipe)
