import os
import subprocess
from spacksites.src.scripts import Scripts

class Site():
    # if not using the default, user code should update Scripts.dir 
    # before instantiating any Site objects
        
    def __init__(self, dir, spack_version=None, error_if_non_existent=False):
        if  error_if_non_existent:
            if not os.path.exists(dir):
                raise FileNotFoundError
        self.dir = dir
        self.build_stage = os.path.join(dir, 'build_stage')
        self.provenance = os.path.join(dir, 'provenance')
        self.spack_setup_env = os.path.join(dir, 'spack', 'share', 'spack', 'setup-env.sh')
        self.spack_version = spack_version
        if not os.path.exists(dir):
            self.make_dirs()
        if not os.path.exists(os .path.join(dir,'spack', 'README.md')):
            self.clone_spack()
            self.configure_spack()
        # TODO test that spack's dependency compiler(s) have been configured
        # if not configure them
    
    # TODO split into  directories, clone spack, basic spack config, identify compiler (or just set conig)        
    # def _create(self, spack_version):
    
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

    def configure_spack(self):
        # set site config
        self.run_command(['spack', 'config', '--scope=site', 'add', 'config:build_stage:{}'.format(self.build_stage)])
        # 6 is a conservative number (for make -j), for testing on login nodes
        self.run_command(['spack', 'config', '--scope=site', 'add', 'config:build_jobs:{}'.format(6)])
        # TODO add more site config for build caches, mirrors(source caches), ready for installing specs, but first identify the compiler
    
    def configure_spack_dependency_compiler():
        pass
    
    def run_command(self, command):
        # spdsper - adds spacks dependencies to process and sets up spack in it
        # TODO fix TypeError: spdsper() takes 1 positional argument but 2 were given
        # why is this interpreted as 2 args - is command wrong type (supposed to be a list)
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
    
    