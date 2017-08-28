# -*- coding: utf-8 -*-

import os  
import sys  
def mkDir(dirName):  
    dirpath = os.path.join(sys.path[0], dirName)  
    if not os.path.exists(dirpath):  
        os.mkdir(dirpath)  
    return dirpath  
SAVE_PATH = mkDir(goal_path)


