import os, shutil, sys
import subprocess
from spacksites.src.scripts import Scripts
from spacksites.src.helpers import spacksites_dir
import random, string
import yaml

class Site():
    # if not using the default, user code should update Scripts.dir 
    # before instantiating any Site objects
        
    def __init__(self, dir, initial_config_yaml, initial_modules_yaml, initial_packages_yaml, initial_repos_yaml, initial_mirrors_yaml,
                 spd_script, spdsper_script,
                 spack_version=None, error_if_non_existent=False):
        if error_if_non_existent:
            if not os.path.exists(dir):
                raise FileNotFoundError
        self.dir = dir
        self.spd_script = spd_script
        self.spdsper_script = spdsper_script
        self.name = os.path.basename(dir)
        self.build_stage = os.path.join(dir, 'build_stage')  # TODO this is out of date it is now in site's config.yaml; it os only used below for the making dirs but does the build stage dir need to exist before spack uses it?
        self.yaml_dir = os.path.join(self.dir, 'spack', 'etc', 'spack')
        self.provenance = os.path.join(dir, 'provenance')  # TODO make some records in here 
        self.spack_setup_env_script = os.path.join(dir, 'spack', 'share', 'spack', 'setup-env.sh')
        self.spack_version = spack_version
        if not os.path.exists(dir):
            self.make_dirs()
        if not os.path.exists(os.path.join(dir,'spack', 'README.md')):
            self.clone_spack()
            self.configure_spack(initial_config_yaml, initial_modules_yaml, initial_packages_yaml, initial_repos_yaml, initial_mirrors_yaml)
            self.find_system_compilers()  # this should find the system compilers
        config_yaml_raw, err = self.run_commands(['spack config --scope=site get config'])
        config_yaml = yaml.safe_load(config_yaml_raw)
        build_stage_raw = config_yaml['config']['build_stage']
        self.build_stage = build_stage_raw.replace('$spack', os.environ['SPACK_ROOT'])
        print('# SPACKSITES: site.build_stage set to: ', self.build_stage, file=sys.stderr)

    
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

    def configure_spack(self, initial_config_yaml, initial_modules_yaml, initial_packages_yaml, initial_repos_yaml, initial_mirrors_yaml):
        shutil.copy(initial_config_yaml, os.path.join(self.yaml_dir, 'config.yaml'))
        shutil.copy(initial_modules_yaml, os.path.join(self.yaml_dir, 'modules.yaml'))
        shutil.copy(initial_packages_yaml, os.path.join(self.yaml_dir, 'packages.yaml'))
        shutil.copy(initial_repos_yaml, os.path.join(self.yaml_dir, 'repos.yaml'))
        # site will need a key to sign packages - this is a for now fix - TODO may want to import the same keys to all sites, also 'ARCHPCSolutions', 'rc-support@ucl.ac.uk' are magic numbers - remove to a settings file
        self.run_command(['spack', 'gpg', 'create', 'ARCHPCSolutions', 'rc-support@ucl.ac.uk'])
        # 2 steps to use the common build cache - thw first, a config copy, links it into this site as spack mirror
        shutil.copy(initial_mirrors_yaml, os.path.join(self.yaml_dir, 'mirrors.yaml'))    
        self.run_command(['spack', 'buildcache', 'keys', '--install', '--trust'])
    
    def find_system_compilers(self, compiler_specs=[]):
        if len(compiler_specs) > 0:
            for compiler_spec in compiler_specs:
                self.run_commands(['spack load {}'.format(compiler_spec), 'spack compiler find --scope=site'])    # these commands: loads + find, need to be in same spack process context 
        else:
            # or a general round up - also needed for when compiler_specs=[]
            self.run_command(['spack', 'compiler', 'find', '--scope=site'])    
         
    def run_command(self, command): # command is a list of words of the command
        # spdsper - adds spacks dependencies to process and sets up spack in it
        command.insert(0, self.spack_setup_env_script) 
        Scripts.spdsper(command)
    
    # this is different to run_command() in that it executes several commands and does so so that they are in the same process
    # the need was for spack load gcc@21; spack compiler find - i.e. the compiler needs to be loaded in the process for spack to find it
    def run_commands(self, commands):  # commands is a list of command lines (no newlines)
        commands.insert(0, 'source  {}'.format(self.spack_setup_env_script))
        return Scripts.spdsperscript(commands, self.spd_script)
    
    # here 'env' means one of spacks environments, a collection of spack specs, 
    # and not the shell environment in which spack commands are run.
    def install_spack_env(self, spack_env_name, spack_env_filename):        
        self.run_command(['spack', 'env', 'create', spack_env_name, spack_env_filename])
        self.run_command(['spack', '-e', spack_env_name, 'install'])
        
    def create_spack_env(self, spack_env_name, spack_env_filename):
        self.run_command(['spack', 'env', 'create', spack_env_name, spack_env_filename])
        
    def refresh_modules(self, spack_env_filename):
        choices = string.ascii_uppercase
        tmp_env_name = 'MODENV_' + ''.join(random.choice(choices) for _ in range(6))
        self.run_command(['spack', 'env', 'create', tmp_env_name, spack_env_filename])
        self.run_command(['spack', '-e', tmp_env_name, 'concretize'])
        self.run_command(['spack', '-e', tmp_env_name, 'module', 'tcl', 'refresh', '-y', '--delete-tree'])
        self.run_command(['spack', 'env', 'remove', '-y', tmp_env_name])      
        
    
    def spack_setup_env_commands(self):
        prompt_command = 'export PS1="(spacksite: {}) $PS1"'.format(self.name)
        disable_user_config_command = 'export SPACK_DISABLE_LOCAL_CONFIG=1'  # so that the operator's personal user scope spack config is ignored
        # This next line is temporary, while spack fix location of temp dir for building buildcaches items - their intent is to use the build cache for ordinaryitems
        tmp_dir_command = 'export TMPDIR={}'.format(self.build_stage)
        environment_variable_command = 'export HPC_SPACK_ROOT={}'.format(os.path.dirname(spacksites_dir()))  # this environment variable is used in spack config files (repos.yaml) to point to objects in this git repo
        spack_deps_command = 'source {}\n'.format(os.path.join(Scripts.dir, self.spd_script))
        spack_setup_env_command = 'source {}\n'.format(self.spack_setup_env_script)
        return ';'.join([prompt_command, disable_user_config_command, environment_variable_command, tmp_dir_command, spack_deps_command, spack_setup_env_command])

    
    