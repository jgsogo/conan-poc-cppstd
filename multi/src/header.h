#pragma once

#if {{ cppstd_checks }}
    #error C++ standard not supported
#endif

namespace {{ namespace }} {
    int secret_of_life(int tabs);
}
