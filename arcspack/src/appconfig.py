import os

from arcspack.src.helpers import arcspack_dir
from configparser import ConfigParser

class AppConfig():
    def __init__(self, config_file):
        # TODO refactor parameter args to config_file
        if config_file == 'FIND_RELATIVE':
            self.ini_file = os.path.join(arcspack_dir(), 'settings/periodic_spack_site_generation.ini')
        else:
            self.ini_file = os.path.abspath(config_file)
        # DEBUG print(ini_file)
        self.read_ini_file()
        
    def read_ini_file(self):
        config = ConfigParser()
        config.sections()
        config.read(self.ini_file)
        self.config = config
        self.spack_sites_root = os.path.abspath(config['general']['sites_root'])
        self.spack_version = config['general']['spack_version']
        # TODO add the other scipts in process-env-scripts if they get used
        self.spdsper_script = config['process_env_scripts']['spdsper']

        