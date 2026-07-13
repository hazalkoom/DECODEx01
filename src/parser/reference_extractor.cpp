#include "reference_extractor.hpp"
#include <string_view>

std::vector<Reference> ReferenceExtractor::extract(TSNode root_node, TSQuery* query, const std::string& source_code) {
    std::vector<Reference> references;
    if (query == nullptr) return references;

    TSQueryCursor* cursor = ts_query_cursor_new();
    ts_query_cursor_exec(cursor, query, root_node);

    TSQueryMatch match;
    // Loop through every time our query matches a function call in the AST
    while (ts_query_cursor_next_match(cursor, &match)) {
        for (uint16_t i = 0; i < match.capture_count; ++i) {
            TSNode capture_node = match.captures[i].node;
            
            // Extract the exact start and end bytes of the function name
            uint32_t start_byte = ts_node_start_byte(capture_node);
            uint32_t end_byte = ts_node_end_byte(capture_node);
            
            // Prevent out-of-bounds memory access
            if (end_byte <= source_code.length() && start_byte < end_byte) {
                Reference ref;
                // Slice the source code to get the actual function name being called
                ref.callee_name = source_code.substr(start_byte, end_byte - start_byte);
                // Tree-sitter is 0-indexed, so we add 1 for standard human-readable line numbers
                ref.line_number = ts_node_start_point(capture_node).row + 1;
                
                references.push_back(ref);
            }
        }
    }

    ts_query_cursor_delete(cursor);
    return references;
}