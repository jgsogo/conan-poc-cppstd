cmake_minimum_required(VERSION 3.10)
project(cmake LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(WRITE ${CMAKE_CURRENT_SOURCE_DIR}/message.h "#pragma once\nconst char* const MESSAGE=\"${MESSAGE}\";")

add_library(library header.h source.cpp)
target_compile_definitions(library PUBLIC $<$<BOOL:WORKS_CPP98>:WORKS_CPP98>
                                          $<$<BOOL:WORKS_CPP11>:WORKS_CPP11>
                                          $<$<BOOL:WORKS_CPP14>:WORKS_CPP14>
                                          $<$<BOOL:WORKS_CPP17>:WORKS_CPP17>)

add_executable(executable main.cpp)
target_link_libraries(executable library)
set_target_properties(executable PROPERTIES OUTPUT_NAME ${OUTPUT_NAME})
