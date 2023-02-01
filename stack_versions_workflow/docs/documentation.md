# Documentation for these scripts

## files: spd, spdr, spdsper

These are some short names for the scripts: 
- stack_versions_workflow/spack-deps.sh
- stack_versions_workflow/spack-deps-run.sh
- stack_versions_workflow/spack-deps-spack-env-run.sh

## spack-deps.sh, spack-deps-run.sh, spack-deps-spack-env-run.sh

These set up the environent for a couple of aspects of spack and/or run a command in such an environment. The latter is used by the main scripts when they shell out to call spack commands. So:
- /home/ucapcjg/Scratch/AHS-5_pack_investigations/hpc-spack/stack_versions_workflow/spack-deps.sh is to be __sourced__ and adds to the environment of the current process dependencies of spack. In paricular it provides (i) a python 3.8 (pyhton 2 is deprecared by spack) to run the spack commands, which are in python, and (ii) gcc 11, which is the system compiled which spack initially uses to build packages, until spack has built a compiler itself. Currently both of these are provided by the scl mechanism and the compiler is from 'devtoolset-11'

## Other scripts

So far these are just tentative TODO placeholders 