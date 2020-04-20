#include <iostream>

#include "zlib/header.h"
#include "message.h"
#include "header.h"


namespace boost {
    int secret_of_life() {
        std::cout << "> boost: " << MESSAGE << std::endl;
        zlib::secret_of_life();
        return 42;
    }
}
