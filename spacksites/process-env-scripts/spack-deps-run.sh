#!/bin/bash

# A script to run a command, from the command line, in the standard working environment for spack 
#
# This script is symlinked as spdr 
#

if [[ "$1" == "-h"  || "$1" == "--help" ]]; then
    echo "Usage: sper <command>"
    echo "  - sets the standard environment for running spack and then runs the command"
    echo "  - NOTE: This is about dependencies over which spack is run and is"
    echo "    disctinct from teh spack-env.sh script which puts a spack site into the"
    echo "    user's environment."
    exit
fi
# set the environment
THIS_SCRIPTS_DIR=$(dirname $0)
source "$THIS_SCRIPTS_DIR/spd"
# call the command from the command line
echo "# SPACKSITES: Have set spacks's external compiler and python dependencies - now calling $@" >&2
$@
