from PyQt5 import QtCore, QtGui, QtWidgets

def nextBtnHandler(self):

    if(str(self.AlgoSelector.currentText()) == "FCFS"):
        self.nextFCFS()
    elif(str(self.AlgoSelector.currentText()) == "SJF"):
        self.nextSJF()
    elif(str(self.AlgoSelector.currentText()) == "SRTF"):
        self.nextSRTF()
    elif(str(self.AlgoSelector.currentText()) == "RR"):
        self.nextRR()
    elif(str(self.AlgoSelector.currentText()) == "LJF"):
        self.nextLJF()
    elif(str(self.AlgoSelector.currentText()) == "LRTF"):
        self.nextLRTF()
    elif(str(self.AlgoSelector.currentText()) == "Priority"):
        self.nextPriority()
    
    