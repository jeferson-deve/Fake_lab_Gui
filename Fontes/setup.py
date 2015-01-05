'''
from cx_Freeze import setup, Executable



setup(
    name='Interface_Gui',
    version='1.0.10',
    description='Gerar resultados de analises',
    executables=[Executable('Interface.py')],
    author='Jeferson de souza',
    author_email='mp_bra_nco@hotmail.com',

)


import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Fake_lab",
        version = "1.0.11",
        description = "Gerador de Analises",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Interface.py", base=base)])

from distutils.core import setup
import py2exe
# para usar $python setup.py py2exe
setup(console=['Interface.py'])

'''

import esky.bdist_esky
from distutils.core import setup

setup(
    name="Fake Lab",
    version="2.5",
    scripts=["Interface.py"],
    requires=['esky', 'cx_Freeze', 'Tkinter']
)