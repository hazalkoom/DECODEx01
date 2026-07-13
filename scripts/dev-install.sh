#!/bin/bash
# Fast development install — uses persistent build cache.
# First-time: ~40s (clones repos + full compile)
# Subsequent: ~2-5s (incremental compile only)

set -e
cd "$(dirname "$0")/.."
# Temporary workaround: pip/scikit-build-core doesn't support Poetry's "||" operator in requires-python.
# We temporarily change the specifier to a PEP 440 compliant version, build/install, and restore it.
original_toml=$(cat pyproject.toml)
cleanup() {
    echo "Restoring pyproject.toml..."
    echo "$original_toml" > pyproject.toml
}
trap cleanup EXIT

sed -i 's/requires-python = ">=3.11,<3.14.1 || >3.14.1"/requires-python = ">=3.11"/' pyproject.toml

poetry run pip install --no-build-isolation -e . -v
echo ""
echo "✅ Build complete! Run tests with: poetry run pytest tests/ -s -v"
