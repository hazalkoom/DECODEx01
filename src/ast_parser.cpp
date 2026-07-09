#include "ast_parser.hpp"
#include <cstring>

// 1. Declare all the external C grammar loaders
extern "C" {
    TSLanguage* tree_sitter_python();
    TSLanguage* tree_sitter_javascript();
    TSLanguage* tree_sitter_cpp();
    TSLanguage* tree_sitter_go();
    TSLanguage* tree_sitter_rust();
    TSLanguage* tree_sitter_bash();
    TSLanguage* tree_sitter_json();
    TSLanguage* tree_sitter_yaml();
}

ASTParser::ASTParser() {
    parser = ts_parser_new();
    ts_parser_set_timeout_micros(parser, 5000000); 
    current_language = nullptr;
}

ASTParser::~ASTParser() {
    if (parser != nullptr) ts_parser_delete(parser);
}

// 2. The Master Language Routing Table
bool ASTParser::set_language(const std::string& lang_name) {
    if (lang_name == "Python" || lang_name == "python") {
        current_language = tree_sitter_python();
        current_query = "(class_definition name: (identifier) @class_name) (function_definition name: (identifier) @func_name)";
    } 
    else if (lang_name == "JavaScript" || lang_name == "javascript") {
        current_language = tree_sitter_javascript();
        current_query = "(class_declaration name: (identifier) @class_name) (function_declaration name: (identifier) @func_name) (method_definition name: (property_identifier) @func_name)";
    }
    else if (lang_name == "C++" || lang_name == "cpp") {
        current_language = tree_sitter_cpp();
        current_query = "(class_specifier name: (type_identifier) @class_name) (function_definition declarator: (function_declarator declarator: (identifier) @func_name))";
    }
    else if (lang_name == "Go" || lang_name == "go") {
        current_language = tree_sitter_go();
        current_query = "(type_spec name: (type_identifier) @class_name) (function_declaration name: (identifier) @func_name) (method_declaration name: (field_identifier) @func_name)";
    }
    else if (lang_name == "Rust" || lang_name == "rust") {
        current_language = tree_sitter_rust();
        current_query = "(struct_item name: (type_identifier) @class_name) (function_item name: (identifier) @func_name)";
    }
    else if (lang_name == "Shell" || lang_name == "bash") {
        current_language = tree_sitter_bash();
        current_query = "(function_definition name: (word) @func_name)";
    }
    else if (lang_name == "JSON" || lang_name == "json") {
        current_language = tree_sitter_json();
        current_query = ""; // JSON has no functions to extract
    }
    else if (lang_name == "YAML" || lang_name == "yaml") {
        current_language = tree_sitter_yaml();
        current_query = ""; // YAML has no functions to extract
    }
    else {
        return false; 
    }

    return ts_parser_set_language(parser, current_language);
}

std::string ASTParser::extract_text(TSNode node, const std::string& source_code) {
    uint32_t start = ts_node_start_byte(node);
    uint32_t end = ts_node_end_byte(node);
    if (start >= source_code.length() || end > source_code.length() || start >= end) return ""; 
    return source_code.substr(start, end - start);
}

std::vector<Symbol> ASTParser::parse_code(const std::string& source_code) {
    std::vector<Symbol> symbols;
    if (current_language == nullptr) return symbols; 
    
    TSTree* tree = ts_parser_parse_string(parser, nullptr, source_code.c_str(), source_code.length());
    if (tree == nullptr) return symbols;

    TSNode root_node = ts_tree_root_node(tree);
    
    // If the language doesn't have a query (like JSON), just return empty symbols (no crash)
    if (current_query.empty()) {
        ts_tree_delete(tree);
        return symbols;
    }

    uint32_t error_offset;
    TSQueryError error_type;
    
    TSQuery* query = ts_query_new(current_language, current_query.c_str(), current_query.length(), &error_offset, &error_type);

    if (query != nullptr) {
        TSQueryCursor* cursor = ts_query_cursor_new();
        ts_query_cursor_exec(cursor, query, root_node);

        TSQueryMatch match;
        while (ts_query_cursor_next_match(cursor, &match)) {
            for (uint16_t i = 0; i < match.capture_count; i++) {
                TSNode name_node = match.captures[i].node;
                uint32_t capture_id = match.captures[i].index;
                
                uint32_t length;
                const char* capture_name = ts_query_capture_name_for_id(query, capture_id, &length);
                std::string type_str(capture_name, length);

                TSNode parent_node = ts_node_parent(name_node);

                Symbol sym;
                sym.name = extract_text(name_node, source_code);
                sym.type = (type_str == "class_name") ? "class" : "function";
                sym.start_line = ts_node_start_point(parent_node).row + 1;
                sym.end_line = ts_node_end_point(parent_node).row + 1;
                
                symbols.push_back(sym);
            }
        }
        ts_query_cursor_delete(cursor);
        ts_query_delete(query);
    }

    ts_tree_delete(tree);
    return symbols;
}