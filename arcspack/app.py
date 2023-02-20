#!/usr/bin/env python3
import os, sys

# while this file can be run via: python -m arcspack <command args>,
# this PYTHONPATH manipulation allows this file to be run directly 
# which might be of help when pointing a debugger at it.
if __name__ == '__main__':
    # TODO test next line - does it need parent of parent?
    print('Adding ',  os.path.dirname(os.path.abspath('__FILE__')), ' to PYTHONPATH')
    sys.path.append(os.path.dirname(os.path.abspath('__FILE__')))

import argparse

from arcspack.src.spacksite import Site
from arcspack.src.helpers import arcspack_dir
from arcspack.src.appconfig import AppConfig

# for debuging
import inspect

# functions to carry out actions specified by cli arguments - args is the parsed arguments
# to do - factor out passing on args to base functions

def site_create(args):
    print(inspect.stack()[0][3])
    config = AppConfig(args.config_file)
    # TODO allow for sites outside spack_sites_root e.g. by testing site name for being an absolute path
    # TODO consider site_name in the form abc/def
    # TODO validate characters in site_name
    # the new site object is dropped here because this is the end of the command
    # if a REPL is added to the project will need to pick it up for the REPL's state
    Site(os.path.join(config.spack_sites_root, args.site_name), config.spack_version)

def site_install_env(args):
    print(inspect.stack()[0][3])
    config = AppConfig(args.config_file)
    # TODO same as TODOs in site_create() above
    site = Site(os.path.join(config.spack_sites_root, args.site_name), config.spack_version)
    # TODO install the spack specs in the site 

def site_spack_setup_env_script(args):
    print(inspect.stack()[0][3])
    pass 

def sites_list(args):
    print(inspect.stack()[0][3])
    pass 

def site_create_test_message(args):
    print('This is a test message - so the cli parser works to get this far!')

def run_with_cli_args():
    parser = argparse.ArgumentParser(prog='arcspack', description='Creates new spack sites and installs ARC software stack therein.')
    subparsers = parser.add_subparsers()
    # parser.add_help = True

    # arcspack site
    site_parser = subparsers.add_parser('site')
    site_subparsers = site_parser.add_subparsers()

    # arcspack site test-message
    site_test_message_parser = site_subparsers.add_parser('test-message') 
    site_test_message_parser.set_defaults(func=site_create_test_message)
        
    # arcspack site create ...
    site_create_parser = site_subparsers.add_parser('create')
    site_create_parser.add_argument('site_name')
    site_create_parser.add_argument('-p', '--path', required=False)
    site_create_parser.add_argument('-c', '--config-file', required=False, default='FIND_RELATIVE')
    site_create_parser.set_defaults(func=site_create)

    # arcspack site install-env ...
    site_install_env_parser = site_subparsers.add_parser('install-env') 
    site_install_env_parser.add_argument('env-name')
    site_install_env_parser.add_argument('specs-file')
    site_install_env_parser.set_defaults(func=site_install_env)

    # arcspack site spack-setup-env ...
    site_spack_setup_env_parser = site_subparsers.add_parser('spack-setup-env')
    site_spack_setup_env_parser.add_argument('site-name')
    site_spack_setup_env_parser.set_defaults(func=site_spack_setup_env_script)

    # arcspack site lock ...

    # arcspack site spack-command ...

    # arcspack sites
    sites_parser = subparsers.add_parser('sites')
    sites_subparsers = sites_parser.add_subparsers()

    # arcspack sites list ...
    sites_list_parser = sites_subparsers.add_parser('list')
    sites_list_parser.add_argument('-l', '-long')
    sites_list_parser.set_defaults(func=sites_list)

    # arcspack sites remove-deleted

    # parse the cli arguments and do what they say
    args = parser.parse_args()
    args.func(args)

# see comment at top of file: if called with python -m arcspack,
# the function   run_with_cli_args() is called from __main__.py
if __name__ == '__main__':
    run_with_cli_args()
    