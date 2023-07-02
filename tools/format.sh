#!/bin/bash

set -euo pipefail

# http://redsymbol.net/articles/unofficial-bash-strict-mode/
# -e
# The set -e option instructs bash to immediately exit if any command [1] has a non-zero exit status.
# -u
# Treat unset variables and parameters other than the special parameters "@" and "*" as an error
# when performing parameter expansion. If expansion is attempted on an unset variable or parameter,
# the shell prints an error message, and, if not interactive, exits with a non-zero status.
# set -o pipefail
# This setting prevents errors in a pipeline from being masked. If any command in a pipeline fails,
# that return code will be used as the return code of the whole pipeline.

# -------
# Colours 

end="\033[0m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"

function red { 
    echo -e "${red}${1}${end}"
}
function green { 
    echo -e "${green}${1}${end}"
}
function yellow {
    echo -e "${yellow}${1}${end}"
}
function blue {
    echo -e "${blue}${1}${end}"
} 
function purple {
    echo -e "${purple}${1}${end}"
}

# ---------
# Variables

if ! command -v git &> /dev/null
then
    blue "🚧 Git not found using current directory as repo root ..."
    TOTO_REPO_ROOT=${PWD}
else
    TOTO_REPO_ROOT=$(git rev-parse --show-toplevel)
fi


# ----
# Main

blue "🔨 Code Formating ..."
black ${TOTO_REPO_ROOT}/toto
isort ${TOTO_REPO_ROOT}/toto
purple "💫 Code Formating done."
