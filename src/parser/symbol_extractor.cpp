#include "symbol_extractor.hpp"

// Internal helper to safely cut the exact word out of the source code string
static std::string extract_text(TSNode node, const std::string& source_code) {
    uint32_t start = ts_node_start_byte(node);
    uint32_t end = ts_node_end_byte(node);
    if (start >= source_code.length() || end > source_code.length() || start >= end) return ""; 
    return source_code.substr(start, end - start);
}

std::vector<Symbol> SymbolExtractor::extract(TSNode root_node, TSQuery* query, const std::string& source_code) {
    std::vector<Symbol> symbols;
    if (query == nullptr) return symbols;

    TSQueryCursor* cursor = ts_query_cursor_new();
    ts_query_cursor_exec(cursor, query, root_node);

    TSQueryMatch match;
    while (ts_query_cursor_next_match(cursor, &match)) {
        for (uint16_t i = 0; i < match.capture_count; i++) {
            TSNode name_node = match.captures[i].node;
            uint32_t capture_id = match.captures[i].index;
            
            // Get the name of the tag (e.g., "class_name" or "func_name")
            uint32_t length;
            const char* capture_name = ts_query_capture_name_for_id(query, capture_id, &length);
            std::string type_str(capture_name, length);

            // We ask for the parent node so we get the start/end lines of the ENTIRE function block.
            TSNode parent_node = ts_node_parent(name_node);

            Symbol sym;
            sym.name = extract_text(name_node, source_code);
            sym.type = (type_str == "class_name") ? "class" : "function";
            sym.start_line = ts_node_start_point(parent_node).row + 1;
            sym.end_line = ts_node_end_point(parent_node).row + 1;
            
            symbols.push_back(sym);
        }
    }
    
    // Clean up memory
    ts_query_cursor_delete(cursor);
    return symbols;
}