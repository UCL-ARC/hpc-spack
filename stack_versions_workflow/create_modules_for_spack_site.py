
"""
outline of intended function

Once a site has been created with create_spack_site.py, and that site has been 
inspected and verified, this script creates modules in respect of the apps etc 
installed in that site.

Several module sets are created, one for each section that we currently have. 
Each section might be defined by a spack environment, because spack has (?) 
a facility to create modules for an environment - if not pehaps some spec file will do

The modules are associated with the site and are left untouched once created
(as are the installed applications). New modules are created for the next period's 
installed applications.

"""