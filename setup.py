"""
utiliser : python setup.py build pour compiler.
"""

import os
import sys

import PySide
import PySide.uic
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

importationCode=[]


dependances = ["cours/","qcm/","qcmrm/","toeic/","users/"]

#QWEB
includefiles = ["res_rc.py","resUsr_rc.py","resPref_rc.py","resLevel_rc.py",(os.path.join(os.path.dirname(PyQt4.uic.__file__),
"widget-plugins"), "PyQt4.uic.widget-plugins")]+importationCode+dependances
#QWEB!

includes = ["PyQt4.QtNetwork"]
excludes = []
packages = ["encodings",
            "OpenGL",
            "OpenGL.arrays" # or just this one
            ]
#
setup(
    name = "Learning",
    version = "0.2",
    description = "Learning",
    executables = [Executable("Ui_main.py", base = base)],
    options = {'build_exe': {'excludes':excludes,"compressed":True,
                             'packages':packages,'include_files':includefiles,
                             "includes":includes}}
    )
