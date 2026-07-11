#!/bin/bash
# Fast development install — uses persistent build cache.
# First-time: ~40s (clones repos + full compile)
# Subsequent: ~2-5s (incremental compile only)

set -e
cd "$(dirname "$0")/.."
poetry run pip install --no-build-isolation -e . -v
echo ""
echo "✅ Build complete! Run tests with: poetry run pytest tests/ -s -v"
