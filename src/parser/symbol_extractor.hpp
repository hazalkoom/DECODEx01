#pragma once
#include <vector>
#include <string>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp" // Pull in our shared data types

class SymbolExtractor {
public:
    // Takes the tree root, the specific query, and the raw text, and returns a list of Symbols (Functions/Classes).
    static std::vector<Symbol> extract(TSNode root_node, TSQuery* query, const std::string& source_code);
};