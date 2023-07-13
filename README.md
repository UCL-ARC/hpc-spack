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

Once the repo already exists, start from here. Our sites location is `/shared/ucl/apps/spack/0.20` for 0.20.x.

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
eval $(spacksites/spacksites spack-setup-env hk-initial-stack)
```

You can now run `spack find` to show the installed packages, or `spack info --all $package` to show available versions of that package to install.

There is more detailed info and possible considerations in [Spacksites README](spacksites/README.md#using-sites).

### Pulling changes into different site roots

If you are not using our default site root for this version, when you pull down changes later on you will need to alter `sites_root` in [spack_sites.ini](spacksites/settings/spack_sites.ini) back to the correct location you are using. 

You could use a script like this one to stash changes, pull, and update `sites_root` for you.

```
spacksites/myriad-utilities/git-pull-on-myriad.sh 
```

### Buildcache

Our Spack-versioned buildcache is at `/shared/ucl/apps/spack/0.20/buildcache` for 0.20.x.

```
# take my site-installed gcc@12.2.0 and all its dependencies, and put it into a buildcache at this location
spack buildcache push --allow-root /shared/ucl/apps/spack/0.20/buildcache gcc@12.2.0
```

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
