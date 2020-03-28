cmake_minimum_required(VERSION 3.10)
project(cmake LANGUAGES CXX)

file(WRITE ${CMAKE_CURRENT_SOURCE_DIR}/message.h "#pragma once\nconst char* const MESSAGE=\"${MESSAGE}\";")

add_executable(executable main.cpp)
set_target_properties(executable PROPERTIES OUTPUT_NAME ${OUTPUT_NAME})
