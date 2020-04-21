# Remove everything
conan remove pyreq/poc@user/testing -f
conan remove zlib/poc@user/testing -f
conan remove boost/poc@user/testing -f
conan remove icu/poc@user/testing -f
conan remove bleeding_edge/poc@user/testing -f

# Export all the recipes
conan export multi/pyreq.py pyreq/poc@user/testing
conan export multi/zlib.py zlib/poc@user/testing
conan export multi/boost.py boost/poc@user/testing
conan export multi/icu.py icu/poc@user/testing
conan export multi/bleeding_edge.py bleeding_edge/poc@user/testing

# ZLib: works for all the configurations (c-library). Compile only default
conan create multi/zlib.py zlib/poc@user/testing --profile=profiles/cpp98

# Boost: so big, that every cppstd makes a different binary family
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp98
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp11
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp14
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp17

# ICU: requires >= C++11
conan create multi/icu.py icu/poc@user/testing --profile=profiles/cpp11

# bleeding_edge: latests features for C++14 or C++17
conan create multi/bleeding_edge.py bleeding_edge/poc@user/testing --profile=profiles/cpp14
conan create multi/bleeding_edge.py bleeding_edge/poc@user/testing --profile=profiles/cpp17
