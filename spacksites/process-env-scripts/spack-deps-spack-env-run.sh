#!/bin/bash

# A script to run a command, from the command line, in the standard working environment for spack 
# so with the intention that command will be a spack command
#
# This script is symlinked as spdsper
#

if [[ "$1" == "-h"  || "$1" == "--help" ]]; then
    echo "Usage: sper <path to spack's setup-env.sh> <command>"
    echo "  - sets the standard environment for running spack and then runs the command"
    each "  - AND sets up spack by sourcing <path to spack's setup-env.sh>"
    exit
fi
# set the environment that spack should use, e.g. python and compiler versions 
# the file spd is a symlink to a script for the particular os in use
THIS_SCRIPTS_DIR=$(dirname $0)
source "$THIS_SCRIPTS_DIR/spd"

# set up spack in the current environment
export SPACK_DISABLE_LOCAL_CONFIG=1
echo "# SPACKSITES: have set SPACK_DISABLE_LOCAL_CONFIG=$SPACK_DISABLE_LOCAL_CONFIG"
export HPC_SPACK_ROOT=$(dirname $(dirname $(dirname $(realpath ${BASH_SOURCE:-$0}))))
echo "# SPACKSITES: have set HPC_SPACK_ROOT=$HPC_SPACK_ROOT"
source $1

# call the command from rest of the command line
shift 
echo "# SPACKSITES: Have set spacks's external compiler and python dependencies - now calling $@" >&2

$@
