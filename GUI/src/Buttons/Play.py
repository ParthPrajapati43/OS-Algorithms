from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest

def playBtnHandler(self):
    self.isPause = False
    self.NextBtn.setEnabled(False)
    self.PrevBtn.setEnabled(False)
    self.AlgoSelector.setEnabled(False)
    self.ModeNonPreemptive.setEnabled(False)
    self.ModePreemptive.setEnabled(False)
    self.TypeWithoutIOBT.setEnabled(False)
    self.TypeWithIOBT.setEnabled(False)
    self.ContextSwitchSelector.setEnabled(False)
    self.TimeQuantumSelector.setEnabled(False)
    self.JobNo.setEnabled(False)
    self.GoBtn.setEnabled(False)
    self.ImportBtn.setEnabled(False)
    self.ResetBtn.setEnabled(False)
    self.SolveBtn.setEnabled(False)
    self.GraphBtn.setEnabled(False)
    self.DownloadBtn.setEnabled(False)

    
    for _ in range(self.currTimer, len(self.CGTableJobs)+1):
        if(self.isPause):
            break
        self.nextBtnHandler()
        QtTest.QTest.qWait(1000)
    self.isPause = True
    self.NextBtn.setEnabled(True)
    self.PrevBtn.setEnabled(True)
    self.AlgoSelector.setEnabled(True)
    self.ModeNonPreemptive.setEnabled(True)
    self.ModePreemptive.setEnabled(True)
    self.TypeWithoutIOBT.setEnabled(True)
    self.TypeWithIOBT.setEnabled(True)
    self.ContextSwitchSelector.setEnabled(True)
    self.TimeQuantumSelector.setEnabled(True)
    self.JobNo.setEnabled(True)
    self.GoBtn.setEnabled(True)
    self.ImportBtn.setEnabled(True)
    self.ResetBtn.setEnabled(True)
    self.SolveBtn.setEnabled(True)
    self.GraphBtn.setEnabled(True)
    self.DownloadBtn.setEnabled(True)