#!/usr/bin/env python3

"""
outline of intended function

create a new spack site with the apps etc defined for the new period 
will need to read a use specs for that period (in a spack format yaml file)
will create that in a new spack site just for that
separate yaml file included for long term constant settings e.g. compiler
  (or put that in the period spec file???)
will need file for long term non spack paramters (.ini to avoid confusion with spack yaml files)
  - e.g. root directory for all period spack sites.



"""

import argparse
import os
import sys
import configparser
import subprocess

# (check which version of python we are using - to meet spack requirement)
# TODO

# read this script's command line arguments e.g. to find new site name
parser = argparse.ArgumentParser(description='A script to create a new spack site and install ARC software stack.')
parser.add_argument('-p', '--period', required=True)
parser.add_argument('-c', '--config-file', required=False, default='FIND_RELATIVE')
parser.add_argument('-s', '--start-spack', required=False, default=False)
parser.add_help = True

args = parser.parse_args()

if args.config_file == 'FIND_RELATIVE':
  ini_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'periodic_spack_site_generation.ini')
else:
  ini_file = os.path.abspath(args.settings_file)
if not args.start_spack:
  print('Using settings file at {}'.format(ini_file))

# read the ini file to find where to put the new site and the spack version to use
config = configparser.ConfigParser()
config.sections()
config.read(ini_file)
spack_sites_root = os.path.abspath(config['general']['sites_root'])
new_spack_site = os.path.join(spack_sites_root, args.period)
spack_version = config['general']['spack_version']
# TODO check in the spack repo that this tag exists

# check that the site does not exist - stop if it does - but then create it
if os.path.exists(new_spack_site):
  raise FileExistsError('Requested new spack site directory ({}) already exists'.format(new_spack_site))

# this should be the only print statement for this CLI option
# if the call is to activate spack do that and terminate (TODO - move to separate script)
if args.start_spack:
  # return bash script lines - user will   eval $(<script name.py> -s -p <period name>)
  # TODO allow for other shells than bash? see https://spack.readthedocs.io/en/latest/getting_started.html#shell-support
  print('source {}'.format(os.path.join(new_spack_site, 'spack', 'share', 'spack', 'setup-env.sh')))  
  exit()

# create the spack site by downloading it from git and select version 
os.mkdir(new_spack_site)
os.chdir(new_spack_site)
# TODO make spack repo URL an .ini setting 
# TODO check for no error
subprocess.run(['git', 'clone', '-c', 'feature.manyFiles=true', '--branch', spack_version, 'https://github.com/spack/spack.git'])

# add the new site to the .ini file under extant sites


# echo some info about how to activate spack for this site
print('To activate spack in bash for this new spack site: ')
print('source {}'.format(os.path.join(new_spack_site, 'spack', 'share', 'spack', 'setup-env.sh')))
print('or run: create_spack.py -s -p {}'.format(args.period))

# import spack api from the new site
sys.path.append(os.path.join(new_spack_site, 'spack', 'lib', 'spack'))
import spack
print('spack version is: {}'.format(spack.spack_version_info))

# TODO copy in the site config file
"""
config:
  build_stage:
    - /home/ucapcjg/Scratch/AHS-5_spack_investigations/spack/spack/share/spack/build-stage
  build_jobs: 6
  """
# TODO find the compilers
# first - Owains scl load of gcc11 - would only be needed for compiler site

# find the specs etc to define this spack site


# update the active spack repos with our special recipes
# TODO make the repos to use a ini file setting - so a section [spack-repos] 

# TODO update/check the yaml files for the period to have expected build and source cache dependencies on earlier ones
# or do this in a preliminray templating phase to create the new yaml file

# build the site with the specs 
# TODO separate this part into a separate script 
# because may want to install specs in batches (to check on progress)