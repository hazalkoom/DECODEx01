#pragma once
#include <string>
#include <vector>
#include <cstdint>

// --- ENUMS FOR TYPE SAFETY & SPEED ---

enum class SymbolKind {
    Class,
    Function,
    Method,
    Interface,
    Variable,
    Unknown
};

enum class ReferenceKind {
    Call,          // function()
    Instantiation, // Database db;
    Inheritance,   // class Child : Parent
    Usage,         // value = x;
    Unknown
};

// --- CORE DATA STRUCTURES ---

// 1. The Entity: Deeply detailed definitions
struct Symbol {
    std::string name;                  // e.g., "connect"
    std::string fully_qualified_name;  // e.g., "myproject.database.Database.connect"
    std::string signature;             // e.g., "connect(DatabaseConfig config, int timeout)"
    std::string return_type;           // e.g., "User", "void", "bool"
    SymbolKind kind;                   // Enum: Faster and safer than strings
    std::string docstring;             // Extracted comments for AI token saving
    
    uint32_t start_line;
    uint32_t end_line;
};

// 2. The Import: File-level dependencies
struct Dependency {
    std::string module_name;     
    std::string imported_name;   
    uint32_t line_number;
};

// 3. The Deep Link: Context-aware relationships
struct Reference {
    std::string caller_fqn;      // Fully Qualified Name of the caller (Context-Aware)
    std::string callee_fqn;      // Fully Qualified Name of the target
    ReferenceKind kind;          // Enum: Call, Construct, Inherit, etc.
    uint32_t line_number;
};

// 4. The Master Record: Single-Pass Output Payload
struct FileContext {
    std::string filepath;
    std::string language;

    std::vector<Symbol> symbols;
    std::vector<Dependency> dependencies;
    std::vector<Reference> references;
};