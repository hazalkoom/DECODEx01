#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../core/fs_walker.hpp"
#include "../core/language_detector.hpp"
#include "../parser/ast_parser.hpp"

namespace py = pybind11;

PYBIND11_MODULE(codelens_core, m) {
    m.def("walk_repository", &walk_repository, "Recursively walks a directory.");
    m.def("detect_language", &detect_language, "Detects the programming language.");
    
    // 1. Expose Enums for type safety in Python
    py::enum_<SymbolKind>(m, "SymbolKind")
        .value("Class", SymbolKind::Class)
        .value("Function", SymbolKind::Function)
        .value("Method", SymbolKind::Method)
        .value("Interface", SymbolKind::Interface)
        .value("Variable", SymbolKind::Variable)
        .value("Unknown", SymbolKind::Unknown)
        .export_values();

    py::enum_<ReferenceKind>(m, "ReferenceKind")
        .value("Call", ReferenceKind::Call)
        .value("Instantiation", ReferenceKind::Instantiation)
        .value("Inheritance", ReferenceKind::Inheritance)
        .value("Usage", ReferenceKind::Usage)
        .value("Unknown", ReferenceKind::Unknown)
        .export_values();

    // 2. Expose the deeply detailed Symbol struct
    py::class_<Symbol>(m, "Symbol")
        .def_readonly("name", &Symbol::name)
        .def_readonly("fully_qualified_name", &Symbol::fully_qualified_name)
        .def_readonly("signature", &Symbol::signature)
        .def_readonly("return_type", &Symbol::return_type)
        .def_readonly("kind", &Symbol::kind)
        .def_readonly("docstring", &Symbol::docstring)
        .def_readonly("start_line", &Symbol::start_line)
        .def_readonly("end_line", &Symbol::end_line);

    // 3. Expose the Dependency struct
    py::class_<Dependency>(m, "Dependency")
        .def_readonly("module_name", &Dependency::module_name)
        .def_readonly("imported_name", &Dependency::imported_name)
        .def_readonly("line_number", &Dependency::line_number);

    // 4. Expose the new Reference struct for the Call Graph
    py::class_<Reference>(m, "Reference")
        .def_readonly("caller_fqn", &Reference::caller_fqn)
        .def_readonly("callee_fqn", &Reference::callee_fqn)
        .def_readonly("kind", &Reference::kind)
        .def_readonly("line_number", &Reference::line_number);

    // 5. Expose the Master Record Payload
    py::class_<FileContext>(m, "FileContext")
        .def_readonly("filepath", &FileContext::filepath)
        .def_readonly("language", &FileContext::language)
        .def_readonly("symbols", &FileContext::symbols)
        .def_readonly("dependencies", &FileContext::dependencies)
        .def_readonly("references", &FileContext::references);

    // 6. Bind the upgraded ASTParser with the Single-Pass method
    py::class_<ASTParser>(m, "ASTParser")
        .def(py::init<>())
        .def("set_language", &ASTParser::set_language)
        .def("analyze_file", &ASTParser::analyze_file, "Extracts symbols, dependencies, and references in one pass.")
        .def("extract_symbols", [](ASTParser& self, const std::string& source_code) {
            return self.analyze_file("dummy.py", source_code).symbols;
        }, "Legacy method for backwards compatibility, calls analyze_file under the hood.")
        .def("extract_dependencies", [](ASTParser& self, const std::string& source_code) {
            return self.analyze_file("dummy.py", source_code).dependencies;
        }, "Legacy method for backwards compatibility, calls analyze_file under the hood.");
}