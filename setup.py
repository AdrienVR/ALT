"""
utiliser : python setup.py build pour compiler.
"""

import os
import sys

import PyQt4
import PyQt4.uic
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

importationCode=[]

dependances = ["cours/","qcm/","qcmrm/","toeic/","users/", "dep"]

icone = [r"dep/img/1-48.ico"]

#QWEB
includefiles = ["res_rc.py","resUsr_rc.py","resPref_rc.py","resLevel_rc.py",(os.path.join(os.path.dirname(PyQt4.uic.__file__),
"widget-plugins"), "PyQt4.uic.widget-plugins")]+importationCode+dependances+icone
#QWEB!

includes = ["PyQt4.QtNetwork"]
excludes = []
packages = ["encodings",
            "OpenGL",
            "OpenGL.arrays" # or just this one
            ]

targetDir = "./build/"
 
setup(
    name = "Assimilation Learning Tool",
    author = "Adrien Vernotte",
    version = "0.5",
    description = "Outil d'entrainement au TOEIC - LGPL v2.1",
    executables = [Executable("Assimilator.py",
                                base = base,
#                                 shortcutName="LearningTool",
#                                 shortcutDir="DesktopFolder",
#                                 targetDir=targetDir,
                                icon = icone[0]
                              )],
    options = {'build_exe': {'excludes':excludes,"compressed":True,
                             'packages':packages,'include_files':includefiles,
                             "includes":includes}
               }
    )
