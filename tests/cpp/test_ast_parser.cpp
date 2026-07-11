#include <gtest/gtest.h>
#include <string>
#include <vector>
#include "ast_parser.hpp"

TEST(ASTParserTest, ParsesPythonSymbolsAndDependencies) {
    ASTParser parser;
    EXPECT_TRUE(parser.set_language("python"));

    std::string python_code = 
        "import os\n"
        "from json import loads\n"
        "\n"
        "class DatabaseConnection:\n"
        "    def connect(self):\n"
        "        pass\n"
        "\n"
        "def helper():\n"
        "    pass\n";

    // Extract symbols
    auto symbols = parser.extract_symbols(python_code);
    ASSERT_EQ(symbols.size(), 3);
    EXPECT_EQ(symbols[0].name, "DatabaseConnection");
    EXPECT_EQ(symbols[0].type, "class");
    EXPECT_EQ(symbols[1].name, "connect");
    EXPECT_EQ(symbols[1].type, "function");
    EXPECT_EQ(symbols[2].name, "helper");
    EXPECT_EQ(symbols[2].type, "function");

    // Extract dependencies
    // Note: The current query only captures @module_name, not @imported_name
    auto deps = parser.extract_dependencies(python_code);
    ASSERT_EQ(deps.size(), 2);
    EXPECT_EQ(deps[0].module_name, "os");
    EXPECT_EQ(deps[1].module_name, "json");
}

TEST(ASTParserTest, RejectsInvalidLanguages) {
    ASTParser parser;
    EXPECT_FALSE(parser.set_language("cobol"));
    EXPECT_FALSE(parser.set_language("invalid_lang_xyz"));
}
