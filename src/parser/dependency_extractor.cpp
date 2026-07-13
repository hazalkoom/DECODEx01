#include "dependency_extractor.hpp"

// Internal helper to safely cut the exact word out of the source code string
static std::string extract_text(TSNode node, const std::string& source_code) {
    uint32_t start = ts_node_start_byte(node);
    uint32_t end = ts_node_end_byte(node);
    if (start >= source_code.length() || end > source_code.length() || start >= end) return ""; 
    return source_code.substr(start, end - start);
}

std::vector<Dependency> DependencyExtractor::extract(TSNode root_node, TSQuery* query, const std::string& source_code) {
    std::vector<Dependency> dependencies;
    if (query == nullptr) return dependencies;

    TSQueryCursor* cursor = ts_query_cursor_new();
    ts_query_cursor_exec(cursor, query, root_node);

    TSQueryMatch match;
    while (ts_query_cursor_next_match(cursor, &match)) {
        Dependency dep;
        dep.line_number = 0;
        
        for (uint16_t i = 0; i < match.capture_count; i++) {
            TSNode node = match.captures[i].node;
            uint32_t capture_id = match.captures[i].index;
            
            uint32_t length;
            const char* capture_name = ts_query_capture_name_for_id(query, capture_id, &length);
            std::string capture_str(capture_name, length);

            if (capture_str == "module_name") {
                dep.module_name = extract_text(node, source_code);
                dep.line_number = ts_node_start_point(node).row + 1;
            } 
            else if (capture_str == "imported_name") {
                dep.imported_name = extract_text(node, source_code);
            }
        }
        
        if (!dep.module_name.empty()) {
            dependencies.push_back(dep);
        }
    }
    
    ts_query_cursor_delete(cursor);
    return dependencies;
}