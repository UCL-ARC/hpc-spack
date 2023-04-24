import os
import sys
import subprocess
from spacksites.src.helpers import spacksites_dir
from spacksites.src.appconfig import AppConfig

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
        print('# SPACKSITES: Now calling: ', ' '.join(args), file=sys.stderr)
        subprocess.run(args)
        
    @classmethod
    def spdsperscript(cls, script, spd_script):
        script.insert(0, "source {}\n".format(os.path.join(Scripts.dir, spd_script)))
        script = '\n'.join(script)
        print('# SPACKSITES: Now calling: #######\n', script, file=sys.stderr)
        print('# SPACKSITES: ####################',file=sys.stderr)
        p = subprocess.Popen('bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out, err = p.communicate(script.encode('utf-8'))
        return out, err
        