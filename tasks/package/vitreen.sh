#!/usr/bin/env bash
VITREEN_ROOT_DEFAULT=/opt/vitreen
[ -f run.py ] && VITREEN_ROOT_DEFAULT=.
VITREEN_ROOT="${VITREEN_ROOT:-$VITREEN_ROOT_DEFAULT}"
VITREEN_BIN="$VITREEN_ROOT/env/bin"
source "$VITREEN_BIN/activate"
"$VITREEN_BIN/python" "$VITREEN_ROOT/run.py" $@
rc="$?"
deactivate
exit "$rc"