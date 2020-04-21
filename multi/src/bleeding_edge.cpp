#include <iostream>

#include "zlib/header.h"

#include "message.h"
#include "header.h"


namespace bleeding_edge {
    int secret_of_life(int tabs) {
        std::cout << std::string(tabs, '\t') << "> bleeding_edge: " << MESSAGE << std::endl;
        zlib::secret_of_life(tabs+1);
        return 42;
    }
}
