# Using sitepack – a spack wrapper to set up sibling spack sites
## Cloning spacksite and starting a new spack site
These steps should be carried out in order. If you omit any __Optionsal__ step something useful will still happen. 
1.	`git clone https://github.com/UCL-ARC/hpc-spack.git`
2.	__Optional__: Switch to the git branch of this repo that is of interest - usually `main`.
3.	__Optional__: consider settings at `spacksites/settings/spack_sites.ini` at `[general]`. If you make no change, your root directory for the spack sites will be `test-spack-sites/`, a sibling of the repo you just cloned. 
4.	__Optional__: view the spacksite command help: `spacksites/spacksites -h`
5.	__Make a new spack site__: `spacksites/spacksites create test_site1`. This will:
    1. make a directory for the new spack site, 
    2. make a subdirectory for the build stage, 
    3. import, to the spack site, and fill in the blanks of, appropriate ones of the spack yaml config files in spacksites/settings
    4. have spack identify the compilers on your system (including that from a devtoolset if such is in the script for your system in `spacksites/process-env-scripts`). One of these will be used to build an up to date compiler inside spack (see below).
6. __Optional__: **NOT IMPLEMENTED** make links to other spack sites to save time on building packages. This will be spacksite commands allowing you specifiy the links with your site names. This only make sense when you have two or more spack sites.
7. __Install your first compiler into the spack site__: either:
   1. `spacksites/spacksites install-env test_site1 compiler_env first_compiler.yaml`, where compiler-env is the name for the spack environment that will contain the new compiler, or
   2. **NOT IMPLEMENTED** `spacksites/spacksites test_site1 install-default-compiler` 
of which: 1. installs the compiler specified in spacksites/settings/first_compiler.yaml, and 2. installs the compiler specified in config.yaml as the default for spack to use in compiling packages. (If these two are not the same compiler version, then think about your settings.)

8. You are now ready to install further spack environments that specify the packages you want in your site. An eample command is: `spacksites/spacksites install-env test_site1 mpi mpi.yaml`. (`mpi.yaml` is not provided as an example - **you** have to decide what goes in it.)

9. Generate module files: **NOT IMPLEMENTED** - this will be spacksite commands making use of more spack environment files. These do not have to be the same ones as were used to install the packages! 

## Other spacksite commands
- `spacksites/spacksites list` - shows the names of the spack sites that you have created. These live in the root directory specified in - `spacksites/settings/spack_sites.ini`. The names returned are those of the subdirectories of the sites root directory.
- `spacksites/spacksites spack <site_name> <spack-args>` - executes a spack command on the named site. You do not have to activate the spack environment, which is done for you, for the duration of the command, in a subshell.

- `bash` then `source spacksites/spacksites spack-setup-env <site_name>` - this sets up your environment to run subsequent ordinary spack commands on the named one of your sites. `bash` first because setting the environment is hard to undo, and you may want to switch to another one of your sites. 