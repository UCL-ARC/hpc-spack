import os
import platform
import subprocess

def spacksites_dir():
    # TODO make more portable - path delims other tham '/' - chech pathlib module
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)).rstrip('/'))
    
# def stack_workflow_app_dir():
#     return os.path.dirname(spacksites_dir())

# def stack_workflow_config(ini_file="FIND_RELATIVE"):
#     if ini_file == 'FIND_RELATIVE':
        
def os_ver():
    platform_system =  platform.system()
    platform_release = platform.release()
    if platform_system == 'Linux':
        completed_process = subprocess.run(['cat', '/etc/os-release'], capture_output=True)
        lines = [line for line in completed_process.stdout.decode('utf-8').split('\n') if '=' in line]
        linux_os_release = {pair[0]: pair[1].strip('"') for pair in [item.split('=') for item in lines]}
        return 'Linux', linux_os_release['ID'], linux_os_release['VERSION_ID']
    elif platform_system == 'Windows':
        return 'Windows', 'NONE', platform_release
    else:
        return 'default', 'default', 'default'
    
def spd_setting_key():
    my_os = os_ver()
    if my_os[0] == 'default':
        return 'spd_default'
    else:
        return 'spd_' + '_'.join(my_os)

def packages_setting_key():
    my_os = os_ver()
    if my_os[0] == 'default':
        return 'packages_default'
    else:
        return 'packages_' + '_'.join(my_os)
