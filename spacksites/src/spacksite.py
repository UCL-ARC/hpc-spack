import os, shutil
import subprocess
from spacksites.src.scripts import Scripts

class Site():
    # if not using the default, user code should update Scripts.dir 
    # before instantiating any Site objects
        
    def __init__(self, dir, initial_config_yaml, initial_packages_yaml, 
                 spack_version=None, error_if_non_existent=False):
        if error_if_non_existent:
            if not os.path.exists(dir):
                raise FileNotFoundError
        self.dir = dir
        self.build_stage = os.path.join(dir, 'build_stage')
        self.yaml_dir = os.path.join(self.dir, 'spack', 'etc', 'spack')
        self.provenance = os.path.join(dir, 'provenance')
        self.spack_setup_env = os.path.join(dir, 'spack', 'share', 'spack', 'setup-env.sh')
        self.spack_version = spack_version
        if not os.path.exists(dir):
            self.make_dirs()
        if not os.path.exists(os.path.join(dir,'spack', 'README.md')):
            self.clone_spack()
            self.configure_spack(initial_config_yaml, initial_packages_yaml)
            self.find_system_compilers()
    
    def make_dirs(self):
        os.makedirs(self.dir)
        os.mkdir(self.build_stage)
        os.mkdir(self.provenance)
        
    def clone_spack(self):
        # clone spack from github
        current_dir = os.getcwd()
        os.chdir(self.dir)
        subprocess.run(['git', 'clone', '-c', 'feature.manyFiles=true', 
                        '--branch', self.spack_version, 'https://github.com/spack/spack.git'])
        os.chdir(current_dir)

    def configure_spack(self, initial_config_yaml, initial_packages_yaml):
        with open(initial_config_yaml, 'r') as f1:
            lines = f1.readlines()
        # substitue for {{build_stage}}
        lines = [line.replace('{{build_stage}}', self.build_stage) if '{{build_stage}}' in line else line for line in lines]
        with open(os.path.join(self.yaml_dir, 'config.yaml'), 'w') as f2:
            f2.writelines(lines)
        # TODO copy the packages yaml
        shutil.copy(initial_packages_yaml, os.path.join(self.yaml_dir, 'packages.yaml'))
        
        # # TODO just make this a copy of config.yaml from template folder (settings/) to $(site prefix)/etc/spack/ and subst in any placeholders 
        # # template config.yaml file chosen per OS etc to allow easy development? yes packages.
        # # TODO repeat for other config files - e.g. packages 
        # # set site config
        # self.run_command(['spack', 'config', '--scope=site', 'add', 'config:build_stage:{}'.format(self.build_stage)])
        # # 6 is a conservative number (for make -j), for testing on login nodes
        # self.run_command(['spack', 'config', '--scope=site', 'add', 'config:build_jobs:{}'.format(6)])
        # # TODO add more site config for build caches, mirrors(source caches), ready for installing specs, but first identify the compiler
    
    def find_system_compilers(self):
        self.run_command(['spack', 'compiler', 'find'])

    def add_upstream_sites(self, site_names):
        # use std spack commands but work out paths to them based on site names.
        pass

    def show_upstream_sites(self): # <- this function does not belong on a site object - move to app
        pass # follow the links a print a dot graph

    def build_first_complier():
        pass # pick compiler as first in packages default and build that - chat to user about what you are doing.  
        # or chat includes info that first compiler could be built by installing an env
    
    def run_command(self, command):
        # spdsper - adds spacks dependencies to process and sets up spack in it
        command.insert(0, self.spack_setup_env)        
        Scripts.spdsper(command)
    
    # here 'env' means one of spacks environments, a collection of spack specs, 
    # and not the shell environment in which spack commands are run.
    def install_spack_env(self, spack_env, spack_specs_filename):        
        self.run_command(['spack', 'env', 'create', spack_env, spack_specs_filename])
        self.run_command(['spack', '-e', spack_env, 'install'])
        
    def create_modules(self, module_dir, spack_env, spack_specs_filename):
        # TODO
        pass
    
    