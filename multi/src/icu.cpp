#include <iostream>

#include "message.h"
#include "header.h"


namespace icu {
    int secret_of_life() {
        std::cout << "> icu: " << MESSAGE << std::endl;
        return 42;
    }
}
