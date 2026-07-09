#pragma once
#include <string>
#include <vector>
#include <tree_sitter/api.h>

struct Symbol {
    std::string name;
    std::string type;
    uint32_t start_line;
    uint32_t end_line;
};

class ASTParser {
private:
    TSParser* parser;
    TSLanguage* current_language;
    std::string current_query;
    
    std::string extract_text(TSNode node, const std::string& source_code);

public:
    ASTParser();
    ~ASTParser();

    // The new dynamic language setter
    bool set_language(const std::string& lang_name);
    
    std::vector<Symbol> parse_code(const std::string& source_code);
};