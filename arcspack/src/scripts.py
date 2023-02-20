import os
import subprocess

class Scripts():
    # TODO copy shell scripts to a dir env-scripts in arcpack/
    dir = os.path.dirname(os.path.abspath(__file__))
    
    @classmethod
    def spdsper(cls, args):
        # TODO update path used here to pick up the scritps config from AppConfig
        print("Scripts.dir", Scripts.dir)  # debug
        subprocess.run(args.insert(0, os.path.join(Scripts.dir, 'spdsper')))
        