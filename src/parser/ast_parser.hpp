#pragma once
#include <string>
#include <vector>
#include <tree_sitter/api.h>
#include "../core/ast_types.hpp"

class ASTParser {
private:
    TSParser* parser;
    TSLanguage* current_language;
    
    std::string symbol_query_str;
    std::string dependency_query_str;

    TSQuery* compile_query(const std::string& query_source);

public:
    ASTParser();
    ~ASTParser();

    bool set_language(const std::string& lang_name);
    
    // We renamed this to perfectly describe what it does!
    std::vector<Symbol> extract_symbols(const std::string& source_code);
    
    // Our brand new Path A function
    std::vector<Dependency> extract_dependencies(const std::string& source_code);
};