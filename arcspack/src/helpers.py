import os

def arcspack_dir():
    # TODO make more portable - path delims other tham '/' - chech pathlib module
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)).rstrip('/'))
    
# def stack_workflow_app_dir():
#     return os.path.dirname(arcspack_dir())

# def stack_workflow_config(ini_file="FIND_RELATIVE"):
#     if ini_file == 'FIND_RELATIVE':
        
