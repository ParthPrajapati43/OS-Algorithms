from PyQt5 import QtCore, QtGui, QtWidgets

def solveBtnHandler(self):

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
    self.storedPercentage = []
    self.storedState = []

    if(str(self.AlgoSelector.currentText()) == "FCFS"):
        self.solveFCFS()
    elif(str(self.AlgoSelector.currentText()) == "SJF"):
        self.solveSJF()
    elif(str(self.AlgoSelector.currentText()) == "SRTF"):
        self.solveSRTF()
    elif(str(self.AlgoSelector.currentText()) == "RR"):
        self.solveRR()
    elif(str(self.AlgoSelector.currentText()) == "LJF"):
        self.solveLJF()
    elif(str(self.AlgoSelector.currentText()) == "LRTF"):
        self.solveLRTF()
    elif(str(self.AlgoSelector.currentText()) == "Priority"):
        self.solvePriority()

    # Store total Time took to execute program.
    self.totalTimeOfExecuting = int( self.GanttChartTable.item(1, self.GanttChartTable.columnCount() - 1).text() )