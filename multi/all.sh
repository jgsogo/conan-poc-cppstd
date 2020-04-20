conan export multi/py_req.py user/testing

# ZLib works for all the configurations
conan create multi/zlib.py user/testing --profile=profiles/cpp98
