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
#     spack install chicken
#
# You can edit this file again by typing:
#
#     spack edit chicken
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Chicken(MakefilePackage):
    """A Scheme compiler that translates Scheme source files into C"""

    homepage = "https://http://wiki.call-cc.org/"
    url = "https://code.call-cc.org/releases/5.3.0/chicken-5.3.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("5.3.0", sha256="c3ad99d8f9e17ed810912ef981ac3b0c2e2f46fb0ecc033b5c3b6dca1bdb0d76")
    
    parallel = False 

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass

# build instructions are at https://code.call-cc.org/cgi-bin/gitweb.cgi?p=chicken-core.git;a=blob;f=README;h=1f2302753f827e5893ada45cb9ff0f2d1991f7c1;hb=e31bbee51ae2b892d624ad2736c624111c15ca9c
# this is indeed just a make - GNU make is specified by README
# so gmake is a build dependency
# make and make install requires setting of variables 
# (which appear after make so are parsed by make, so not environment vars):
# PLATFORM=linux PREFIX=${INSTALL_PREFIX}
# "Note that parallel builds (using the "-j" make(1) option) are *not* supported."
# So how to fix that?
# https://spack.readthedocs.io/en/latest/packaging_guide.html#package-level-build-parallelism indicates set parallel = False at the class level
# and that fixed it - i.e. apparently builds
# TODO any tests?
# TODO declare dependencies

# the two properties below implement the build instruction of  make PLATFORM=<platform> PREFIX=<destination>

    @property
    def build_targets(self):
        return ['PLATFORM=linux', 'PREFIX={0}'.format(self.prefix)]

    @property
    def install_targets(self):
        return ['PLATFORM=linux', 'PREFIX={0}'.format(self.prefix), 'install']