import os
from inspect import getsourcefile
import sys


def directory_open():
    """ Открывает папку, со скаченными изображениями"""
    commands_dir = {'linux': "xdg-open ",
                    'win32': "start "}
    p = os.path.abspath(getsourcefile(lambda: 0))
    p = os.path.join(p[:-31] + 'pictures')
    try:
        ans = int(input("Do you want to open a folder with files? 1 - Yes, "
                        "2 - No: "))
    except (Exception, KeyboardInterrupt):
        return "Error in function input"
    else:
        if ans == 1:
            try:
                os.system(commands_dir[sys.platform] + p)
            except (Exception, KeyboardInterrupt):
                return "Error in function os.system"
        elif ans == 2:
            return "Done!"
        else:
            return "The program ended without opening the folder"
