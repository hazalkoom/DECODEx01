#!/bin/bash
# =============================================================================
# DECODE Code Coverage Report Generator
# =============================================================================
# Generates coverage reports for both C++ (via gcov/lcov) and Python (via pytest-cov).
#
# C++ coverage: Builds codelens_lib and cpp_tests with --coverage flags,
#               runs the tests, and generates HTML via lcov + genhtml.
# Python coverage: Runs pytest with --cov and generates an HTML report.
#
# Reports are written to:
#   coverage_reports/cpp/html/index.html
#   coverage_reports/python/html/index.html
#
# Usage: ./run_coverage.sh
# =============================================================================
set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="$PROJECT_DIR/build/coverage"
REPORT_DIR="$PROJECT_DIR/coverage_reports"

echo "============================================="
echo "  DECODE Code Coverage Report Generator"
echo "============================================="
echo ""

# 1. Check for lcov
if ! command -v lcov &> /dev/null; then
    echo "⚠  lcov not found. Installing via dnf..."
    sudo dnf install -y lcov
fi

if ! command -v genhtml &> /dev/null; then
    echo "⚠  genhtml not found. Installing via dnf..."
    sudo dnf install -y lcov
fi

# 2. Configure and build with coverage flags
echo "--- [1/6] Configuring CMake with --coverage flags ---"
cmake -S "$PROJECT_DIR" -B "$BUILD_DIR" \
    -DENABLE_COVERAGE=ON \
    -DBUILD_TESTING=ON \
    -DBUILD_PYTHON_MODULE=OFF \
    -DENABLE_SANITIZERS=OFF \
    -G Ninja 2>&1 | tail -5

echo ""
echo "--- [2/6] Building cpp_tests with coverage instrumentation ---"
cmake --build "$BUILD_DIR" --target cpp_tests -j$(nproc)

# 3. Reset counters and run C++ tests
echo ""
echo "--- [3/6] Resetting lcov counters ---"
lcov --zerocounters --directory "$BUILD_DIR" 2>/dev/null || true

echo ""
echo "--- [4/6] Running C++ tests ---"
"$BUILD_DIR/cpp_tests"

# 4. Capture C++ coverage using gcovr
echo ""
echo "--- [5/6] Capturing C++ coverage data with gcovr ---"
mkdir -p "$REPORT_DIR/cpp/html"

# Run gcovr to generate HTML report
poetry run gcovr \
    --root "$PROJECT_DIR" \
    --filter "$PROJECT_DIR/src/" \
    --html-details "$REPORT_DIR/cpp/html/index.html" \
    --print-summary

echo "✅ C++ coverage report: $REPORT_DIR/cpp/html/index.html"

# 5. Run Python tests
echo ""
echo "--- [6/6] Running Python test suite ---"
# Note: pytest-cov is omitted because Python's coverage module cannot trace
# inside C++ compiled extensions (.so files). The C++ gcov coverage above
# is what actually measures our engine's test coverage.
poetry run pytest tests/ --benchmark-disable -q 2>&1

echo ""
echo "============================================="
echo "  ✅ Coverage run complete!"
echo ""
echo "  C++ report: $REPORT_DIR/cpp/html/index.html"
echo "============================================="
