#include <gtest/gtest.h>
#include <fstream>
#include <string>
#include <cstdio>
#include "language_detector.hpp"

TEST(LanguageDetectorTest, DetectsByExtension) {
    // 1. Setup temp files
    std::string py_path = "test_temp_file.py";
    std::string cpp_path = "test_temp_file.cpp";
    std::string js_path = "test_temp_file.js";
    
    std::ofstream(py_path) << "print('hello')";
    std::ofstream(cpp_path) << "int main() {}";
    std::ofstream(js_path) << "console.log()";

    // 2. Validate
    EXPECT_EQ(detect_language(py_path), "Python");
    EXPECT_EQ(detect_language(cpp_path), "C++");
    EXPECT_EQ(detect_language(js_path), "JavaScript");

    // 3. Cleanup
    std::remove(py_path.c_str());
    std::remove(cpp_path.c_str());
    std::remove(js_path.c_str());
}

TEST(LanguageDetectorTest, DetectsByShebang) {
    std::string shebang_path = "test_temp_shebang";
    
    std::ofstream(shebang_path) << "#!/usr/bin/env python3\nprint('hello')";
    EXPECT_EQ(detect_language(shebang_path), "Python");
    
    std::ofstream(shebang_path, std::ios::trunc) << "#!/bin/bash\necho 123";
    EXPECT_EQ(detect_language(shebang_path), "Shell");

    std::remove(shebang_path.c_str());
}

TEST(LanguageDetectorTest, HandlesDirectoriesGracefully) {
    // Current directory "." should be Unknown/invalid language
    EXPECT_EQ(detect_language("."), "Unknown");
}
