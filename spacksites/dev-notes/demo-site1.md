# Demo-site1

# creating it

as ever: `become ccspapp`, `cd Scratch/hpc-spack`, `module load python3/recommended` and `alias sps=spacksites/spacksites`

`sps create demo-site1`, this creates a spack site, configures it with the initial yaml files, makes some keys for the site
- check out the initial*.yaml files in this repo's settings file to see what it sets up

`sps install-env demo-site1 first_compiler first_compiler.yaml`, this installs gcc13 and its build and run dependencies, by downloading them from the build cache

finally:
```
spack load gcc@13.1.0
spack compiler find --scope=site
spack unload gcc@13.1.0
```
tells spack that it can use gcc13 as one of its compilers - DONE integrate this step to the sps install-env first_compiler first_compiler.yaml command

# exploring it

as ever: `become ccspapp`, `cd Scratch/hpc-spack` and then

```
bash
alias sps=spacksites/spacksites
eval $(sps spack-setup-env demo-site1)
```

after that ordinary spack commands will apply to demo-site1

# building stuff
