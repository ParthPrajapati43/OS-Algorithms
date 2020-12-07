from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess

def helpBtnHandler(self):
    
    fileadd = os.path.realpath(__file__)
    abspath = os.path.dirname(fileadd)
    abspath = abspath[:-(12)]
    openfile = str(abspath)+'\\README.pdf'
    subprocess.Popen([openfile],shell=True)
    openfile = str(abspath)+'\\ALGORITHMS.pdf'
    subprocess.Popen([openfile],shell=True)