# Spacksites - archive of spack environments
This directory is intended as an archive of spack environments, the spack.yaml files or the spack.lock files of all the spack environments of a site. 

Each subdirectory is for a single spack site at a particular time, and should allow a site to be reproduced. (Assuming no conflicts between spack environments or unknown dependencies between for concretization - if these problems in fact exist). The format for the subdirectory name is `spacksite_archive-<timestamp>-<site-name>`.

A way to begin work on a the next iteration of a site will be archive the present site here and then import all the environments from the archive to a new spack site. 