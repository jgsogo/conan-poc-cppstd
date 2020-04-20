conan export multi/py_req.py pyreq/poc@user/testing

# ZLib: works for all the configurations (c-library). Compile only default
conan create multi/zlib.py zlib/poc@user/testing --profile=profiles/cpp98

# Boost: so big, that every cppstd makes a different binary family
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp98
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp11
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp14
conan create multi/boost.py boost/poc@user/testing --profile=profiles/cpp17

