# Progress

1 Feb 2023
stack_versions_workflow/create_spack_site.py 
now downloads a new spack site, sets some config for it and finds the compilers (including the desired gcc 11, from the scl)

## next thing:
do some specs for the site in a yaml, particularly gcc 12, find that spec (by period name) and 

## backlog:
set config for own repo to spack recipes
get it working in /shared/apps (minor barrier: getting code to download when am ccspapp)

## futurelog:
more specs (separate file from compiler?)
script to activate spack in an open shell for a named period using spack's set-env.sh (check that another site is not yet activated)
standard spack settings yaml to include in all periods' yaml
generate period's modules (using an env for each section)
push compiled packages to binary store and use them in  
in each site have a provenance folder and write to it the activities of this script and the specs files used.

