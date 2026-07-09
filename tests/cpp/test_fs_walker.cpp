#include <gtest/gtest.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <filesystem>
#include "fs_walker.hpp"

namespace fs = std::filesystem;

TEST(FsWalkerTest, WalksDirectoryAndIgnoresCorrectly) {
    // 1. Setup nested structures
    std::string base_dir = "test_walker_sandbox";
    fs::create_directories(base_dir + "/src");
    fs::create_directories(base_dir + "/node_modules");
    fs::create_directories(base_dir + "/.git");

    std::string file_py = base_dir + "/src/main.py";
    std::string file_js = base_dir + "/node_modules/lib.js";
    std::string file_git = base_dir + "/.git/config";
    std::string file_root = base_dir + "/README.md";

    std::ofstream(file_py) << "print('hello')";
    std::ofstream(file_js) << "console.log('js')";
    std::ofstream(file_git) << "secret";
    std::ofstream(file_root) << "# README";

    // 2. Walk
    std::vector<std::string> results = walk_repository(base_dir);

    // 3. Validate
    // Check that we found python and readme
    bool found_py = false;
    bool found_root = false;
    bool found_ignored = false;

    for (const auto& path : results) {
        if (path.find("main.py") != std::string::npos) found_py = true;
        if (path.find("README.md") != std::string::npos) found_root = true;
        if (path.find("node_modules") != std::string::npos || path.find(".git") != std::string::npos) {
            found_ignored = true;
        }
    }

    EXPECT_TRUE(found_py);
    EXPECT_TRUE(found_root);
    EXPECT_FALSE(found_ignored);

    // 4. Cleanup
    fs::remove_all(base_dir);
}
