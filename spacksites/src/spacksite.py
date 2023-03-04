import os, shutil
import subprocess
from spacksites.src.scripts import Scripts

class Site():
    # if not using the default, user code should update Scripts.dir 
    # before instantiating any Site objects
        
    def __init__(self, dir, initial_config_yaml, initial_modules_yaml, initial_packages_yaml, 
                 spack_version=None, error_if_non_existent=False):
        if error_if_non_existent:
            if not os.path.exists(dir):
                raise FileNotFoundError
        self.dir = dir
        self.name = os.path.basename(dir)
        self.build_stage = os.path.join(dir, 'build_stage')
        self.yaml_dir = os.path.join(self.dir, 'spack', 'etc', 'spack')
        self.provenance = os.path.join(dir, 'provenance')  # TODO make some records in here 
        self.spack_setup_env = os.path.join(dir, 'spack', 'share', 'spack', 'setup-env.sh')
        self.spack_version = spack_version
        if not os.path.exists(dir):
            self.make_dirs()
        if not os.path.exists(os.path.join(dir,'spack', 'README.md')):
            self.clone_spack()
            self.configure_spack(initial_config_yaml, initial_modules_yaml, initial_packages_yaml)
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

    def configure_spack(self, initial_config_yaml, initial_modules_yaml, initial_packages_yaml):
        shutil.copy(initial_config_yaml, os.path.join(self.yaml_dir, 'modules.yaml'))
        shutil.copy(initial_modules_yaml, os.path.join(self.yaml_dir, 'modules.yaml'))
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
        self.run_command(['spack', 'compiler', 'find', '--scope=site'])
    
    def run_command(self, command):
        # spdsper - adds spacks dependencies to process and sets up spack in it
        command.insert(0, self.spack_setup_env) 
        Scripts.spdsper(command)
    
    # here 'env' means one of spacks environments, a collection of spack specs, 
    # and not the shell environment in which spack commands are run.
    def install_spack_env(self, spack_env_name, spack_env_filename):        
        self.run_command(['spack', 'env', 'create', spack_env_name, spack_env_filename])
        self.run_command(['spack', '-e', spack_env_name, 'install'])
        
    def create_modules(self, spack_env_filename):
        self.run_command(['spack', 'module', 'tcl', 'refresh', '--delete-tree'])
        
        # TODO
        pass
    
    def spack_setup_env_commands(self):
        prompt_command = 'export PS1="(spacksite: {}) $PS1"'.format(self.name)
        disable_user_config_command = 'export SPACK_DISABLE_LOCAL_CONFIG=1'  # so that the operator's personal user scope spack config is ignored
        spack_setup_env_command = 'source {}\n'.format(self.spack_setup_env)
        return ';'.join([prompt_command, disable_user_config_command, spack_setup_env_command])

    
    