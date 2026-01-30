#!/usr/bin/env bash
# Stub shell script for a task hook.
# Place in $root/.tasks/task-{name}/[0-9]+[a-z].{desc}.bash
# then make it executable with chmod +x
# Return Codes:
# - 0 : success
# - 1 : failure
# - 2 | $PRINTED_HELP
set -o nounset
set -o pipefail

# shellcheck disable=SC1091
source "$POLY_SRC/lib/lib-util.bash"
# shellcheck disable=SC1091
[[ -e "$POLYGLOT_ROOT/.tasks/task-util.bash" ]] && source "$POLYGLOT_ROOT/.tasks/task-util.bash"

function main () {
    declare -a sphinx_args=()
    builder="$POLYGLOT_SPHINX_BUILDER"
    conf="$POLYGLOT_SPHINX_CONF_DIR"
    out="$POLYGLOT_TEMP/site"
    doctrees="$POLYGLOT_TEMP/doctrees"
    logs="$POLYGLOT_TEMP/logs"
    src="$POLYGLOT_SRC"

    fname=$(basename "${BASH_SOURCE[0]}")
    subhead "$fname." "Args: $*"

    # Parse args:
    while [[ $# -gt 0 ]]; do
        case $1 in
            --fresh)
                echo "- using a fresh environment for sphinx"
                sphinx_args+=("--fresh-env")
                ;;
            --all)
                echo "- writing all files"
                sphinx_args+=("--write-all")
                ;;
            --builder=*)
                IFS="=" read -ra KEYVAL <<< "$1"
                builder="${KEYVAL[1]}"
                ;;
            *) ;;
        esac
        shift
    done

    sphinx_args+=("--builder" "$builder")

    uv run sphinx-build "${sphinx_args[@]}" \
        --conf-dir "$conf" \
        --doctree-dir "$doctrees" \
        --warning-file "$logs/sphinx.log" \
        "$src" "$out"
}

main "$@"
