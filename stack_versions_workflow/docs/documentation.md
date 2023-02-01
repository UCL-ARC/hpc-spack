# Documentation for these scripts

## files: spd, spdr, spdsper

These are some short names for the scripts: 
- stack_versions_workflow/spack-deps.sh
- stack_versions_workflow/spack-deps-run.sh
- stack_versions_workflow/spack-deps-spack-env-run.sh

## spack-deps.sh, spack-deps-run.sh, spack-deps-spack-env-run.sh

These set up the environent for a couple of aspects of spack and/or run a command in such an environment. The latter is used by the main scripts when they shell out to call spack commands. So:
- /home/ucapcjg/Scratch/AHS-5_pack_investigations/hpc-spack/stack_versions_workflow/spack-deps.sh is to be __sourced__ and adds to the environment of the current process dependencies of spack. In paricular it provides (i) a python 3.8 (pyhton 2 is deprecared by spack) to run the spack commands, which are in python, and (ii) gcc 11, which is the system compiled which spack initially uses to build packages, until spack has built a compiler itself. Currently both of these are provided by the scl mechanism and the compiler is from 'devtoolset-11'

## create_spack_site.py, create_spack_site.sh

A script to make a new directory in the root directory for the series of spack sites, clone spack into that so creating a new spack site, set some spack config, and create a spack environment of specs from a file, and build those specs. 

Later additions will create modules based on the installed apps, and will make use of build caches from earlier members of the series to speed builds.

The .sh calls the .py but first includes dependencies in the current process's environment, in particular python3.8 and a gcc 11. These are provided with the scl mechanism; gcc11 comes from 'devtoolset-11'.

## Other scripts

So far these are just tentative TODO placeholders 