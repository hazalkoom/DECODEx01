#include "reference_extractor.hpp"
#include <string_view>

std::string ReferenceExtractor::extract_text(TSNode node, const std::string& source_code) {
    uint32_t start = ts_node_start_byte(node);
    uint32_t end = ts_node_end_byte(node);
    if (start >= source_code.length() || end > source_code.length() || start >= end) return ""; 
    return source_code.substr(start, end - start);
}

std::string ReferenceExtractor::determine_caller_fqn(TSNode node, const std::string& source_code) {
    std::string caller = "<global>"; // Default if called outside any function
    TSNode current = ts_node_parent(node);
    
    // Climb up the AST to find the function or method that encloses this call
    while (!ts_node_is_null(current)) {
        std::string type = ts_node_type(current);
        
        // Catch function and method definitions across multiple languages
        if (type == "function_definition" || type == "function_declaration" || 
            type == "method_definition" || type == "method_declaration" ||
            type == "function_item") {
            
            // Extract the name of the calling function
            TSNode name_node = ts_node_child_by_field_name(current, "name", 4);
            if (ts_node_is_null(name_node)) {
                name_node = ts_node_child_by_field_name(current, "declarator", 10); // C++ fallback
            }

            if (!ts_node_is_null(name_node)) {
                caller = extract_text(name_node, source_code);
                
                // Now, keep walking up to see if this function is inside a class
                std::string class_prefix = "";
                TSNode scope_parent = ts_node_parent(current);
                
                while (!ts_node_is_null(scope_parent)) {
                    std::string p_type = ts_node_type(scope_parent);
                    if (p_type == "class_definition" || p_type == "class_declaration" || 
                        p_type == "class_specifier" || p_type == "struct_item") {
                        
                        TSNode class_name_node = ts_node_child_by_field_name(scope_parent, "name", 4);
                        if (!ts_node_is_null(class_name_node)) {
                            class_prefix = extract_text(class_name_node, source_code) + ".";
                        }
                    }
                    scope_parent = ts_node_parent(scope_parent);
                }
                
                caller = class_prefix + caller;
                break; // We found the caller, stop climbing
            }
        }
        
        // NEW: Catch class-level references (e.g., inheritance superclass declarations).
        // This fires when a reference appears directly inside a class definition body
        // but NOT inside any method. The enclosing class IS the caller.
        if (type == "class_definition" || type == "class_declaration" ||
            type == "class_specifier" || type == "struct_item") {
            TSNode class_name_node = ts_node_child_by_field_name(current, "name", 4);
            if (!ts_node_is_null(class_name_node)) {
                caller = extract_text(class_name_node, source_code);
                break;
            }
        }

        current = ts_node_parent(current);
    }
    
    return caller;
}

std::vector<Reference> ReferenceExtractor::extract(TSNode root_node, TSQuery* query, const std::string& source_code) {
    std::vector<Reference> references;
    if (query == nullptr) return references;

    TSQueryCursor* cursor = ts_query_cursor_new();
    ts_query_cursor_exec(cursor, query, root_node);

    TSQueryMatch match;
    // Loop through every time our query matches a function call in the AST[cite: 10]
    while (ts_query_cursor_next_match(cursor, &match)) {
        for (uint16_t i = 0; i < match.capture_count; ++i) {
            TSNode capture_node = match.captures[i].node;
            
            Reference ref;
            // Extract the actual function name being called
            ref.callee_fqn = extract_text(capture_node, source_code);
            
            // CONTEXT AWARENESS: Figure out who is making the call
            ref.caller_fqn = determine_caller_fqn(capture_node, source_code);
            
            // Tree-sitter is 0-indexed, so we add 1 for standard human-readable line numbers
            ref.line_number = ts_node_start_point(capture_node).row + 1;
            
            // INHERITANCE DETECTION: Check if this reference is a class superclass declaration,
            // not a plain function call.
            // - C++: parent is `base_class_specifier` (inside `base_class_clause`)
            // - Python: parent is `argument_list` whose parent is `class_definition`
            TSNode capture_parent = ts_node_parent(capture_node);
            std::string parent_type = ts_node_is_null(capture_parent) ? "" : std::string(ts_node_type(capture_parent));
            TSNode grandparent = ts_node_parent(capture_parent);
            std::string gp_type = ts_node_is_null(grandparent) ? "" : std::string(ts_node_type(grandparent));

            if (parent_type == "base_class_clause" ||
                (parent_type == "argument_list" && gp_type == "class_definition")) {
                ref.kind = ReferenceKind::Inheritance;
            } else {
                ref.kind = ReferenceKind::Call;
            }
            
            references.push_back(ref);
        }
    }

    ts_query_cursor_delete(cursor);
    return references;
}