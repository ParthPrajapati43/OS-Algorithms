from PyQt5 import QtCore, QtGui, QtWidgets

def prevBtnHandler(self):
    
    if(self.TypeWithoutIOBT.isChecked()):
        self.prevNotIOBT()
    else:
        self.prevIOBT()