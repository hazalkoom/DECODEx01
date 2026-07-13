#pragma once
#include <vector>
#include <string>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp"

class DependencyExtractor {
public:
    // Walks the AST using the compiled query to extract file-level imports and includes
    static std::vector<Dependency> extract(TSNode root_node, TSQuery* query, const std::string& source_code);
};