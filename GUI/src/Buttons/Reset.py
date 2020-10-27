from PyQt5 import QtCore, QtGui, QtWidgets

# Reset Button Handler

def resetBtnHandler(self):
    c = self.JobTable.columnCount()
    c = int(c)
    r = self.JobTable.rowCount()
    r = int(r)
    for i in range(r):
        for j in range(c):
            item = QtWidgets.QTableWidgetItem()
            item.setText("")
            self.JobTable.setItem(i,j,item)
    
    self.CGTableJobs = []
    self.CGTableTimer = []
    self.GanttChartTable.setColumnCount(0)
    self.JobQueue.setColumnCount(0)
    self.ReadyQueue.setColumnCount(0)
    self.CPU.setColumnCount(0)
    self.TerminatedQueue.setColumnCount(0)
    self.IODevice.setColumnCount(0)
    self.IOQueue.setColumnCount(0)
    self.TimerLabel.setText("00")
    self.ScheduleProgressBar.setValue(0)
    self.AvgTAT.setText("")
    self.AvgWT.setText("")
    self.AvgRT.setText("")
    self.latestTimer = 0
    self.latestTimerStart = 0
    self.myATlist = []
    self.myBTlist = []
    self.myjobNumber = []
    self.myJobDetails = []
    self.myTimer = 0
    self.totalTimeOfExecuting = 0
    self.currTimer = 0
    self.storedJobQueue = []
    self.storedReadyQueue = []
    self.storedCPU = []
    self.storedTerminatedQueue = []