"""
utiliser : python setup.py build pour compiler.
"""

import os
import sys

import PySide
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

importationCode=[]


dependances = ["cours/","qcm/","qcmrm/","toeic/","users/"]

#QWEB
includefiles = ["res_rc.py","resUsr_rc.py","resPref_rc.py","resLevel_rc.py"]+importationCode+dependances
#QWEB!

includes = []
excludes = []
packages = ["encodings",
            "OpenGL",
            "OpenGL.arrays" # or just this one
            ]
#
setup(
    name = "Learning",
    version = "0.3",
    description = "Learning",
    executables = [Executable("Ui_main.py", base = base)],
    options = {'build_exe': {'excludes':excludes,"compressed":True,
                             'packages':packages,'include_files':includefiles,
                             "includes":includes}}
    )
