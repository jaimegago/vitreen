#!/usr/bin/env bash
set -x
set -e


TESTS_DIR="${1:-TESTS_DIR}"
REPORTS="${2:-REPORTS}"
mkdir -p ${REPORTS}
pip install pytest
python -m pytest "${TESTS_DIR}" --junitxml="${REPORTS}"/report.xml

