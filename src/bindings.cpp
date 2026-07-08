#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "fs_walker.hpp"
#include "language_detector.hpp"

namespace py = pybind11;

PYBIND11_MODULE(codelens_core, m) {
    // Existing walker
    m.def("walk_repository", &walk_repository, "Recursively walks a directory and returns a list of files, skipping ignored folders.");
    
    // New language detector
    m.def("detect_language", &detect_language, "Detects the programming language of a file based on extension or shebang.");
}