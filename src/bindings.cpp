#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "fs_walker.hpp" // Pull in our logic

namespace py = pybind11;

PYBIND11_MODULE(codelens_core, m) {
    m.def("walk_repository", &walk_repository, "Recursively walks a directory and returns a list of files, skipping ignored folders.");
}