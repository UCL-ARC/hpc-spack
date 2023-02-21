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
        sites_root_setting = config['general']['sites_root']
        if '{hpc_spack_root}' in sites_root_setting:
            sites_root_setting = sites_root_setting.format(hpc_spack_root=os.path.dirname(arcspack_dir()))
        self.spack_sites_root = os.path.abspath(sites_root_setting)
        self.spack_version = config['general']['spack_version']
        # TODO add the other scipts in process-env-scripts if they get used
        self.spdsper_script = config['process_env_scripts']['spdsper']

        