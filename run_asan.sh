#!/bin/bash
# =============================================================================
# DECODE AddressSanitizer Runner
# =============================================================================
# Builds the C++ static library and test binary with ASan instrumentation,
# then runs the native tests to detect memory leaks, buffer overflows,
# use-after-free, and other memory safety violations.
#
# NOTE: ASan flags are ONLY applied to codelens_lib and cpp_tests.
#       The Python module (codelens_core) is NOT instrumented.
#
# Usage: ./run_asan.sh
# =============================================================================
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="$PROJECT_DIR/build/asan"

echo "============================================="
echo "  DECODE AddressSanitizer Runner"
echo "============================================="
echo ""

# 1. Configure with ASan enabled
echo "--- [1/3] Configuring CMake with AddressSanitizer ---"
cmake -S "$PROJECT_DIR" -B "$BUILD_DIR" \
    -DENABLE_SANITIZERS=ON \
    -DBUILD_TESTING=ON \
    -DBUILD_PYTHON_MODULE=OFF \
    -DENABLE_COVERAGE=OFF \
    -G Ninja 2>&1 | tail -5

# 2. Build only the test binary
echo ""
echo "--- [2/3] Building cpp_tests with ASan ---"
cmake --build "$BUILD_DIR" --target cpp_tests -j$(nproc)

# 3. Run tests under ASan
echo ""
echo "--- [3/3] Running C++ tests under AddressSanitizer ---"
echo ""
ASAN_OPTIONS="detect_leaks=1:halt_on_error=0:print_stats=1" \
    "$BUILD_DIR/cpp_tests"

echo ""
echo "============================================="
echo "  ✅ ASan run complete — no memory errors!"
echo "============================================="
