import os, shutil
import subprocess
from spacksites.src.scripts import Scripts
from spacksites.src.helpers import spacksites_dir

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
        # TODO
        # for compiler_spec in compiler_specs:
            # check that this exists as an installed package 
            
            # find the compiler path from the installed package
            
            # do a spack compiler find using  
        
        # and a general pickup
        self.run_command(['spack', 'compiler', 'find', '--scope=site'])
    
    def run_command(self, command):
        # spdsper - adds spacks dependencies to process and sets up spack in it
        command.insert(0, self.spack_setup_env_script) 
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
        # This next line is temporary, while spack fix location of temp dir for building buildcaches items - their intent is to use the build cache for ordinaryitems
        tmp_dir_command = 'export TMPDIR={}'.format(self.build_stage)
        environment_variable_command = 'export HPC_SPACK_ROOT={}'.format(os.path.dirname(spacksites_dir()))  # this environment variable is used in spack config files (repos.yaml) to point to objects in this git repo
        spack_deps_command = 'source {}\n'.format(os.path.join(Scripts.dir, self.spd_script))
        spack_setup_env_command = 'source {}\n'.format(self.spack_setup_env_script)
        return ';'.join([prompt_command, disable_user_config_command, environment_variable_command, tmp_dir_command, spack_deps_command, spack_setup_env_command])

    
    