#!/bin/bash
THIS_SCRIPTS_DIR=$(dirname $0)
"$THIS_SCRIPTS_DIR/spdr" "$THIS_SCRIPTS_DIR/create_spack_site.py" $@
