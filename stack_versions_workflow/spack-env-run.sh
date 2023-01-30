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
source spe
"$@"
