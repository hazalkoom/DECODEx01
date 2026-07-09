#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "fs_walker.hpp"
#include "language_detector.hpp"
#include "ast_parser.hpp"

namespace py = pybind11;

PYBIND11_MODULE(codelens_core, m) {
    m.def("walk_repository", &walk_repository, "Recursively walks a directory.");
    m.def("detect_language", &detect_language, "Detects the programming language.");
    
    py::class_<Symbol>(m, "Symbol")
        .def_readonly("name", &Symbol::name)
        .def_readonly("type", &Symbol::type)
        .def_readonly("start_line", &Symbol::start_line)
        .def_readonly("end_line", &Symbol::end_line);

    py::class_<ASTParser>(m, "ASTParser")
        .def(py::init<>())
        // NEW: We now pass the language name string!
        .def("set_language", &ASTParser::set_language, "Sets the active parser grammar (e.g., 'python', 'javascript')")
        .def("parse_code", &ASTParser::parse_code, "Parses source code and extracts functions and classes.");
}