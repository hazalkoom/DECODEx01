#pragma once
#include <string>
#include <vector>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp"

class ASTParser {
public:
    ASTParser();
    ~ASTParser();

    // Configures the parser engine for the correct language (e.g., Python, C++)
    bool set_language(const std::string& lang_name);

    // THE MASTER METHOD: Replaces extract_symbols and extract_dependencies.
    // Parses the file exactly once, applying all queries simultaneously for maximum efficiency.
    FileContext analyze_file(const std::string& filepath, const std::string& source_code);

private:
    TSParser* parser;
    const TSLanguage* current_language;

    // Cached query strings specific to the currently loaded language
    std::string symbol_query_str;
    std::string dependency_query_str;
    std::string reference_query_str; // NEW: For finding function calls and instantiations

    // Helper to compile raw string queries into Tree-sitter TSQuery objects
    TSQuery* compile_query(const std::string& query_source);
};