#include "language_detector.hpp"
#include <filesystem>
#include <fstream>
#include <unordered_map>
#include <string_view>

namespace fs = std::filesystem;

const std::unordered_map<std::string, std::string> EXTENSION_MAP = {
    {".py", "Python"}, {".js", "JavaScript"}, {".ts", "TypeScript"},
    {".java", "Java"}, {".cpp", "C++"}, {".hpp", "C++"}, {".c", "C"}, {".h", "C"},
    {".go", "Go"}, {".rs", "Rust"}, {".cs", "C#"}, {".rb", "Ruby"}, {".php", "PHP"},
    {".swift", "Swift"}, {".kt", "Kotlin"}, {".sh", "Shell"}, {".bash", "Shell"},
    {".zsh", "Shell"}, {".pl", "Perl"}, {".lua", "Lua"}, {".r", "R"},
    {".json", "JSON"}, {".yaml", "YAML"}, {".yml", "YAML"}, {".xml", "XML"},
    {".html", "HTML"}, {".htm", "HTML"}, {".css", "CSS"}, {".md", "Markdown"},
    {".csv", "CSV"}, {".sql", "SQL"}, {".txt", "Plain Text"},
    {".pdf", "PDF Document"}, {".doc", "Microsoft Word"}, {".docx", "Microsoft Word"},
    {".xls", "Microsoft Excel"}, {".xlsx", "Microsoft Excel"},
    {".ppt", "Microsoft PowerPoint"}, {".pptx", "Microsoft PowerPoint"}
};

const std::unordered_map<std::string, std::string> EXECUTOR_MAP = {
    {"python", "Python"}, {"python2", "Python"}, {"python3", "Python"},
    {"node", "JavaScript"}, {"deno", "TypeScript"}, {"bun", "JavaScript"},
    {"bash", "Shell"}, {"sh", "Shell"}, {"zsh", "Shell"}, {"dash", "Shell"},
    {"ruby", "Ruby"}, {"perl", "Perl"}, {"php", "PHP"}
};

// Helper function to trim whitespace from both ends of a string_view
std::string_view trim_whitespace(std::string_view sv) {
    size_t start = sv.find_first_not_of(" \t\r\n");
    if (start == std::string_view::npos) return ""; // All whitespace
    size_t end = sv.find_last_not_of(" \t\r\n");
    return sv.substr(start, end - start + 1);
}

std::string detect_language(const std::string& filepath) {
    fs::path path(filepath);

    // QA FIX 1: Ensure it is a regular file before we do ANYTHING.
    // This stops directories named "folder.js" from being identified as code.
    if (!fs::is_regular_file(path)) {
        return "Unknown";
    }

    if (path.has_extension()) {
        std::string ext = path.extension().string();
        for (auto& c : ext) c = std::tolower(c);
        
        auto it = EXTENSION_MAP.find(ext);
        if (it != EXTENSION_MAP.end()) {
            return it->second;
        }
    }

    // Magic Bytes & Shebangs
    std::ifstream file(filepath, std::ios::binary);
    if (file.is_open()) {
        char buffer[256] = {0};
        file.read(buffer, 255);
        std::streamsize bytes_read = file.gcount();
        
        if (bytes_read > 0) {
            std::string_view content(buffer, bytes_read);

            if (content.starts_with("%PDF-")) return "PDF Document";
            if (content.starts_with("\x7F" "ELF")) return "Binary (ELF)";
            if (content.starts_with("MZ")) return "Binary (Windows)";
            if (content.starts_with("PK\x03\x04")) return "ZIP/Office Archive";

            if (content.starts_with("#!")) {
                size_t newline_pos = content.find('\n');
                if (newline_pos != std::string_view::npos) {
                    std::string_view shebang = content.substr(2, newline_pos - 2);
                    
                    size_t env_pos = shebang.find("env");
                    if (env_pos != std::string_view::npos) {
                        // Move past "env"
                        shebang = shebang.substr(env_pos + 3);
                    }
                    
                    size_t last_slash = shebang.find_last_of('/');
                    if (last_slash != std::string_view::npos) {
                        shebang = shebang.substr(last_slash + 1);
                    }

                    // QA FIX 2: Aggressively trim all spaces, tabs, and carriage returns
                    shebang = trim_whitespace(shebang);

                    auto it = EXECUTOR_MAP.find(std::string(shebang));
                    if (it != EXECUTOR_MAP.end()) {
                        return it->second;
                    }
                }
            }
        }
    }

    return "Unknown";
}