'''

Currently using PyInstall not this setup.py

'''


import py2exe
from distutils.core import setup
import sys, os
import zmq
sys.argv.append('py2exe')
os.environ["PATH"] = \
    os.environ["PATH"] + \
    os.path.pathsep + os.path.split(zmq.__file__)[0]
setup(
    name='reVEmind',
    version='1',
    console=['reVEmind/reVEmind.py'],
    url='https://github.com/Proc3ss/reVEmind/',
    license='MIT',
    author='proC3ss',
    author_email='proc3sselevated@gmail.com',
    description='Eve Online Combat Log Analyzer',
    packages=['reVEmind', 'reVEmind.ui', 'reVEmind.classes'],
    data_files = [('sqldrivers', ('C:\Python27\Lib\site-packages\PyQt4\plugins\sqldrivers\qsqlite4.dll',))],
)
