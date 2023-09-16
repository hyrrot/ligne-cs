#!/bin/bash -ex
set -o pipefail

POETRY_RUN_PYTHON="poetry run python"
BUILD_SH_ABSOLUTE_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SRC_DIR="${BUILD_SH_ABSOLUTE_PATH}/src"
BUILD_DIR="${BUILD_SH_ABSOLUTE_PATH}/build"

rm -r $(dirname $0)/build || true

# Build diagrams
mkdir -p ${BUILD_DIR}/diagrams
cd ${BUILD_DIR}/diagrams

SRC_DIAGRAMS_DIR="${SRC_DIR}/diagrams"

${POETRY_RUN_PYTHON} ${SRC_DIAGRAMS_DIR}/system_diagram.py

# Copy markdown files
mkdir -p ${BUILD_DIR}/md
cd ${BUILD_DIR}/md
cp -r ${SRC_DIR}/md/* .