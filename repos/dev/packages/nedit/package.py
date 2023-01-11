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
#     spack install nedit
#
# You can edit this file again by typing:
#
#     spack edit nedit
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
# that includes spack/spack/lib/spack/llnl/util/filesystem.py, which provides functions like workingdir, mkdirp, install
# import also provides definitions of version(), depends_on()

import os, subprocess

class Nedit(MakefilePackage):
    """Nedit - an XWindows GUI editor"""

    # Add a proper url for your package's homepage here.
    homepage = "https://sourceforge.net/projects/nedit/"
    url = "https://sourceforge.net/projects/nedit/files/nedit-source/nedit-5.7-src.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("5.7", sha256="add9ac79ff973528ad36c86858238bac4f59896c27dbf285cbe6a4d425fca17a")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on('motif', type='build')
    # FIXME: any runtime dependencies for Xwindows?

    # def edit(self, spec, prefix):
    #     # FIXME: Edit the Makefile if necessary
    #     # FIXME: If not needed delete this function
    #     # makefile = FileFilter("Makefile")
    #     # makefile.filter("CC = .*", "CC = cc")
    #     pass

    # this property serves only the fisrt of the two makes in build()
    @property
    def build_targets(self):
        return ['linux'] 

    def build(self, spec, prefix):
        """Run "make" on the build targets specified by the builder."""
        # parent code being overriden is:
        # with fs.working_dir(self.build_directory):
        #     inspect.getmodule(self.pkg).make(*self.build_targets)

        # the main build, of the executables, so the same as the code being overridden
        with working_dir(self.build_directory):
            #inspect.getmodule(self.pkg).make(*self.build_targets) 
            make(*self.build_targets)  # FIXME: where is make() defined
        
        # the build of the man files
        with working_dir(os.path.join(self.build_directory, 'doc')):
            #inspect.getmodule(self.pkg).make('man')
            make('man')

    def install(self, spec, prefix):
        """Run "make" on the install targets specified by the builder."""
        # parent code being overriden is:
        # with fs.working_dir(self.build_directory):
        #    inspect.getmodule(self.pkg).make(*self.install_targets)

        # create directories
        # FIXME: decide on file mode for these dirs and use mode=0oXXX to set them
        mkdirp(prefix.bin)
        mkdirp(prefix.share.man.man1)

        # main install of the executable files:
        with working_dir(os.path.join(self.build_directory, 'source')):
            #    cp nedit $INSTALL_PREFIX/bin/
            #    cp nc $INSTALL_PREFIX/bin/ncl
            install('nedit', prefix.bin)
            install('nc', os.path.join(prefix.bin, 'ncl'))

        #  install the docs:
        with working_dir(os.path.join(self.build_directory, 'doc')):
            #    cp nedit.man $mandir/nedit.1
            install('nedit.man', os.path.join(prefix.share.man.man1, 'nedit.1'))
            #    sed -e '/Title /s/NC/NCL/;/^.TH/s/NC/NCL/;/^nc /s//ncl /;/\\fBnc\\fR/s//\\fBncl\\fR/' nc.man > ncl.man
            #    cp ncl.man $mandir/ncl.1
            with open('ncl.man', 'w') as modified_file:
                subprocess.run(['sed', '-e', r'/Title /s/NC/NCL/;/^.TH/s/NC/NCL/;/^nc /s//ncl /;/\\fBnc\\fR/s//\\fBncl\\fR/', 'nc.man'], stdout=modified_file)  # FIXME: any incorrect string esaping? check subprocess ourput. run() will not use shell expansion
            install('ncl.man', os.path.join(prefix.share.man.man1, 'ncl.1'))  
            
            


# RCPS script:

#!/usr/bin/env bash

###############################################
# Installing NEdit from GIT repository
#
# by Brian Alston, 2015 
#
# Using Ian's require function to load modules
#
# Will need modules: default-modules

# VERSION=${VERSION:-5.6-Aug15}
# INSTALL_PREFIX=${INSTALL_PREFIX:-/shared/ucl/apps/NEdit/${VERSION}}
# SRC_ARCHIVE=${SRC_ARCHIVE:- git://git.code.sf.net/p/nedit/git}

# export PATH=$INSTALL_PREFIX/bin:$PATH

# dirname=$(dirname $0 2>/dev/null || pwd)
# INCLUDES_DIR=${INCLUDES_DIR:-${dirname}/includes}
# source ${INCLUDES_DIR}/module_maker_inc.sh
# source ${INCLUDES_DIR}/require_inc.sh

# require rcps-core

# temp_dir=`mktemp -d -p /dev/shm`

# cd $temp_dir

# git clone $SRC_ARCHIVE nedit-git

# if [[ "$?" == "0" ]]
# then
#    cd nedit-git
#    make linux 2>&1 | tee make-linux-log
#    cd source
#    mkdir -p $INSTALL_PREFIX/bin
#    cp nedit $INSTALL_PREFIX/bin/
#    cp nc $INSTALL_PREFIX/bin/ncl
#    cd ../doc
#    make man
#    mandir=$INSTALL_PREFIX/share/man/man1
#    mkdir -p $mandir
#    cp nedit.man $mandir/nedit.1
#    sed -e '/Title /s/NC/NCL/;/^.TH/s/NC/NCL/;/^nc /s//ncl /;/\\fBnc\\fR/s//\\fBncl\\fR/' nc.man > ncl.man
#    cp ncl.man $mandir/ncl.1

# else
#    echo ""
#    echo "***** git clone failed."
# fi

