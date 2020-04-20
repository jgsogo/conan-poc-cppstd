
#include <iostream>

#include "header.h"


#if __cplusplus == 199711L
    #ifndef WORKS_CPP98
        #error Build error - C++98 not supported
    #endif
#endif 

#if __cplusplus == 201103L
    #ifndef WORKS_CPP11
        #error Build error - C++11 not supported
    #endif
#endif 

#if __cplusplus == 201402L
    #ifndef WORKS_CPP14
        #error Build error - C++14 not supported
    #endif
#endif 

#if __cplusplus == 201703L
    #ifndef WORKS_CPP17
        #error Build error - C++17 not supported
    #endif
#endif 


int main() {
    std::cout << "{{ namespace }} main" << std::endl;
    std::cout << {{ namespace }}::secret_of_life() << std::endl;
}
