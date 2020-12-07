from PyQt5 import QtCore, QtGui, QtWidgets

def nextBtnHandler(self):

    if(self.TypeWithoutIOBT.isChecked()):
        self.nextNotIOBT()
    else:
        self.nextIOBT()