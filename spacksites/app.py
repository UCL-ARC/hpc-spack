#!/usr/bin/env python3
import os, sys
import yaml

# while this file can be run via: python -m spacksites <command args>,
# this PYTHONPATH manipulation allows this file to be run directly 
# which might be of help when pointing a debugger at it.
if __name__ == '__main__':
    print('# SPACKSITES: Adding ',  os.path.dirname(os.path.abspath('__FILE__')), ' to PYTHONPATH', file=sys.stderr)
    sys.path.append(os.path.dirname(os.path.abspath('__FILE__')))

import argparse

from spacksites.src.spacksite import Site
from spacksites.src.appconfig import AppConfig
from spacksites.src.scripts import Scripts
from spacksites.src.helpers import spacksites_dir

# for debuging
import inspect
import sys

# functions to carry out actions specified by cli arguments - args is the parsed arguments
# to do - factor out passing on args to base functions

def create(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    config = AppConfig(args.config_file)
    Scripts.make_links(config.spd_script)  # this is repetive here but avoids use having to init the application with this before any use
    # TODO allow for sites outside spack_sites_root e.g. by testing site name for being an absolute path
    # TODO consider site_name in the form abc/def
    # TODO validate characters in site_name
    # the new site object is dropped here because this is the end of the command
    # if a REPL is added to the project will need to pick it up for the REPL's state
    Site(os.path.join(config.spack_sites_root, args.site_name), config.initial_site_config_yaml, 
         config.initial_site_modules_yaml, config.initial_site_packages_yaml, config.initial_site_repos_yaml, config.initial_site_mirrors_yaml,
         config.spd_script, config.spdsper_script,
         spack_version=config.spack_version)

def spack(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    config = AppConfig(args.config_file)
    Scripts.make_links(config.spd_script)  # this is repetive here but avoids use having to init the application with this before any use
    site = Site(os.path.join(config.spack_sites_root, args.site_name), config.initial_site_config_yaml, config.initial_site_modules_yaml,
         config.initial_site_packages_yaml, config.initial_site_repos_yaml, config.initial_site_mirrors_yaml,
         config.spd_script, config.spdsper_script,
         spack_version=config.spack_version, error_if_non_existent=True)  # TODO fix: if this fn called before site created it will create it - refactor Site object not to auto create when missing
    spack_args = args.spack_args
    spack_args.insert(0, 'spack')
    site.run_command(spack_args)

def install_env(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    config = AppConfig(args.config_file)
    Scripts.make_links(config.spd_script)  # this is repetive here but avoids use having to init the application with this before any use
    # TODO same as TODOs in site_create() above
    site = Site(os.path.join(config.spack_sites_root, args.site_name), config.initial_site_config_yaml, config.initial_site_modules_yaml,
         config.initial_site_packages_yaml, config.initial_site_repos_yaml, config.initial_site_mirrors_yaml,
         config.spd_script, config.spdsper_script,
         spack_version=config.spack_version, error_if_non_existent=True)
    specs_file = args.specs_file
    if not os.path.isabs(specs_file):
        if specs_file == 'first_compiler.yaml':
            full_specs_file = os.path.join(spacksites_dir(), config.templates_active_set, specs_file)
        else:
            full_specs_file = os.path.join(spacksites_dir(), config.templates_active_set, 'build', specs_file)
    else:
        full_specs_file = specs_file
    site.install_spack_env(args.env_name, full_specs_file)
    if (not os.path.isabs(specs_file)) and (specs_file == 'first_compiler.yaml'):
        with open(config.initial_site_packages_yaml) as file:
            packages_yaml = yaml.safe_load(file)
        compiler_specs = packages_yaml['packages']['all']['compiler']
        for compiler_spec in compiler_specs:
            print('# SPACKSITES: found first compiler spec in packages.yaml', compiler_spec, file=sys.stderr)
            first_compiler_yaml_raw, err = site.run_commands(['spack -e '+args.env_name+' config get'])
            first_compiler_yaml = yaml.safe_load(first_compiler_yaml_raw)
            compilers_in_first_compiler_yaml = first_compiler_yaml['spack']['specs']
            if any([comp.startswith(compiler_spec) for comp in compilers_in_first_compiler_yaml]):
                site.find_system_compilers([compiler_spec])  # temporary fix until the general value of the spec can be read.
            else:
                print(f'# SPACKSITES: ERROR! first compiler {compiler_spec} in packages.yaml not in first_compiler spack environment', file=sys.stderr)

def create_env(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    config = AppConfig(args.config_file)
    Scripts.make_links(config.spd_script)  # this is repetive here but avoids use having to init the application with this before any use
    # TODO same as TODOs in site_create() above
    site = Site(os.path.join(config.spack_sites_root, args.site_name), config.initial_site_config_yaml, config.initial_site_modules_yaml,
         config.initial_site_packages_yaml, config.initial_site_repos_yaml, config.initial_site_mirrors_yaml,
         config.spd_script, config.spdsper_script,
         spack_version=config.spack_version, error_if_non_existent=True)
    specs_file = args.specs_file
    if not os.path.isabs(specs_file):
        if specs_file == 'first_compiler.yaml':
            full_specs_file = os.path.join(spacksites_dir(), config.templates_active_set, specs_file)
        else:
            full_specs_file = os.path.join(spacksites_dir(), config.templates_active_set, 'build', specs_file)
    site.create_spack_env(args.env_name, full_specs_file)

def refresh_modules(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    config = AppConfig(args.config_file)
    Scripts.make_links(config.spd_script)  # this is repetive here but avoids use having to init the application with this before any use
    site = Site(os.path.join(config.spack_sites_root, args.site_name), config.initial_site_config_yaml, config.initial_site_modules_yaml,
         config.initial_site_packages_yaml, config.initial_site_repos_yaml, config.initial_site_mirrors_yaml,
         config.spd_script, config.spdsper_script,
         spack_version=config.spack_version, error_if_non_existent=True)
    module_specs_file = args.modules_env_file
    site.refresh_modules(module_specs_file)  

def spack_setup_env_script(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    config = AppConfig(args.config_file)
    site = Site(os.path.join(config.spack_sites_root, args.site_name), config.initial_site_config_yaml, config.initial_site_modules_yaml,
         config.initial_site_packages_yaml, config.initial_site_repos_yaml, config.initial_site_mirrors_yaml,
         config.spd_script, config.spdsper_script,
         spack_version=config.spack_version, error_if_non_existent=True)
    print('# SPACKSITES: to setup spack in your shell use: eval $(spacksites spack-setup-env site-name)',  file=sys.stderr)
    print('# SPACKSITES: now issuing commands to set up your environment',  file=sys.stderr)
    print('# SPACKSITES: - these are not seen if you have eval\'ed them.',  file=sys.stderr)
    print(site.spack_setup_env_commands())

def list(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    config = AppConfig(args.config_file)
    Scripts.make_links(config.spd_script)  # this is repetive here but avoids use having to init the application with this before any use
    site_names = [dir for dir in os.listdir(config.spack_sites_root) if os.path.isdir(os.path.join(config.spack_sites_root, dir))]
    print(' '.join(site_names))

def test_message(args):
    print('# SPACKSITES: in app.py function:', inspect.stack()[0][3], file=sys.stderr)
    print('# SPACKSITES: This is a test message - so the cli parser works to get this far!', file=sys.stderr)

def run_with_cli_args():
    parser = argparse.ArgumentParser(prog='spacksites', description='Creates new spack sites and installs ARC software stack therein.')
    subparsers = parser.add_subparsers()
    parser.add_argument('-c', '--config-file', required=False, default='FIND_RELATIVE')  # TODO check that this applies the said config file

    # spacksites list 
    list_parser = subparsers.add_parser('list')
    # sites_list_parser.add_argument('-l', '-long') # TODO implement a long format
    list_parser.set_defaults(func=list)

    # spacksites create site-name
    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('site_name')
    # site_create_parser.add_argument('-p', '--parent-path', required=False) # TODO if exists create a simlink to new site in spack sites root
    create_parser.set_defaults(func=create)

    # spacksites test-message
    test_message_parser = subparsers.add_parser('test-message') 
    test_message_parser.set_defaults(func=test_message)
   
    # spacksites spack site-name spack-args
    spack_parser = subparsers.add_parser('spack')
    spack_parser.add_argument('site_name')
    spack_parser.add_argument('spack_args', type=str, nargs='+')
    spack_parser.set_defaults(func=spack)

    # spacksites install-env site-name env-name specs-file
    install_env_parser = subparsers.add_parser('install-env') 
    install_env_parser.add_argument('site_name')
    install_env_parser.add_argument('env_name')
    install_env_parser.add_argument('specs_file')
    install_env_parser.set_defaults(func=install_env)
    
    # spacksites create-env site-name env-name specs-file
    create_env_parser = subparsers.add_parser('create-env') 
    create_env_parser.add_argument('site_name')
    create_env_parser.add_argument('env_name')
    create_env_parser.add_argument('specs_file')
    create_env_parser.set_defaults(func=create_env)
    
    # spacksites refresh-modules site-name modules-env-file
    refresh_modules_parser = subparsers.add_parser('refresh-modules')
    refresh_modules_parser.add_argument('site_name')
    refresh_modules_parser.add_argument('modules_env_file')
    refresh_modules_parser.set_defaults(func=refresh_modules)
    
    # spacksites spack-setup-env site-name
    spack_setup_env_parser = subparsers.add_parser('spack-setup-env')
    spack_setup_env_parser.add_argument('site_name')
    spack_setup_env_parser.set_defaults(func=spack_setup_env_script)

    # spacksites remove-deleted

    # parse the cli arguments and do what they say
    args = parser.parse_args()
    args.func(args)

# see comment at top of file: if called with python -m spacksites,
# the function   run_with_cli_args() is called from __main__.py
if __name__ == '__main__':
    run_with_cli_args()
    
