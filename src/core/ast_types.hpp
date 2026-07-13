#pragma once
#include <string>

// 1. The Entity (What we already built)
// This holds the functions and classes we find in a file.
struct Symbol {
    std::string name;
    std::string type;
    uint32_t start_line;
    uint32_t end_line;
};

// 2. The Relationship (What we are building now for Path A)
// This holds the 'import' and 'include' statements we find in a file.
struct Dependency {
    std::string module_name;   // The library being imported (e.g., "os" or "json")
    std::string imported_name; // The specific function imported (e.g., "loads"). Can be empty!
    uint32_t line_number;      // The line where the import happened
};

struct Reference {
    std::string callee_name; // The function or class being called (e.g., "walk_repository")
    uint32_t line_number;    // Where the call happens
    
    // Note: To make this a true Call Graph, we will eventually want to calculate the 'caller_name'
    // (the function making the call) by walking *up* the AST tree from this node.
};