#include <iostream>

#include "message.h"
#include "header.h"


namespace icu {
    int secret_of_life(int tabs) {
        std::cout << std::string(tabs, '\t') << "> icu: " << MESSAGE << std::endl;
        return 42;
    }
}
