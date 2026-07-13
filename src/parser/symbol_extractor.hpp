#pragma once
#include <vector>
#include <string>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp"

class SymbolExtractor {
public:
    // Walks the AST using the compiled query to gather symbols with complete structural context
    static std::vector<Symbol> extract(TSNode root_node, TSQuery* query, const std::string& source_code);

private:
    // Helper to find a leading comment or docstring attached to a structural node
    static std::string extract_docstring(TSNode node, const std::string& source_code);

    // Helper to build the fully qualified name and infer parent scopes
    static std::string build_fully_qualified_name(TSNode node, const std::string& source_code);

    // Helper to capture the parameters/arguments line for the function signature
    static std::string extract_signature(TSNode node, const std::string& source_code);

    // Helper to extract the real return type from Python `-> Type` annotations or C++ return type nodes
    static std::string extract_return_type(TSNode name_node, const std::string& source_code);
};