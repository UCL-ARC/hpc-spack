#!/bin/bash

# A script to run a command, form the command line, in the standard working environment for spack 
#
# This script is symlinked as spe 
#

if [[ "$1" == "-h"  || "$1" == "--help" ]]; then
    echo "Usage: sper <command>"
    echo "  - sets the standard environment for spack and then runs the command"
    exit
fi
# set the environment
THIS_SCRIPTS_DIR=$(dirname $0)
source "$THIS_SCRIPTS_DIR/spe"
# call the command from the command line
"$@"
