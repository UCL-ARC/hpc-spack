import os
import sys
import subprocess
from spacksites.src.helpers import spacksites_dir

class Scripts():
    dir = os.path.join(spacksites_dir(), 'process-env-scripts')
    
    @classmethod
    def make_links(cls, spd_script):
        target = os.path.join(Scripts.dir, spd_script)
        spd_link = os.path.join(Scripts.dir, 'spd')
        try:
            os.remove(spd_link)
        except FileNotFoundError:
            pass  # not a problem
        os.symlink(target, spd_link)
    
    @classmethod
    def spdsper(cls, args):
        _ = args.insert(0, os.path.join(Scripts.dir, 'spack-deps-spack-env-run.sh'))
        # _ = args.insert(0, 'SPACK_DISABLE_LOCAL_CONFIG=1')  # this disables the users own config   - TODO fix how to set env var for python subprocess    
        # command_env = os.environ.copy()
        # command_env['SPACK_DISABLE_LOCAL_CONFIG'] = 1
        print('# SPACKSITES: Now calling: ', ' '.join(args), file=sys.stderr)
        subprocess.run(args)
        