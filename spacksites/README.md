# Using sitepack – a spack wrapper to set up sibling spack sites
## Main steps
These steps should be carried out in order.  
1.	__Clone this repo__: `git clone https://github.com/UCL-ARC/hpc-spack.git`
2.	__Make a new spack site__: with the command `spacksites/spacksites create test_site1`. (You can use another naem for the site.) This will:
    1. make a directory for the new spack site, 
    2. clone spack into that,
    3. import, to the spack site, appropriate ones of the spack yaml config files in spacksites/settings (config.yaml, modules.yaml, packages.yaml), with all the defaults you will love. These include, default compiler for spack to use, the number of cores to use in a build, locating the build stage under the site directory (rather than some TMP, whick gets filled up), module name format and module location. (The current value, `$spack/../modules/$env`, of this last one will sepatate modules created by differnt spack environment files into different sub directories, with a desired result of facilitating corresponding separate sections in `module avail`.) The yaml files are selected automatically from those at `spacksites/settings/initial_site_*.yaml`.
    4. have spack identify the compilers already on your system (including that from a devtoolset if such is in the script for your system in `spacksites/process-env-scripts`). One of these will be used to build an up to date compiler inside spack - see the next step below.
3. __Install your first compiler into the spack site__: use `spacksites/spacksites install-env test_site1 first_compiler first_compiler.yaml`, where 'first_compiler' is the name for the spack environment that will contain the new compiler. first_compiler.yaml is found at `spacksites/spack-env-specs/first_compiler.yaml`. It makes sense to specify the same compiler there and in the `intial_site_packages_*.yaml` files. 

_TODO ??? after the first compiler is built in spack, do you need to `run spack compiler find` again??_

_TODO use expected paths for finding env yaml files (for 4. and 5.)_

4. __Install packages__: You are now ready to install further spack environments that specify the packages you want in your site. An eample command is: `spacksites/spacksites install-env test_site1 mpi mpi.yaml`. (`mpi.yaml` is not provided as an example - **you** have to decide what goes in it.) If your yaml file for an environment is not an absolute path it will be searched for from `spacksites/settings/spack-env-specs/build`. There are some other examples there.

_TODO for 5. wrap: spack module tcl refresh --delete-tree_

5. __Generate module files__: ___NOT YET IMPLEMENTED___ This again uses spack environment yaml files. These, however, do not have specs for packages but do have filters to select packages to inlcude in a module set, and these do not have to have the same sets of packages as were used to install the packages! An eample command is: `spacksites/spacksites make-modules test_site1 dev-tools.yaml`. This will generate the specified set of modules and put them at `site-name/modules/dev-tools`, for example, (unless some other path is specified in the yaml file with `roots: \ tcl: <path e.g. $spack/../modules/new-name>`).

## Useful spacksite commands
- `spacksites/spacksites list` - shows the names of the spack sites that you have created. These live in the root directory specified in - `spacksites/settings/spack_sites.ini`. The names returned are those of the subdirectories of the sites root directory.
- `spacksites/spacksites spack <site_name> <spack-args>` - executes a spack command on the named site. You do not have to activate the spack environment, which is done for you, for the duration of the command, in a subshell.
- `bash` then `eval $(spacksites/spacksites spack-setup-env <site_name>)` - this sets up your shell to run subsequent ordinary spack commands on the named one of your sites. `bash` first because setting the environment is hard to undo, and you may want to switch to another one of your sites. Your shellprompt is modified to show which spack site you are using.
- `spacksites/spacksites -h` - view the spacksite command help: 

## Optional steps 
Some things you might want to do between steps 1 and 2 above:
  - 1A.	__Optional__: Switch to the git branch of this repo that is of interest - usually `main`.
  - 1B.	__Optional__: Consider settings at `spacksites/settings/spack_sites.ini` at `[general]`. If you make no change, your root directory for the spack sites will be `test-spack-sites/`, a sibling of the repo you just cloned. 
  - 1C __Optional__: Consider the settins in the files `spacksites/settings/initial_site_*.yaml`. e.g. for an actual rather then a test spack site you would want to increase `build_jobs:`, the number of cores used when intalling packages.

Something you might want to do between steps 2 and 3 aboove:
  - 2A. __Optional__: ___NOT YET IMPLEMENTED___ make links to other spack sites to save time on building packages. This will be spacksite commands allowing you specifiy the links with your site names. This only make sense when you have two or more spack sites.

## Personal spack config - ignored
Spack has config settings at several priorty level. Personal, user, config overrides that in a site. Our sites will be administered by several operators, so for clarity and avoiding mistakes, user congfiguration files are ignored by spacksites and also when activating spack in your shell with `spacksites spack-set-up-env ...`. This is done by setting the environment variable `SPACK_DISABLE_LOCAL_CONFIG`; this does not happen if you set up spack in the shell yourself without that - so be aware. The setting also overrides the system scope spack config.

## Shell environment scripts at `spacksites/process-env-scripts`
These scripts relate to the environment of the process/shell in which spacksite and spack commands are run. Do not confuse this environment with a spack environment. The scripts put in place spack's dependencies. Those are a system compiler that it can use to compile its first compiler and a sensible version of python to run spack adn spacksites. The filename suffices identifying the operating system are there to help spacksites work out of the box. Rhel-7.8 is for UCL ARC clusters and Ubuntu-20.04 is to allow development on a laptop, in particular the author's, using WSL. Extra scripts would have to be provided for other operating systems / the base of installed system packages.