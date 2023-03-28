# Using sitepack – a spack wrapper to set up sibling spack sites
## Main steps

These steps should be carried out in order.  
1.	__Clone this repo__: `git clone https://github.com/UCL-ARC/hpc-spack.git`
2.	__Make a new spack site__: with the command `spacksites/spacksites create test_site1`. (You can use another name for the site.) This will:
    1. make a directory for the new spack site, 
    2. clone spack into that,
    3. import, to the spack site, appropriate ones of the spack yaml config files in spacksites/settings (config.yaml, modules.yaml, packages.yaml), with all the defaults you will love. These include, default compiler for spack to use, the number of cores to use in a build, locating the build stage under the site directory (rather than some TMP, whick gets filled up), module name format and module location. (The current value, `$spack/../modules/$env`, of this last one will sepatate modules created by differnt spack environment files into different sub directories, with a desired result of facilitating corresponding separate sections in `module avail`.) The yaml files are selected automatically from those at `spacksites/settings/initial_site_*.yaml`.  
    4. have spack identify the compilers already on your system (including that from a devtoolset if such is in the script for your system in `spacksites/process-env-scripts`). One of these will be used to build an up to date compiler inside spack - see the next step below.
3. __Install your first compiler into the spack site__: use `spacksites/spacksites install-env test_site1 first_compiler first_compiler.yaml`, where `first_compiler` is the name for the spack environment that will contain the new compiler. `first_compiler.yaml` is found at `spacksites/spack-env-templates/first_compiler.yaml`. It makes sense to specify the same compiler there and in the `intial_site_packages_*.yaml` files. 

## Optional steps 
Some things you might want to do between steps 1 and 2 above:
  - 1A.	__Optional__: Switch to the git branch of this repo that is of interest, if that is not `main`.
  - 1B.	__Optional__: Consider settings in  `spacksites/settings/spack_sites.ini` under `[general]`. If you make no change, your root directory for the spack sites will be `test-spack-sites/`, a sibling of the repo you just cloned. 
  - 1C. __Optional__: Consider the settings in the files `spacksites/settings/initial_site_*.yaml`. e.g. for an actual, rather than a test, spack site you would want to increase `build_jobs:`, the number of cores used when intalling packages. The configration of your spack site can be altered later with the usual spack commands.
  - 1D. __Optional__: Consider the setting in `spacksites/settings/spack_sites.ini` of `[spack_env_templates][active_set]`. This governs which set of spack environment templates is used by default. You may change this setting later, and access to other sets is not prevented in the meantime; there is a path syntax for those. Indeed, using templates from elsewhere is not prevented. See the relevant sections below for how `spacksites` helps with spack environments4. 

Something you might want to do between steps 2 and 3 above:
  - 2A. __Optional__: ___NOT YET IMPLEMENTED___ make links to other spack sites to save time on building packages. This will be spacksite commands allowing you specifiy the links with your site names. This only make sense when you have two or more spack sites.

## Using sites
At this point you have a new spack site that you can use as normal. There are two activities that you will want to do with your new spack site(s): 
  - Install spack packages, and
  - generate modulefiles.

`spacksites` provides particular commands for both of those - see steps 4. and 5., later below. However, `spacksites` also offers two general commands / methods for you to carry out any spack command on your new site, which you will need as part of the process. These are:
- __To execute a single spack command on the named site:__ `spacksites/spacksites spack <site_name> <spack-args>` You do not have to activate the spack environment in your shell, which is done for you, but only for the duration of the command.  # ***TODO fix:*** passthorough of --option options (at the moment they are consumed, with error, by spacksites)
- __To set up your shell to run subsequent ordinary spack commands on the named one of your sites:__ `bash` then `eval $(spacksites/spacksites spack-setup-env <site_name>)`. `bash` first because setting the environment is hard to undo, and you may want to switch to another one of your sites. Your shell prompt is modified to show which spack site you are using.

The preferred way to __build up a new site__ is to make spack environments from template spack environments. These can be used both to install packages to, and to create module files from, your spack site. `spacksites` includes convenient stores for spack environement templates, which are described first, followed by `spacksites` commands for using them.

## Spack environment templates
These are stored at `spacksites/spack-env-templates`. This is a general purpose and development store. Subdirectories divide the templates into sets, for whatever purpose. Each of those has a `build` subdirectory and a `modules` subdirectory, depending on to which of those purposes the environment is directed. Examples in the `dev1` subdirectory show the distinction in the spack configuration items used. These directories may also contain `spack.lock` files. 

Template spack environments are also to be found in the `spack-env-archive` directory. These are preserved `spack.yaml` and `spack.lock` files from other spack sites, which you may now use as templates for new spack environments in your new site. How such archives are created is described later below. Each subdirectory is an archive of a one spack site at a particular time. The format of the subdirectrory name is `spacksite_archive-<timestamp>-<site-name>`. One way to iterate a software installation through a series of spack sites is to archive all the environments of the site of the last iteration and then import those to a new site. You can make changes to the spack environments in your new site before building the software. Another way is to copy the preserved environment files to somewhere, make changes and then import them.  

## Spacksite commands for using template spack environments
(main step numbering continues from 1., 2., 3. above)

4. __Install packages from a template environment template__: You are now ready to install further spack environments that specify the packages you want in your site. An eample command is: `spacksites/spacksites install-env test_site1 mpi mpi.yaml`. (`mpi.yaml` is not provided as an example - **you** have to decide what goes in it.) If you sepcify the yaml file for an environment with just a plain basename, it will be searched for from `spacksites/settings/spack-env-templates/<active_set>/build`. If you use a relative path it will be seached for from `spackstites/spack-env-archive`. Absolute paths are treated as such.

__TODO Implement this:__ 
`spacksties create-env test_site1 mpi mpi.yaml`  This allows you just to create a spack site from the template. You may then inspect it, e.g. to see how it concretizes, and change the configuration before installing the packages it has defined, using ordinary spack commands.

___TODO for 5. wrap: spack module tcl refresh --delete-tree___
___TODO use expected paths for finding env yaml files (for  5.)___

5. __Generate module files__: ___TODO NOT YET IMPLEMENTED___ This again uses spack environment yaml files. These, however, do not have specs for packages but do have filters to select packages to include in a module set, and these do not have to be the same sets of packages as in the environments that were used to install them! An example command is: `spacksites/spacksites make-modules test_site1 <section>`. This will generate the specified set of modules and put them at `site-name/modules/<section>`, for example, (unless some other path is specified in the yaml file at `spacksites/spack-env-templates/modules/<section>` with `roots: \ tcl: <path e.g. $spack/../modules/<section>>`).

If you want to add the environment defining the modules permanently to the site, use `spacksties create-env ...` and then use `spack module tcl refresh --delete-tree` whenever needed to (re)create the module files.  

## Archiving spack enviroment definitions and iterating spack sites 
***TODO NOT YET IMPLEMENTED*** There will be some spacksite commands to round up spack environment definitions into the archive location described above. Files to preserve may well include the spack.yaml and spack.lock files for each spack environment in the site. 

## Other  spacksite commands
- `spacksites/spacksites list` - shows the names of the spack sites that you have created. These live in the root directory specified in - `spacksites/settings/spack_sites.ini`. The names returned are those of the subdirectories of the sites root directory.
- `spacksites/spacksites -h` - view the spacksite command help: 

## Personal spack config - ignored
`spack` has config settings at several priorty level. Personal, user, config overrides that in a site. Our sites will be administered by several operators, so for clarity and avoiding mistakes, user congfiguration files are ignored by spacksites and also when activating spack in your shell with `spacksites spack-set-up-env ...`. This is done by setting the environment variable `SPACK_DISABLE_LOCAL_CONFIG`; this does not happen if you set up spack in the shell yourself without that - so be aware. The setting also overrides the system scope spack config.

## Other shell environment variables
`spacksites` passes `HPC_SPACK_ROOT` to spack. This is a reference to the root of this git repo and allows its use in paths in `spack` config files to point to items in this repo. In particular repos.yaml copied to new sites uses it to point to the `spack` package repo in this git repo. Use of ordinary `spack` commands without this variable being set may cause an error when trying to access our homebuilt `spack` packages in `hpc-spack/repos`. 

## Shell environment scripts at `spacksites/process-env-scripts`
These scripts relate to the environment of the process/shell in which spacksite and spack commands are run. This environment is not to be confused with a spack environment. The scripts put in place spack's dependencies. Those are a system compiler that it can use to compile its first compiler and a sensible version of python to run spack and spacksites. The suffices of the filenames of these scripts identifying the operating system are there to help spacksites work out of the box. Rhel-7.8 is for UCL ARC clusters and Ubuntu-20.04 is to allow development on a laptop, in particular the author's, using WSL. Extra scripts may have to be provided for other operating systems / the base of installed system packages, in particular if they are lacking in the aforementioned dependencies. 

## Spack environment development tips
To be able to divide efforts and to make testing more finite we can split our packages into separate environments. There seems to be many ways to upset a spack site so to develop the definition of an environment it may be better to develop it in its own separate spack site - use this spacksites tool to create it. When these work they can be combined (at the cost perhaps of then finding more conflicts?)  

Check when concretizing that it has selected the desired compiler. Building takes a long time. 

When you make changes to the confuration of a sites's config, usually the package specs, the way to preserve it is to view it with `spack config edit` copy what you see, or the relevent part thereof, and paste it into the environment template file in this repo.  
