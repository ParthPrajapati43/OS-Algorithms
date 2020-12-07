from PyQt5 import QtCore, QtGui, QtWidgets

def pauseBtnHandler(self):
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