# hpc-spack
Solutions - HPC's Spack config

## Get started with a personal install

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

See which compilers spack finds: does not look in our new `/opt/rh/devtoolset-11`.

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

- LLNL, 2021, TREX Hackathon, Intro to Spack: https://www.trex-coe.eu/sites/default/files/TREX%20Build-systems%20Hackathon%20-%20Nov%202021/TREX%20-%20Spack%20presentation.pdf
- EPCC, 2020, Software Packages in HPC with Spack and EasyBuild: https://www.archer2.ac.uk/training/courses/200617-spack-easybuild/
