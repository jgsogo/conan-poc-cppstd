#include <iostream>

#include "message.h"
#include "header.h"


namespace zlib {
    int secret_of_life() {
        std::cout << "> zlib: " << MESSAGE << std::endl;
        return 42;
    }
}
