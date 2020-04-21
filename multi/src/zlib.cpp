#include <iostream>

#include "message.h"
#include "header.h"


namespace zlib {
    int secret_of_life(int tabs) {
        std::cout << std::string(tabs, '\t') << "> zlib: " << MESSAGE << std::endl;
        return 42;
    }
}
