#pragma once
#include <string>

// Takes a file path and returns the language name (e.g., "Python", "JavaScript")
std::string detect_language(const std::string& filepath);