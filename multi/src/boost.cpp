#include <iostream>

#include "zlib/header.h"
#if USING_ICU
#include "icu/header.h"
#endif

#include "message.h"
#include "header.h"


namespace boost {
    int secret_of_life() {
        std::cout << "> boost: " << MESSAGE << std::endl;
        zlib::secret_of_life();
        #if USING_ICU
        icu::secret_of_life();
        #endif
        return 42;
    }
}
