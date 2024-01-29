# hpc-spack
Solutions - HPC's Spack config

There should be a branch of this repo for each major Spack release. Branch 0.20 covers all 0.20.x Spack versions.

## Using spacksites to work with central installs as ccspapp

The very first user of this version of Spack and this repo should create an Spack-versioned directory to check out into, clone this repo and switch to the desired branch. This example is for Spack 0.20.x:

```
mkdir -p /home/ccspapp/Scratch/spack/0.20
cd /home/ccspapp/Scratch/spack/0.20

git clone https://github.com/UCL-ARC/hpc-spack.git --branch 0.20
```

Once the repo already exists, start from here. Our sites location is `/shared/ucl/apps/spack/0.20` for 0.20.x which is defined in [spack_sites.ini](spacksites/settings/spack_sites.ini).

```
cd /home/ccspapp/Scratch/spack/0.20/hpc-spack

# initialise spacksites
source spacksites/myriad-utilities/init-spacksites-on-myriad.sh

# make your new site - we've been prefixing $site_name with initials
spacksites/spacksites create $site_name

# install your first compiler into your site - will use the buildcache as long as it exists
# $env_name will be the name of the environment you are creating, eg first_compiler.
spacksites/spacksites install-env $site_name $env_name first_compiler.yaml

# get ready to run spack commands as normal for this site
eval $(spacksites/spacksites spack-setup-env $site_name)
```

You can now run `spack find` to show the installed packages, or `spack info --all $package` to show available versions of that package to install.

There is more detailed info and possible considerations in [Spacksites README](spacksites/README.md#using-sites).

### Intended use

Make a site for a small subset of software, test them, end up with a .yaml specifying what has been installed, decide those are the 
versions we want, push them into the buildcache so they can be picked up by everyone, work on the next subset until we have a large 
set of software packages and one large .yaml file while keeping different versions of the same build dependencies to a necessary minimum.

On new releases of Spack, rebuild the build cache, see if there are package versions that have been removed and new ones we want to include.

### Buildcache

Our Spack-versioned buildcache is at `/shared/ucl/apps/spack/0.20/buildcache` for 0.20.x.

This is specified in [initial_site_mirrors.yaml](spacksites/settings/initial_site_mirrors.yaml) and gets copied into `$site_name/spack/etc/spack/mirrors.yaml` in any sites you create.

To push a package to the buildcache as ccspapp:

```
# take my site-installed gcc@12.2.0 and all its dependencies, and put it into a buildcache at this location
spack buildcache push --allow-root /shared/ucl/apps/spack/0.20/buildcache gcc@12.2.0
```

### Local package repositories

We have two local package repos at the top level in this repository:

```
repos/dev
repos/ucl
```

The intent is that `dev` is for specs that we are developing and don't consider to be fully tested. 
`ucl` is for non-dev specs, including updated versions from Spack's `develop` branch in situations
where we need the updated version but it doesn't exist in the version of Spack we are currently using.

These repos are defined in [spacksites/settings/initial_site_repos.yaml](spacksites/settings/initial_site_repos.yaml) 
so all new sites will pick those up.

Spack will search through the repos in order to find requested specs, so it will find our versions first.

```
# show repos for the active site
spack repo list
==> 3 package repositories.
ucl.arc.hpc        /lustre/scratch/scratch/ccspapp/spack/0.20/hpc-spack/repos/ucl
ucl.arc.hpc.dev    /lustre/scratch/scratch/ccspapp/spack/0.20/hpc-spack/repos/dev
builtin            /lustre/shared/ucl/apps/spack/0.20/hk-initial-stack/spack/var/spack/repos/builtin
```

If you have an existing site and we have added new repos that it does not have, add them to
`spack/etc/spack/repos.yaml` in your site.

[Spack documentation on Package Repositories](https://spack.readthedocs.io/en/latest/repositories.html).

#### zlib-api virtual package

If we pick up a spec from `develop` that depends on `zlib-api`, we need to change that to `zlib` in
our local copy for Spack 0.20 - adding a comment to the package that we have done this may be 
helpful!

### Updating to a new Spack version

When there is a major version release, we need to:

 - Create a new branch in this repo
 - In that branch, edit the version in [spack_sites.ini](spacksites/settings/spack_sites.ini)
 - Update the sites_root in [spack_sites.ini](spacksites/settings/spack_sites.ini)
 - Update the buildcache location in [initial_site_mirrors.yaml](spacksites/settings/initial_site_mirrors.yaml)
 - Check whether the major changes/deprecations for the new version require any alterations to the spack commands spacksites runs, [initial_site_modules.yaml](spacksites/settings/initial_site_modules.yaml), any other config or format changes or changes in default behaviour.
 - Check out the new branch in a new directory, as when starting from scratch above.
 - Create the new sites_root in `/shared/ucl/apps/$version`
 - Create a new buildcache in the sites_root, checking whether the versions we build are still available in the new Spack version and updating our site .yaml files if they do not.
 - Check our `ucl` local package repo to see if specs we got from `develop` now exist in builtin. If they do, delete the local one.

## Running spacksites as your own user

You can run spacksites and use the existing buildcache as your own user rather than `ccspapp`. You will need to make these changes.

#### Check your login environment

The instructions all assume that you have the default Myriad login environment (you can view the default `.bashrc` and `.bash_profile` in `/etc/skel`).

Most importantly, you mustn't have any other python loaded or PYTHONPATH set, or other spack environment active, or things are likely to break in strange ways.

#### Update spack_sites.ini for your user locations

You may wish to make a private fork of this repo with the [spack_sites.ini](spacksites/settings/spack_sites.ini) changes suitable for your install location, or you can create another script like this one to stash changes, pull, and update `sites_root` and other settings in the .ini file for you.

```
spacksites/myriad-utilities/git-pull-on-myriad.sh
```

#### Update or create your own init-spacksites-on-myriad.sh

You will need to change [init-spacksites-on-myriad.sh](spacksites/myriad-utilities/init-spacksites-on-myriad.sh) so it is suitable for your own user and install of spacksites rather than `ccspapp`, or create your own similar init script. Right now that script hard-codes where the spacksites checkout location is.

#### Initialise spacksites and create a site

The first two steps are the same as above:

```
# initialise spacksites (or replace this with your own init script)
source spacksites/myriad-utilities/init-spacksites-on-myriad.sh

# make your new site - this will be created in your specified site_root
spacksites/spacksites create $site_name
```

#### Set up the env so you can run Spack commands

```
# get ready to run spack commands as normal for this site
eval $(spacksites/spacksites spack-setup-env $site_name)
```

#### Trust the buildcache

The public gpg key for the buildcache exists in `/shared/ucl/apps/spack/0.20/buildcache/build_cache/_pgp/` for version 0.20. This key belongs to the `ccspapp` user.

```
# To use the buildcache you need to trust our existing public gpg key
spack gpg trust <keyfile>
```

#### Install your first compiler

```
# install your first compiler into your site - will use the buildcache as long as it exists
# $env_name will be the name of the environment you are creating, eg first_compiler.
spacksites/spacksites install-env $site_name $env_name first_compiler.yaml
```

You can now go ahead and install any other packages you want to build.

#### Optional: change build_stage

You can set a different build_stage in your site's `config.yaml` file (suggested to use `$XDG_RUNTIME_DIR` if you are on the login nodes).

Spack's default config.yaml for your site is in `$site_root/$site_name/etc/spack/defaults/config.yaml`. Each site has its own.

Note: spacksites deliberately ignores any other local Spack config files to avoid clashes with other Spack setups you may have: [Personal spack config - ignored](spacksites/README.md#personal-spack-config---ignored) 


## Get started with a personal install

This is for non-spacksites-managed personal Spack use.

```
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
```

A script to load the SCLs which will make Python 3.8 and GCC 11.2 available to you on the nodes:
Referring to this from now on as `load_scls.sh`.

```
#!/bin/bash
# Source this.

UCL_SCLS="rh-python38 devtoolset-11"

for a in ${UCL_SCLS}
do
   source /opt/rh/${a}/enable
done
export X_SCLS="${UCL_SCLS} ${X_SCLS}"
```

You can then `source load_scls.sh` and will see the following are now available:

```
[cceahke@login13 spack]$ which g++
/opt/rh/devtoolset-11/root/usr/bin/g++
[cceahke@login13 spack]$ which python
/opt/rh/rh-python38/root/usr/bin/python
```

Spack setup: do we want to do this? It sets `$SPACK_ROOT` among other things.

```
source spack/share/spack/setup-env.sh
```

Spack's default config.yaml is `$SPACK_ROOT/etc/spack/defaults/config.yaml`. Things I changed straight away:

```
  build_stage:
    - $user_cache_path/stage

  build_jobs: 4
```

`build_stage` is where all the temporary building happens and must not be in `/tmp`.

You can then start to use Spack.

```
spack list gromacs
spack info --all gromacs
```

See which compilers spack finds: if you sourced setup-env.sh before sourcing load_scls.sh then it will not look in our new `/opt/rh/devtoolset-11`.

```
spack compilers
==> Available compilers
-- gcc rhel7-x86_64 ---------------------------------------------
gcc@4.9.2  gcc@4.8.5
```

So tell it to look for the new one.

```
spack compiler add /opt/rh/devtoolset-11/root/usr/bin/
==> Added 1 new compiler to /home/cceahke/.spack/linux/compilers.yaml
    gcc@11.2.1
==> Compilers are defined in the following files:
    /home/cceahke/.spack/linux/compilers.yaml
```

## Other setups

Spack has a repo at https://github.com/spack/spack-configs

- LLNL, 2021, TREX Hackathon, Intro to Spack: https://www.trex-coe.eu/sites/default/files/TREX%20Build-systems%20Hackathon%20-%20Nov%202021/TREX%20-%20Spack%20presentation.pdf
- LLNL, 2022, Software Deployment Process at NERSC: Deploying the Extreme-scale Scientific Software Stack (E4S) Using Spack at the National Energy Research Scientific Computing Center (NERSC): https://escholarship.org/uc/item/5zh5z08q
- EPCC, 2020, Software Packages in HPC with Spack and EasyBuild (brief overview): https://www.archer2.ac.uk/training/courses/200617-spack-easybuild/

### User-level

- ORNL, installing own user packages with a base central environment and chained Spack instances https://docs.olcf.ornl.gov/software/spack_env/summit_spack_env.html

### Additional

- E4S as mentioned above uses Spack and provides a build cache and containers. Attempts to put together an interoperable set of packages. "The Extreme-Scale Scientific Software Stack (E4S) is a community effort supported by the Exascale Computing Project (ECP) to provide an ecosystem of open source software packages for developing, deploying and running scientific applications on HPC platforms."
   - https://e4s-project.github.io/
- This may be of use if we have more AMD and need to build with AOCC/AOCL.
   - AMD, Spack support of HPC applications https://developer.amd.com/spack/
