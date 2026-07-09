#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../core/fs_walker.hpp"
#include "../core/language_detector.hpp"
#include "../parser/ast_parser.hpp"

namespace py = pybind11;

PYBIND11_MODULE(codelens_core, m) {
    m.def("walk_repository", &walk_repository, "Recursively walks a directory.");
    m.def("detect_language", &detect_language, "Detects the programming language.");
    
    py::class_<Symbol>(m, "Symbol")
        .def_readonly("name", &Symbol::name)
        .def_readonly("type", &Symbol::type)
        .def_readonly("start_line", &Symbol::start_line)
        .def_readonly("end_line", &Symbol::end_line);

    // NEW: Expose Dependency object to Python
    py::class_<Dependency>(m, "Dependency")
        .def_readonly("module_name", &Dependency::module_name)
        .def_readonly("imported_name", &Dependency::imported_name)
        .def_readonly("line_number", &Dependency::line_number);

    py::class_<ASTParser>(m, "ASTParser")
        .def(py::init<>())
        .def("set_language", &ASTParser::set_language)
        // Renamed to match the new architecture
        .def("extract_symbols", &ASTParser::extract_symbols, "Extracts functions and classes.")
        // NEW:
        .def("extract_dependencies", &ASTParser::extract_dependencies, "Extracts imports and includes.");
}