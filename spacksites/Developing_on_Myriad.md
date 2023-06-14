# Temporary notes for developing Spack specs and environments on Myriad

These notes are for ARC HPC solutions staff developing Spack specifications and environments on Myriad

You should build test sites in the common area. This is at `/shared/ucl/apps/spack-test/`, but you do not need to know that path because it is coded into the settings of the hpc-spack installation for ccspapp on Myriad. To use that installation, do this:

## Logging into Myriad to use the common hpc-spack installation, under the ccspapp user
A typical sequence of commands to work on an existing site.
```
ssh myriad
become ccspapp
cd Scratch/hpc-spack
spacksites/process-env-scripts/init-spacksites-on-myriad.sh  # loads python3.8 and gcc12
alias sps=/home/ccspapp/Scratch/hpc-spack/spacksites/spacksites
sps list  # To verify operation - this just shows a list of spacksites available to work on
```

The above is abbreviated and improved on (uses system python38 to run spacksites):
```
ssh myriad
become ccspapp
source /home/ccspapp/Scratch/hpc-spack/spacksites/process-env-scripts/init-spacksites-on-myriad.sh
```

# To work on a particular site, e.g. site1

```
alias sps=/home/ccspapp/Scratch/hpc-spack/spacksites/spacksites
eval $(sps spack-setup-env site1)
```
The later commands are for working on a particular spack site, `site1`. You may well want to create and work on others - see the README. Indeed for your own experimentations create sites having names begining with your initials! We can consolidate efforts later.

## Contributing environments back to the hpc-spack repo
When you create an environment on one of your test sites on Myriad the definition of the environment, including tweaks made with `spack config edit` are part of the spack site and not the local copy of the hpc-spack code repo. When you are happy with the definition of a spack environment copy it to a spack environment definition .yaml file (aka a "template" in hpc-spack speak) in the directory `hpc-spack/spacksites/spack-env-templates/dev1/build`. There it is in the local code repo copy, so you can (1) commit it and then (2) push it to github. For (2) you will need to set up a personal key for github `/lustre/home/ccspapp/.ssh`.

You may well not want to develop and push file `spacksites/settings/spack_sites.ini` because this has a local path value edited to point to the spack sites on Myriad. 
