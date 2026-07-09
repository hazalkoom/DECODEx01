#pragma once
#include <vector>
#include <string>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp" // Pull in our shared data types!

class DependencyExtractor {
public:
    // A static function means we can call it without creating a new "Extractor" object every time.
    // It takes the tree root, the specific query, and the raw text, and returns a list of Dependencies.
    static std::vector<Dependency> extract(TSNode root_node, TSQuery* query, const std::string& source_code);
};