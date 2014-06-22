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

dependances = ["cours/","qcm/","qcmrm/","toeic/","users/","dep/"]
#["res_rc.py","resUsr_rc.py","resPref_rc.py","resLevel_rc.py"]

includefiles = importationCode+dependances

includes = []
excludes = []
packages = ["encodings"]

setup(
    name = "Learning",
    version = "0.3",
    description = "Learning",
    executables = [Executable("Assimilator.py", base = base)],
    options = {'build_exe': {'excludes':excludes,"compressed":True,
                             'packages':packages,'include_files':includefiles,
                             "includes":includes}}
    )
