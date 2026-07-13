#pragma once
#include <vector>
#include <string>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp"

class ReferenceExtractor {
public:
    // Walks the AST to find function calls, method calls, and object instantiations
    static std::vector<Reference> extract(TSNode root_node, TSQuery* query, const std::string& source_code);

private:
    // Safely slices text out of the source code string via node byte offsets
    static std::string extract_text(TSNode node, const std::string& source_code);

    // Context-Aware Scope: Walks UP the AST from a function call to figure out 
    // which function/method is actually making the call. 
    // This is the secret to building an unbreakable Call Graph.
    static std::string determine_caller_fqn(TSNode node, const std::string& source_code);
};