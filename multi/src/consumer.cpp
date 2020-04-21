#include <iostream>

#include "boost/header.h"
#include "bleeding_edge/header.h"

#include "message.h"
#include "header.h"


namespace consumer {
    int secret_of_life(int tabs) {
        std::cout << std::string(tabs, '\t') << "> consumer: " << MESSAGE << std::endl;
        boost::secret_of_life(tabs+1);
        bleeding_edge::secret_of_life(tabs+1);
        return 42;
    }
}
