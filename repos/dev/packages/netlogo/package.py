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
#     spack install netlogo
#
# You can edit this file again by typing:
#
#     spack edit netlogo
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *

import shutil, os

class Netlogo(Package):
    """A multi-agent programmable modeling environment"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://ccl.northwestern.edu/netlogo/"
    url = "https://ccl.northwestern.edu/netlogo/6.3.0/NetLogo-6.3.0-64.tgz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("6.3.0-64", sha256="baeec4d3d5d7548d13d48574c4c1dd9909d99b2a41ad60a765dce966138dd77a")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    
    # model rcps script has:
    # require gcc-libs/4.9.2
    # FIXME: what would be the equivalent in spack? for gcc 12  

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        # make()
        # make("install")
        # FIXME: check that copytree copes with filenames with spaces (cf rcps model script)
        shutil.copytree('.', prefix, dirs_exist_ok=True)
        
        # next the model script drops the excutables. Reason not stated, 
        # but may be because those are the ones with a gui
        # 
        for file in ['Behaviorsearch', 'HubNetClient', 'libpackager.so', 'NetLogo', 'NetLogo3D', 'NetLogoLogging']:
            os.remove(file)
        shutil.rmtree('runtime')
        
        # model recps script now does:
        # cp netlogo-headless.sh netlogo.sh
        # ln -s netlogo.sh NetLogo
        # so:
        shutil.copy2('netlogo-headless.sh ', 'netlogo.sh')
        os.symlink('netlogo.sh', 'NetLogo')

        # finally model rcps script does 
        # sed -i.bak 's|org.nlogo.headless.Main|-jar ${BASE_DIR}/app/netlogo-6.1.0.jar|g' netlogo.sh
        # sed -i.bak 's|-Dfile.encoding=UTF-8|-Dfile.encoding=UTF-8 -Dnetlogo.models.dir=${BASE_DIR}/app/models|g' netlogo-headless.sh
        # sed -i.bak 's|-Dfile.encoding=UTF-8|-Dfile.encoding=UTF-8 -Dnetlogo.models.dir=${BASE_DIR}/app/models|g' netlogo.sh
        # FIXME: convert those to python - there are models in recent packages added to this repo (repos/dev/)

        # rm *.bak  <-- the ones created by the lines just above???

# rcps build script model is:
# #!/usr/bin/env bash

# ###############################################
# # Installing 
# #
# # by Owain Kenway, 2019
# #
# set -e

# for i in ${includes_dir:=$(dirname $0 2>/dev/null)/includes}/{module_maker,require}_inc.sh; do . $i; done

# require gcc-libs/4.9.2

# NAME=${NAME:-NetLogo}
# VERSION=${VERSION:-6.1.0}
# INSTALL_PREFIX=${INSTALL_PREFIX:-/shared/ucl/apps/$NAME/$VERSION/}
# MD5=${MD5:-1f69450af8d25aa3e833a37d144df73b}

# SRC_ARCHIVE=${SRC_ARCHIVE:-https://ccl.northwestern.edu/netlogo/${VERSION}/NetLogo-${VERSION}-64.tgz}


# rm -rf ${INSTALL_PREFIX} # Clear old installs
# mkdir -p ${INSTALL_PREFIX}

# cd ${INSTALL_PREFIX}

# wget $SRC_ARCHIVE
# archive=$(basename "${SRC_ARCHIVE}")

# md5sum -c <<< "$MD5 $archive"

# tar -xvf $archive

# mv "${NAME} ${VERSION}" tmp # Spaces in filenames :(
# mv tmp/* .
# rm -rf tmp

# # We need to remove all binaries.
# rm -f Behaviorsearch HubNetClient libpackager.so NetLogo NetLogo3D NetLogoLogging
# rm -rf runtime

# # Create scripts to launch netlogo from the headless one as a model.
# cp netlogo-headless.sh netlogo.sh
# ln -s netlogo.sh NetLogo
# sed -i.bak 's|org.nlogo.headless.Main|-jar ${BASE_DIR}/app/netlogo-6.1.0.jar|g' netlogo.sh
# sed -i.bak 's|-Dfile.encoding=UTF-8|-Dfile.encoding=UTF-8 -Dnetlogo.models.dir=${BASE_DIR}/app/models|g' netlogo-headless.sh
# sed -i.bak 's|-Dfile.encoding=UTF-8|-Dfile.encoding=UTF-8 -Dnetlogo.models.dir=${BASE_DIR}/app/models|g' netlogo.sh

# rm *.bak
