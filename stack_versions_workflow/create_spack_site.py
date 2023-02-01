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

this_scripts_dir = os.path.dirname(os.path.abspath(__file__))
print('This script is in directory {}'.format(this_scripts_dir))

# read this script's command line arguments e.g. to find new site name
parser = argparse.ArgumentParser(description='A script to create a new spack site and install ARC software stack.')
parser.add_argument('-p', '--period', required=True)
parser.add_argument('-c', '--config-file', required=False, default='FIND_RELATIVE')
parser.add_argument('-s', '--start-spack', required=False, default=False)
parser.add_help = True

args = parser.parse_args()

if args.config_file == 'FIND_RELATIVE':
  ini_file = os.path.join(this_scripts_dir, 'periodic_spack_site_generation.ini')
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
spacks_setup_env_for_site = os.path.join(new_spack_site, 'spack', 'share', 'spack', 'setup-env.sh')
print('source {}'.format(spacks_setup_env_for_site))
print('or run: create_spack.py -s -p {}'.format(args.period))

# import spack api from the new site
sys.path.append(os.path.join(new_spack_site, 'spack', 'lib', 'spack'))
import spack
print('spack version is: {}'.format(spack.spack_version_info))  # while API programming is not preferred approach, this does confirm spack is functional

# API or shell out. API has a learning curve - shell out will be path of least resistance.


# TODO copy this in the site config file - but with the correct path
# TODO find out whether there is a TMPDIR available (e.g. on compute node) - will speed build
# TODO when Myriad available check where these settings were made
build_stage = os.path.join(new_spack_site, 'build_stage')
# # """config:
# #   build_stage:
# #     - {}
# #   build_jobs: 6  """.format(build_stage)
# # TODO better: set this using spack API if it has a fn for it
# site_config = spack.config.get_config('config'  , scope='site')
# site_config['build_stage'] = build_stage
# site_config['build_jobs'] = 6
# spack.config.update_config('config', scope='site')

# try the config with shell out

os.mkdir(build_stage)  # TODO set the file mode parameter appropriately
# TODO *** run all these subprocesses in a context that has had spack available (avoid repeatedly running spacks setup-env.sh - using sister scipt sper for now ***
# tp make references to sister scipts easier (e.g. sper)
print('Changing current directory to {}'.format(this_scripts_dir))
os.chdir(this_scripts_dir)
print('Current directory changed to {}'.format(os.getcwd()))
# TODO in each of these subprocesses spack.s dependencies of python and gcc are set
# - but also need to set up this spack within that - so calling this sites setup-env.sh
# so TODO another scipt that does sper with setup env before running the argument program
subprocess.run(['./spdsper', spacks_setup_env_for_site, 'spack', 'config', '--scope=site', 'add', 'config:build_stage:{}'.format(build_stage) ])
subprocess.run(['./spdsper', spacks_setup_env_for_site, 'spack', 'config', '--scope=site', 'add', 'config:build_jobs:{}'.format(6) ])


# TODO find the compilers
# TODO make this more predicatble by setting config files
subprocess.run(['./spdsper', spacks_setup_env_for_site, 'spack', 'compiler', 'find', '--scope=site'])
# echo what has been found
subprocess.run(['./spdsper', spacks_setup_env_for_site, 'spack', 'compilers'])

# find the specs etc to define this spack site
first_spack_compilers = os.path.join(this_scripts_dir, 'spack_site_definitions', 'spacks_first_own_compilers.yaml')

# update the active spack repos with our special recipes
# TODO make the repos to use a ini file setting - so a section [spack-repos] 

# TODO update/check the yaml files for the period to have expected build and source cache dependencies on earlier ones
# or do this in a preliminray templating phase to create the new yaml file

# build spack's first compilers 
print("Installing first compilers with spack - creates a spack environment 'first_compilers'")

subprocess.run(['./spdsper', spacks_setup_env_for_site, 'spack', 'env', 'create', 'first_compilers', first_spack_compilers])
subprocess.run(['./spdsper', spacks_setup_env_for_site, 'spack', '-e', 'first_compilers', 'install'])

print("First compilers created")
subprocess.run(['./spdsper', spacks_setup_env_for_site, 'spack', 'find' ])
# build the site with the specs 
# TODO separate this part into a separate script 
# because may want to install specs in batches (to check on progress)