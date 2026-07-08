cmake_minimum_required(VERSION 3.15)
project(DECODEx01Core)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(codelens_core src/bindings.cpp src/fs_walker.cpp src/language_detector.cpp)

install(TARGETS codelens_core DESTINATION .)