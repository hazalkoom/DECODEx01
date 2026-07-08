#include "ast_parser.hpp"
#include <cstring> // Required for strlen

extern "C" {
    TSLanguage* tree_sitter_python();
}

ASTParser::ASTParser() {
    parser = ts_parser_new();
    // Safety net: Set a 5-second timeout to prevent infinite loops in the
    // parser/scanner. If a parse takes longer than this, ts_parser_parse_string
    // will return NULL rather than hanging forever.
    ts_parser_set_timeout_micros(parser, 5000000);
}

ASTParser::~ASTParser() {
    if (parser != nullptr) {
        ts_parser_delete(parser);
    }
}

bool ASTParser::initialize_python() {
    return ts_parser_set_language(parser, tree_sitter_python());
}

std::string ASTParser::extract_text(TSNode node, const std::string& source_code) {
    uint32_t start = ts_node_start_byte(node);
    uint32_t end = ts_node_end_byte(node);
    
    // Safety check to prevent memory access violations
    if (start >= source_code.length() || end > source_code.length() || start >= end) {
        return ""; 
    }
    return source_code.substr(start, end - start);
}

std::vector<Symbol> ASTParser::parse_code(const std::string& source_code) {
    std::vector<Symbol> symbols;
    
    TSTree* tree = ts_parser_parse_string(parser, nullptr, source_code.c_str(), source_code.length());
    if (tree == nullptr) return symbols;

    TSNode root_node = ts_tree_root_node(tree);

    // 1. The Query: We tell the C engine exactly what we want to find.
    // We want the names of classes and the names of functions.
    const char *query_source = 
        "(class_definition name: (identifier) @class_name) "
        "(function_definition name: (identifier) @func_name)";
    
    uint32_t error_offset;
    TSQueryError error_type;
    
    // 2. Compile the query (Instantly handled by the C library)
    TSQuery* query = ts_query_new(
        tree_sitter_python(), 
        query_source, 
        strlen(query_source), 
        &error_offset, 
        &error_type
    );

    if (query != nullptr) {
        // 3. Execute the query
        TSQueryCursor* cursor = ts_query_cursor_new();
        ts_query_cursor_exec(cursor, query, root_node);

        TSQueryMatch match;
        // 4. Iterate over the direct matches. No manual tree walking!
        while (ts_query_cursor_next_match(cursor, &match)) {
            for (uint16_t i = 0; i < match.capture_count; i++) {
                TSNode name_node = match.captures[i].node;
                uint32_t capture_id = match.captures[i].index;
                
                uint32_t length;
                const char* capture_name = ts_query_capture_name_for_id(query, capture_id, &length);
                std::string type_str(capture_name, length);

                // The match gives us the name (e.g., "connect"). 
                // We ask for the parent node so we can get the start/end lines of the ENTIRE function block.
                TSNode parent_node = ts_node_parent(name_node);

                Symbol sym;
                sym.name = extract_text(name_node, source_code);
                sym.type = (type_str == "class_name") ? "class" : "function";
                sym.start_line = ts_node_start_point(parent_node).row + 1;
                sym.end_line = ts_node_end_point(parent_node).row + 1;
                
                symbols.push_back(sym);
            }
        }

        // 5. Cleanup the query memory
        ts_query_cursor_delete(cursor);
        ts_query_delete(query);
    }

    // 6. Cleanup the tree memory
    ts_tree_delete(tree);
    return symbols;
}