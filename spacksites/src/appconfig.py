import os

from spacksites.src.helpers import spacksites_dir, spd_setting_key
from configparser import ConfigParser

class AppConfig():
    def __init__(self, config_file):
        if config_file == 'FIND_RELATIVE':
            self.ini_file = os.path.join(spacksites_dir(), 'settings/spack_sites.ini')
        else:
            self.ini_file = os.path.abspath(config_file)
        self.read_ini_file()
        
    def read_ini_file(self):
        config = ConfigParser()
        config.sections()
        config.read(self.ini_file)
        self.config = config
        sites_root_setting = config['general']['sites_root']
        if '{hpc_spack_root}' in sites_root_setting:
            sites_root_setting = sites_root_setting.format(hpc_spack_root=os.path.dirname(spacksites_dir()))
        self.spack_sites_root = os.path.abspath(sites_root_setting)
        self.spack_version = config['general']['spack_version']
        # TODO add the other scipts in process-env-scripts if they get used
        self.spdsper_script = config['process_env_scripts']['spdsper']
        self.spd_script = config['process_env_scripts'][spd_setting_key()]

        