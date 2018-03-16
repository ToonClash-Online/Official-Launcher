import subprocess
import os
import unicodedata
from string import *

from launcher_globals import *



class GameStarter():

    def __init__(self):

        if CURRENT_PLATFORM == 'Linux':
            self.python_path = PYTHON_PATH
        else:
            self.python_path = '"'+ CURRENT_PATH + PYTHON_PATH + '"'



    def launchGame(self):
        cookie = str((self.uiCallback.uName + self.uiCallback.pWord))

        if CURRENT_PLATFORM == 'Linux':
            cmd_00 = 'export ttiUsername=' + self.uiCallback.uName + ' && export ttiPassword=' + self.uiCallback.pWord + ' && export TTI_GAMESERVER=' + GAME_SERVER + ' && cd src/ && ' + self.python_path + ' -O -m toontown.toonbase.ClientStart ' + cookie
        else:
            cmd_00 = 'set ttiUsername=' + self.uiCallback.uName + ' && set ttiPassword=' + self.uiCallback.pWord + ' && set TTI_GAMESERVER=' + GAME_SERVER + ' && cd "src" && ' + self.python_path + ' -O -m toontown.toonbase.ClientStart ' + cookie

        self.uiCallback.uName = False
        self.uiCallback.pWord = False
        cookie = False

        subprocess.call(cmd_00, shell=True)

        return



