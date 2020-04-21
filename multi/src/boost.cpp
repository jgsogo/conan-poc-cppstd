#include <iostream>

#include "zlib/header.h"
#if USING_ICU
#include "icu/header.h"
#endif

#include "message.h"
#include "header.h"


namespace boost {
    int secret_of_life(int tabs) {
        std::cout << std::string(tabs, '\t') << "> boost: " << MESSAGE << std::endl;
        zlib::secret_of_life(tabs+1);
        #if USING_ICU
        icu::secret_of_life(tabs+1);
        #endif
        return 42;
    }
}
