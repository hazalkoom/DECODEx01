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

    // 1. Create a cursor to execute the search
    TSQueryCursor* cursor = ts_query_cursor_new();
    ts_query_cursor_exec(cursor, query, root_node);

    TSQueryMatch match;
    
    // 2. Loop through every time the query finds a match in the file
    while (ts_query_cursor_next_match(cursor, &match)) {
        Dependency dep;
        dep.line_number = 0;
        
        // 3. A single match might have multiple "captures" (like @module_name and @imported_name)
        for (uint16_t i = 0; i < match.capture_count; i++) {
            TSNode node = match.captures[i].node;
            uint32_t capture_id = match.captures[i].index;
            
            // Get the name of the tag (e.g., "module_name")
            uint32_t length;
            const char* capture_name = ts_query_capture_name_for_id(query, capture_id, &length);
            std::string capture_str(capture_name, length);

            // 4. If the tag is "@module_name", save it to dep.module_name
            if (capture_str == "module_name") {
                dep.module_name = extract_text(node, source_code);
                dep.line_number = ts_node_start_point(node).row + 1; // +1 to make it human-readable
            } 
            // 5. If the tag is "@imported_name", save it to dep.imported_name
            else if (capture_str == "imported_name") {
                dep.imported_name = extract_text(node, source_code);
            }
        }
        
        // Only save the dependency if we actually extracted a valid module name
        if (!dep.module_name.empty()) {
            dependencies.push_back(dep);
        }
    }
    
    // Clean up memory
    ts_query_cursor_delete(cursor);
    return dependencies;
}