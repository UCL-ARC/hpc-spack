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
#     spack install clojure
#
# You can edit this file again by typing:
#
#     spack edit clojure
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *

import os, shutil, subprocess

class Clojure(Package):
    """The Clojure programming languange"""

    # Add a proper url for your package's homepage here.
    homepage = "https://www.clojure.org/"
    url = "https://download.clojure.org/install/clojure-tools-1.11.1.1208.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("1.11.1.1208", sha256="6e7f6e34ce3aa18734c31249f073066c4f3fda69d8c66fe9f52e8c8587e17103")

    # Add dependencies if required.
    # depndencies on Java, bash, curl, rlwrap are stated at:
    # https://www.clojure.org/guides/install_clojure
    # FIXME: these are not setting run dependencies
    depends_on("bash")  # might be just a build dependency
    depends_on("curl")  #  might be just a build dependency
    depends_on("rlwrap")
    depends_on("java")  # clojure is wrtitten in java

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        # make()
        # make("install")

        print('**** in install function cwd is: ', os.getcwd())
        # this says cwd is /lustre/scratch/scratch/ucapcjg/AHS-5_spack_investigations/spack/spack/share/spack/build-stage/spack-stage-clojure-1.11.1.1208-hbrgylah7ozw4xubyhmawam52gielspu/spack-src
        # which is where the source files have been unpacked
        
        # lines from official install script:
        # lib_dir="$prefix_dir/lib"
        # bin_dir="$prefix_dir/bin"
        # man_dir="$prefix_dir/share/man/man1"
        # clojure_lib_dir="$lib_dir/clojure"
        # now in python:
        lib_dir = os.path.join(prefix, 'lib')
        bin_dir = os.path.join(prefix, 'bin')
        man_dir = os.path.join(prefix, 'share', 'man', 'man1')
        clojure_lib_dir = os.path.join(lib_dir, 'clojure')
        # and an extra one
        clojure_libexec_dir = os.path.join(clojure_lib_dir, 'libexec')
        # FIXME: decide on file mode for these dirs and use mode=0oXXX to set them
        os.makedirs(lib_dir)
        os.makedirs(bin_dir)
        os.makedirs(man_dir)
        os.makedirs(clojure_libexec_dir)  # this also makes parent of clojure_lib_dir 
        
        # lines from official install script
        # install -m644 clojure-tools/deps.edn "$clojure_lib_dir/deps.edn"
        # install -m644 clojure-tools/example-deps.edn "$clojure_lib_dir/example-deps.edn"
        # install -m644 clojure-tools/tools.edn "$clojure_lib_dir/tools.edn"
        # install -m644 clojure-tools/exec.jar "$clojure_lib_dir/libexec/exec.jar"
        # install -m644 clojure-tools/clojure-tools-1.11.1.1208.jar "$clojure_lib_dir/libexec/clojure-tools-1.11.1.1208.jar"
        # now in python:
        def install_file(source, destination, mode_bits):
            shutil.copy2(source, destination)
            os.chmod(destination, mode_bits)
        
        install_file('deps.edn', os.path.join(clojure_lib_dir, 'deps.edn'), 0o644)
        install_file('deps.edn', os.path.join(clojure_lib_dir, 'deps.edn'), 0o644)
        install_file('example-deps.edn', os.path.join(clojure_lib_dir, 'example-deps.edn'), 0o644)
        install_file('tools.edn', os.path.join(clojure_lib_dir, 'tools.edn'), 0o644)
        install_file('exec.jar', os.path.join(clojure_libexec_dir, 'exec.jar'), 0o644)
        install_file('clojure-tools-1.11.1.1208.jar', os.path.join(clojure_libexec_dir, 'clojure-tools-1.11.1.1208.jar'), 0o644)

        # lines from official install script
        # sed -i -e 's@PREFIX@'"$clojure_lib_dir"'@g' clojure-tools/clojure
        # sed -i -e 's@BINDIR@'"$bin_dir"'@g' clojure-tools/clj
        # install -m755 clojure-tools/clojure "$bin_dir/bin_dir"
        # install -m755 clojure-tools/clj "$bin_dir/clj"
        # now in python:
        subprocess.call(['sed', '-i', '-e', 's@PREFIX@{}@g'.format(clojure_lib_dir), 'clojure'])
        subprocess.call(['sed', '-i', '-e', 's@BINDIR@{}@g'.format(bin_dir), 'clj'])
        install_file('clojure', os.path.join(bin_dir, 'clojure'), 0o755)
        install_file('clj', os.path.join(bin_dir, 'clj'), 0o755)

        # lines from official install script
        # install -m644 clojure-tools/clojure.1 "$man_dir/clojure.1"
        # install -m644 clojure-tools/clj.1 "$man_dir/clj.1"
        # now in python:
        install_file('clojure.1', os.path.join(man_dir, 'clojure.1'), 0o644)
        install_file('clj.1', os.path.join(man_dir, 'clj.1'), 0o644)

        # it is expected that spack will tidy up the source files

# this package emulates this official install script:
# curl https://download.clojure.org/install/linux-install-1.11.1.1208.sh | cat
#   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                  Dload  Upload   Total   Spent    Left  Speed
# 100  1828  100  1828    0     0   9714      0 --:--:-- --:--:-- --:--:--  9723
# officila install script begins here:
# #!/usr/bin/env bash

# set -euo pipefail

# # Start
# do_usage() {
#   echo "Installs the Clojure command line tools."
#   echo -e
#   echo "Usage:"
#   echo "linux-install.sh [-p|--prefix <dir>]"
#   exit 1
# }

# default_prefix_dir="/usr/local"

# # use getopt if the number of params grows
# prefix_dir=$default_prefix_dir
# prefix_param=${1:-}
# prefix_value=${2:-}
# if [[ "$prefix_param" = "-p" || "$prefix_param" = "--prefix" ]]; then
#   if [[ -z "$prefix_value" ]]; then
#     do_usage
#   else
#     prefix_dir="$prefix_value"
#   fi
# fi

# echo "Downloading and expanding tar"
# curl -O https://download.clojure.org/install/clojure-tools-1.11.1.1208.tar.gz
# tar xzf clojure-tools-1.11.1.1208.tar.gz

# lib_dir="$prefix_dir/lib"
# bin_dir="$prefix_dir/bin"
# man_dir="$prefix_dir/share/man/man1"
# clojure_lib_dir="$lib_dir/clojure"

# echo "Installing libs into $clojure_lib_dir"
# mkdir -p $bin_dir $man_dir $clojure_lib_dir/libexec
# install -m644 clojure-tools/deps.edn "$clojure_lib_dir/deps.edn"
# install -m644 clojure-tools/example-deps.edn "$clojure_lib_dir/example-deps.edn"
# install -m644 clojure-tools/tools.edn "$clojure_lib_dir/tools.edn"
# install -m644 clojure-tools/exec.jar "$clojure_lib_dir/libexec/exec.jar"
# install -m644 clojure-tools/clojure-tools-1.11.1.1208.jar "$clojure_lib_dir/libexec/clojure-tools-1.11.1.1208.jar"

# echo "Installing clojure and clj into $bin_dir"
# sed -i -e 's@PREFIX@'"$clojure_lib_dir"'@g' clojure-tools/clojure
# sed -i -e 's@BINDIR@'"$bin_dir"'@g' clojure-tools/clj
# install -m755 clojure-tools/clojure "$bin_dir/clojure"
# install -m755 clojure-tools/clj "$bin_dir/clj"

# echo "Installing man pages into $man_dir"
# install -m644 clojure-tools/clojure.1 "$man_dir/clojure.1"
# install -m644 clojure-tools/clj.1 "$man_dir/clj.1"

# echo "Removing download"
# rm -rf clojure-tools
# rm -rf clojure-tools-1.11.1.1208.tar.gz
