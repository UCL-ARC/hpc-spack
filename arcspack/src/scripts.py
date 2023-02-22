import os
import sys
import subprocess
from arcspack.src.helpers import arcspack_dir

class Scripts():
    dir = os.path.join(arcspack_dir(), 'process-env-scripts')
    
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
        print('# ARCKPSACK: Now calling: ', ' '.join(args), file=sys.stderr)
        subprocess.run(args)
        