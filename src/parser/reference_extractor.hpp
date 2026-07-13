#pragma once
#include <vector>
#include <string>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp"

class ReferenceExtractor {
public:
    // Takes the root AST node, the compiled query, and the raw source code
    // Returns a list of all function calls and object instantiations.
    static std::vector<Reference> extract(TSNode root_node, TSQuery* query, const std::string& source_code);
};