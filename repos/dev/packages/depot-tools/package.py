# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install depot-tools
#
# You can edit this file again by typing:
#
#     spack edit depot-tools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *

import os, shutil

class DepotTools(Package):
    """Depot Tools - tool for working with Chromium development"""

    # Add a proper url for your package's homepage here.
    homepage = "https://chromium.googlesource.com/chromium/tools/depot_tools"
    git = "https://chromium.googlesource.com/chromium/tools/depot_tools.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    # FIXME: Add proper versions and checksums here.
    version("4147", branch='chrome/4147')
    

    # FIXME: Add dependencies if required.
    # FIXME: https://chromium.googlesource.com/chromium/tools/depot_tools says python 3.8 required 
    # (but https://chromium.googlesource.com/chromium/tools/depot_tools/+/refs/heads/chrome/4147/README.md does not mention python3) 
    # depends_on("foo")
    depends_on('python@3.8', type='run')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        #make()
        #make("install")
        # FIXME: Hmmm: rcps script seems to put all tools in a directory 'depot_tools' inside the prefix dir ???? is prefixing coammands with depot_tools/<command> standard usage for this package?
        shutil.copytree('.', prefix, dirs_exist_ok=True)  # requries python3.8

    # run env will need: DEPOT_TOOLS_UPDATE=0, i.e. to stops install updating itself, which will fail with user permissions    
    def setup_run_environment(self, env):
        env.set('DEPOT_TOOLS_UPDATE', '0') 

# rcps build script model is:

#!/usr/bin/env bash

###############################################
# Installing depot_tools from git
#
# by Owain Kenway, 2017 
#

# APPNAME=${APPNAME:-depot_tools}
# SRC_ARCHIVE=${SRC_ARCHIVE:-https://chromium.googlesource.com/chromium/tools/depot_tools.git}

# set -e

# mkdir -p /dev/shm/$APPNAME
# temp_dir=`mktemp -d -p /dev/shm/$APPNAME`

# cd $temp_dir

# git clone $SRC_ARCHIVE
# cd depot_tools

# VERSION=${VERSION:-`git rev-parse --short HEAD`}
# INSTALL_PREFIX=${INSTALL_PREFIX:-/shared/ucl/apps/$APPNAME/$VERSION}
# git checkout $VERSION
# mkdir -p ${INSTALL_PREFIX}/depot_tools

# cp -R * $INSTALL_PREFIX/depot_tools

# echo "Completed install of depot_tools version ${VERSION}"

