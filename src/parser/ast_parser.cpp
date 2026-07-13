#include "ast_parser.hpp"
#include "symbol_extractor.hpp"
#include "dependency_extractor.hpp"
#include "reference_extractor.hpp"

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

bool ASTParser::set_language(const std::string& lang_name) {
    if (lang_name == "Python" || lang_name == "python") {
        current_language = tree_sitter_python();
        symbol_query_str = "(class_definition name: (identifier) @class_name) (function_definition name: (identifier) @func_name)";
        dependency_query_str = 
            "(import_statement name: (dotted_name) @module_name) "
            "(import_statement name: (aliased_import name: (dotted_name) @module_name)) "
            "(import_from_statement module_name: (_) @module_name)";
        reference_query_str = 
            "(call function: (identifier) @callee_name) "
            "(call function: (attribute attribute: (identifier) @callee_name))";
    } 
    else if (lang_name == "JavaScript" || lang_name == "javascript") {
        current_language = tree_sitter_javascript();
        symbol_query_str = "(class_declaration name: (identifier) @class_name) (function_declaration name: (identifier) @func_name) (method_definition name: (property_identifier) @func_name)";
        dependency_query_str = 
            "(import_statement source: (string) @module_name) "
            "(export_statement source: (string) @module_name)";
        reference_query_str = 
            "(call_expression function: (identifier) @callee_name) "
            "(call_expression function: (member_expression property: (property_identifier) @callee_name))";
    }
    else if (lang_name == "C++" || lang_name == "cpp") {
        current_language = tree_sitter_cpp();
        symbol_query_str = 
            "(class_specifier name: (type_identifier) @class_name) "
            "(function_definition declarator: (function_declarator declarator: (identifier) @func_name)) "
            "(function_definition declarator: (function_declarator declarator: (field_identifier) @func_name))";
        dependency_query_str = "(preproc_include path: (_) @module_name)";
        reference_query_str = 
            "(call_expression function: (identifier) @callee_name) "
            "(call_expression function: (field_expression field: (field_identifier) @callee_name))";
    }
    else if (lang_name == "Go" || lang_name == "go") {
        current_language = tree_sitter_go();
        symbol_query_str = "(type_spec name: (type_identifier) @class_name) (function_declaration name: (identifier) @func_name) (method_declaration name: (field_identifier) @func_name)";
        dependency_query_str = "(import_spec path: (interpreted_string_literal) @module_name)";
        reference_query_str = 
            "(call_expression function: (identifier) @callee_name) "
            "(call_expression function: (selector_expression field: (field_identifier) @callee_name))";
    }
    else if (lang_name == "Rust" || lang_name == "rust") {
        current_language = tree_sitter_rust();
        symbol_query_str = "(struct_item name: (type_identifier) @class_name) (function_item name: (identifier) @func_name)";
        dependency_query_str = "(use_declaration argument: (_) @module_name)";
        reference_query_str = 
            "(call_expression function: (identifier) @callee_name) "
            "(call_expression function: (field_expression field: (field_identifier) @callee_name))";
    }
    else if (lang_name == "Shell" || lang_name == "bash") {
        current_language = tree_sitter_bash();
        symbol_query_str = "(function_definition name: (word) @func_name)";
        dependency_query_str = "";
        reference_query_str = ""; // Bash function calls are harder to reliably extract with basic queries
    }
    else if (lang_name == "JSON" || lang_name == "json") {
        current_language = tree_sitter_json();
        symbol_query_str = ""; dependency_query_str = ""; reference_query_str = "";
    }
    else if (lang_name == "YAML" || lang_name == "yaml") {
        current_language = tree_sitter_yaml();
        symbol_query_str = ""; dependency_query_str = ""; reference_query_str = "";
    }
    else {
        return false; 
    }
    return ts_parser_set_language(parser, current_language);
}

TSQuery* ASTParser::compile_query(const std::string& query_source) {
    if (query_source.empty() || current_language == nullptr) return nullptr;
    uint32_t error_offset;
    TSQueryError error_type;
    return ts_query_new(current_language, query_source.c_str(), query_source.length(), &error_offset, &error_type);
}

FileContext ASTParser::analyze_file(const std::string& filepath, const std::string& source_code) {
    FileContext context;
    context.filepath = filepath;

    if (current_language == nullptr) return context; 

    // 1. PARSE ONCE: Convert the raw string into an AST
    TSTree* tree = ts_parser_parse_string(parser, nullptr, source_code.c_str(), source_code.length());
    if (tree == nullptr) return context;

    TSNode root_node = ts_tree_root_node(tree);

    // 2. EXTRACT SYMBOLS
    TSQuery* symbol_query = compile_query(symbol_query_str);
    if (symbol_query != nullptr) {
        context.symbols = SymbolExtractor::extract(root_node, symbol_query, source_code);
        ts_query_delete(symbol_query);
    }

    // 3. EXTRACT DEPENDENCIES
    TSQuery* dep_query = compile_query(dependency_query_str);
    if (dep_query != nullptr) {
        context.dependencies = DependencyExtractor::extract(root_node, dep_query, source_code);
        ts_query_delete(dep_query);
    }

    // 4. EXTRACT REFERENCES
    TSQuery* ref_query = compile_query(reference_query_str);
    if (ref_query != nullptr) {
        context.references = ReferenceExtractor::extract(root_node, ref_query, source_code);
        ts_query_delete(ref_query);
    }

    ts_tree_delete(tree);
    
    return context;
}