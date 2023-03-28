import os

from spacksites.src.helpers import spacksites_dir, spd_setting_key, packages_setting_key
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
        sites_root_setting = self._subst_setting(config['general']['sites_root'])
        self.spack_sites_root = os.path.abspath(sites_root_setting)
        self.spack_version = config['general']['spack_version']
        # TODO add the other scipts in process-env-scripts if they get used
        self.spdsper_script = self._subst_setting(config['process_env_scripts']['spdsper'])
        self.spd_script = self._subst_setting(config['process_env_scripts'][spd_setting_key()])

        self.initial_site_config_yaml = self._subst_setting(config['initial_site_configs']['config_default'])
        self.initial_site_modules_yaml = self._subst_setting(config['initial_site_configs']['modules_default'])
        self.initial_site_repos_yaml = self._subst_setting(config['initial_site_configs']['repos_default'])
        self.initial_site_mirrors_yaml = self._subst_setting(config['initial_site_configs']['mirrors_default'])
        self.initial_site_packages_yaml = self._subst_setting(config['initial_site_configs'][packages_setting_key()])
        self.templates_active_set = self._subst_setting(config['spack_env_templates']['active_set'])
        self.site_archive_root = self._subst_setting(config['spack_env_templates']['archive_root'])

    def _subst_setting(self, raw_setting):
        if '{hpc_spack_root}' in raw_setting:
            return raw_setting.format(hpc_spack_root=os.path.dirname(spacksites_dir()))
        else:
            return raw_setting
        # could add here any further subsitutions that arise