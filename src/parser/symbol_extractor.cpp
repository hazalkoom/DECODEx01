#include "symbol_extractor.hpp"

// Safely slices text out of the source code string via node byte offsets
static std::string extract_text(TSNode node, const std::string& source_code) {
    uint32_t start = ts_node_start_byte(node);
    uint32_t end = ts_node_end_byte(node);
    if (start >= source_code.length() || end > source_code.length() || start >= end) return ""; 
    return source_code.substr(start, end - start);
}

std::string SymbolExtractor::extract_docstring(TSNode node, const std::string& source_code) {
    // Walk backwards from the current node's sibling sequence to pull preceding comments
    TSNode prev = ts_node_prev_sibling(node);
    std::string doc = "";
    
    while (!ts_node_is_null(prev)) {
        std::string type = ts_node_type(prev);
        // Catch line/block comments or raw string expressions (Python docstrings)
        if (type == "comment" || type == "line_comment" || type == "block_comment" || type == "expression_statement") {
            std::string comment_text = extract_text(prev, source_code);
            doc = comment_text + "\n" + doc;
            prev = ts_node_prev_sibling(prev);
        } else {
            break; // Stop when we hit actual code structures
        }
    }
    return doc;
}

std::string SymbolExtractor::build_fully_qualified_name(TSNode node, const std::string& source_code) {
    std::string fqn = "";
    TSNode current = ts_node_parent(node);

    // Climb up the AST hierarchy to check for enclosing structural contexts (namespaces, classes)
    while (!ts_node_is_null(current)) {
        std::string type = ts_node_type(current);
        if (type == "class_definition" || type == "class_declaration" || type == "namespace_definition") {
            // Find the identifying child of the parent structure
            TSNode name_child = ts_node_child_by_field_name(current, "name", 4);
            if (!ts_node_is_null(name_child)) {
                std::string parent_name = extract_text(name_child, source_code);
                if (!parent_name.empty()) {
                    fqn = parent_name + "." + fqn;
                }
            }
        }
        current = ts_node_parent(current);
    }
    return fqn;
}

std::string SymbolExtractor::extract_signature(TSNode node, const std::string& source_code) {
    TSNode parent = ts_node_parent(node);
    if (ts_node_is_null(parent)) return "";

    // Search common children sub-nodes representing execution parameters
    TSNode params = ts_node_child_by_field_name(parent, "parameters", 10);
    if (ts_node_is_null(params)) {
        params = ts_node_child_by_field_name(parent, "declarator", 10); // Secondary fallback pattern for C++
    }

    if (!ts_node_is_null(params)) {
        return extract_text(node, source_code) + extract_text(params, source_code);
    }
    return extract_text(node, source_code) + "()";
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
            
            uint32_t length;
            const char* capture_name = ts_query_capture_name_for_id(query, capture_id, &length);
            std::string capture_str(capture_name, length);

            TSNode parent_node = ts_node_parent(name_node);
            if (ts_node_is_null(parent_node)) continue;

            Symbol sym;
            sym.name = extract_text(name_node, source_code);
            
            // Map string types securely to type-safe enums
            if (capture_str == "class_name") {
                sym.kind = SymbolKind::Class;
            } else {
                // If it lives inside a class tree path, assign it as a method
                std::string prefix = build_fully_qualified_name(name_node, source_code);
                sym.kind = prefix.empty() ? SymbolKind::Function : SymbolKind::Method;
            }

            // Extract context blocks
            std::string path_prefix = build_fully_qualified_name(name_node, source_code);
            sym.fully_qualified_name = path_prefix + sym.name;
            sym.signature = (sym.kind == SymbolKind::Class) ? sym.name : extract_signature(name_node, source_code);
            sym.docstring = extract_docstring(parent_node, source_code);
            sym.return_type = "auto"; // Default fallback typing deduction for single pass parsing phase
            
            sym.start_line = ts_node_start_point(parent_node).row + 1;
            sym.end_line = ts_node_end_point(parent_node).row + 1;
            
            symbols.push_back(sym);
        }
    }
    
    ts_query_cursor_delete(cursor);
    return symbols;
}