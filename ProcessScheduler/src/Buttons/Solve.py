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
    self.JOBqueue = []
    self.READYqueue = []
    self.inCPU = []
    self.TERMINATEDqueue = []
    self.IOqueue = []
    self.inIO = []
    self.GCchangeBtn.setText('IO Gantt Chart')
    self.GanttChartLabel.setText('Gantt Chart (CPU)')
    self.GCchangeBtn.setEnabled(False)

    if(str(self.AlgoSelector.currentText()) == "FCFS"):
        if(self.TypeWithoutIOBT.isChecked()):
            self.solveFCFS()
        else:
            self.GCchangeBtn.setEnabled(True)
            self.solveFCFSIO()
    elif(str(self.AlgoSelector.currentText()) == "SJF"):
        if(self.TypeWithoutIOBT.isChecked()):
            self.solveSJF()
        else:
            if(self.ModeNonPreemptive.isChecked()):
                self.GCchangeBtn.setEnabled(True)
                self.solveSJFIO()
            else:
                self.GCchangeBtn.setEnabled(True)
                self.solveSRTFIO()    
    elif(str(self.AlgoSelector.currentText()) == "SRTF"):
        if(self.TypeWithoutIOBT.isChecked()):
            self.solveSRTF()
        else:
            if(self.ModeNonPreemptive.isChecked()):
                self.GCchangeBtn.setEnabled(True)
                self.solveSJFIO()
            else:
                self.GCchangeBtn.setEnabled(True)
                self.solveSRTFIO()
    elif(str(self.AlgoSelector.currentText()) == "RR"):
        if(self.TypeWithoutIOBT.isChecked()):
            self.solveRR()
        else:
            self.GCchangeBtn.setEnabled(True)
            self.solveRRIO()
    elif(str(self.AlgoSelector.currentText()) == "LJF"):
        if(self.TypeWithoutIOBT.isChecked()):
            self.solveLJF()
        else:
            if(self.ModeNonPreemptive.isChecked()):
                self.GCchangeBtn.setEnabled(True)
                self.solveLJFIO()
            else:
                self.GCchangeBtn.setEnabled(True)
                self.solveLRTFIO()
    elif(str(self.AlgoSelector.currentText()) == "LRTF"):
        if(self.TypeWithoutIOBT.isChecked()):
            self.solveLRTF()
        else:
            if(self.ModeNonPreemptive.isChecked()):
                self.GCchangeBtn.setEnabled(True)
                self.solveLJFIO()
            else:
                self.GCchangeBtn.setEnabled(True)
                self.solveLRTFIO()
    elif(str(self.AlgoSelector.currentText()) == "Priority"):
        if(self.TypeWithoutIOBT.isChecked()):
            self.solvePriority()
        else:
            if(self.ModeNonPreemptive.isChecked()):
                self.GCchangeBtn.setEnabled(True)
                self.solvePriorityIONP()
            else:
                self.GCchangeBtn.setEnabled(True)
                self.solvePriorityIO()

    # Store total Time took to execute program.
    self.totalTimeOfExecuting = int( self.GanttChartTable.item(1, self.GanttChartTable.columnCount() - 1).text() )