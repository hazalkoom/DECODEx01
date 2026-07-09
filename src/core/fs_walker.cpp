#include "fs_walker.hpp"
#include <filesystem>
#include <unordered_set>

namespace fs = std::filesystem;

// A high-performance hash set of directories to ignore.
// Looking up a name in here is instant, no matter how big the list gets.
const std::unordered_set<std::string> IGNORED_DIRS = {
    // Version Control & OS
    ".git", ".svn", ".hg", ".DS_Store", "__MACOSX",
    
    // Python
    ".venv", "venv", "env", ".env", "__pycache__", ".pytest_cache", ".tox", "dist", "build", "eggs",
    
    // Node.js / Frontend
    "node_modules", ".next", ".nuxt", "coverage", "dist", "build", "out",
    
    // Java / Kotlin / Scala
    "target", ".gradle", "build", ".m2",
    
    // C / C++ / C#
    "bin", "obj", ".vs", "out", "build",
    
    // Rust & Go
    "target", "vendor"
};

bool should_skip(const std::string& dir_name) {
    // 1. Skip anything that starts with a dot (hidden folders like .idea, .vscode)
    if (!dir_name.empty() && dir_name[0] == '.') {
        return true;
    }
    
    // 2. Check if the exact folder name exists in our high-speed hash set
    return IGNORED_DIRS.find(dir_name) != IGNORED_DIRS.end();
}

std::vector<std::string> walk_repository(const std::string& root_path) {
    std::vector<std::string> discovered_files;

    auto options = fs::directory_options::skip_permission_denied;

    try {

        for (auto it = fs::recursive_directory_iterator(root_path, options); it != fs::recursive_directory_iterator(); ++it) {
            const auto& entry = *it;
            std::string filename = entry.path().filename().string();

            if (entry.is_directory() && should_skip(filename)) {
                it.disable_recursion_pending(); 
                continue;
            }

            if (entry.is_regular_file()) {
                discovered_files.push_back(entry.path().string());
            }
        }
    } catch (const fs::filesystem_error& e) {
        // This will now only catch catastrophic disk errors, not standard permission walls
    }

    return discovered_files;
}