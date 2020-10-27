from PyQt5 import QtCore, QtGui, QtWidgets

def prevBtnHandler(self):

    if(str(self.AlgoSelector.currentText()) == "FCFS"):
        self.prevFCFS()
    elif(str(self.AlgoSelector.currentText()) == "SJF"):
        self.prevSJF()
    elif(str(self.AlgoSelector.currentText()) == "SRTF"):
        self.prevSRTF()
    elif(str(self.AlgoSelector.currentText()) == "RR"):
        self.prevRR()
    elif(str(self.AlgoSelector.currentText()) == "LJF"):
        self.prevLJF()
    elif(str(self.AlgoSelector.currentText()) == "LRTF"):
        self.prevLRTF()
    elif(str(self.AlgoSelector.currentText()) == "Priority"):
        self.prevPriority()