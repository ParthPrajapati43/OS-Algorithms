from PyQt5 import QtCore, QtGui, QtWidgets

def nextIOBT(self):    

    if(len(self.JOBqueue) <= self.currTimer):
        return

    # setting up the job queue
    self.JobQueue.setColumnCount(len(self.JOBqueue[self.currTimer]))
    for i in range(len(self.JOBqueue[self.currTimer])):
        item = QtWidgets.QTableWidgetItem(str(self.JOBqueue[self.currTimer][i] + 1))
        item.setBackground(QtGui.QColor(
            self.rgbRed[int(self.JOBqueue[self.currTimer][i])], self.rgbGreen[int(self.JOBqueue[self.currTimer][i])], self.rgbBlue[int(self.JOBqueue[self.currTimer][i])]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.JobQueue.setItem(0, i, item)
    
    # setting up the ready queue
    self.ReadyQueue.setColumnCount(len(self.READYqueue[self.currTimer]))
    for i in range(len(self.READYqueue[self.currTimer])):
        item = QtWidgets.QTableWidgetItem(str(self.READYqueue[self.currTimer][i] + 1))
        item.setBackground(QtGui.QColor(
            self.rgbRed[int(self.READYqueue[self.currTimer][i])], self.rgbGreen[int(self.READYqueue[self.currTimer][i])], self.rgbBlue[int(self.READYqueue[self.currTimer][i])]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.ReadyQueue.setItem(0, i, item)

    # setting up the CPU
    self.CPU.setColumnCount(len(self.inCPU[self.currTimer]))
    for i in range(len(self.inCPU[self.currTimer])):
        item = QtWidgets.QTableWidgetItem(str(self.inCPU[self.currTimer][i] + 1))
        item.setBackground(QtGui.QColor(
            self.rgbRed[int(self.inCPU[self.currTimer][i])], self.rgbGreen[int(self.inCPU[self.currTimer][i])], self.rgbBlue[int(self.inCPU[self.currTimer][i])]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.CPU.setItem(0, i, item)
    
    # setting up the IO queue
    self.IOQueue.setColumnCount(len(self.IOqueue[self.currTimer]))
    for i in range(len(self.IOqueue[self.currTimer])):
        item = QtWidgets.QTableWidgetItem(str(self.IOqueue[self.currTimer][i] + 1))
        item.setBackground(QtGui.QColor(
            self.rgbRed[int(self.IOqueue[self.currTimer][i])], self.rgbGreen[int(self.IOqueue[self.currTimer][i])], self.rgbBlue[int(self.IOqueue[self.currTimer][i])]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.IOQueue.setItem(0, i, item)

    # setting up the IO device
    self.IODevice.setColumnCount(len(self.inIO[self.currTimer]))
    for i in range(len(self.inIO[self.currTimer])):
        item = QtWidgets.QTableWidgetItem(str(self.inIO[self.currTimer][i] + 1))
        item.setBackground(QtGui.QColor(
            self.rgbRed[int(self.inIO[self.currTimer][i])], self.rgbGreen[int(self.inIO[self.currTimer][i])], self.rgbBlue[int(self.inIO[self.currTimer][i])]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.IODevice.setItem(0, i, item)
    
    # setting up the terminated queue
    self.TerminatedQueue.setColumnCount(len(self.TERMINATEDqueue[self.currTimer]))
    for i in range(len(self.TERMINATEDqueue[self.currTimer])):
        item = QtWidgets.QTableWidgetItem(str(self.TERMINATEDqueue[self.currTimer][i] + 1))
        item.setBackground(QtGui.QColor(
            self.rgbRed[int(self.TERMINATEDqueue[self.currTimer][i])], self.rgbGreen[int(self.TERMINATEDqueue[self.currTimer][i])], self.rgbBlue[int(self.TERMINATEDqueue[self.currTimer][i])]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.TerminatedQueue.setItem(0, i, item)

    # setting the gantt chart
    self.GanttChartTable.setColumnCount(min(self.currTimer+1, len(self.CGTableJobs)))
    for i in range(min(self.currTimer+1, len(self.CGTableJobs))):
        if(str(self.CGTableJobs[i]) != "X" and str(self.CGTableJobs[i]) != "C"):
            item = QtWidgets.QTableWidgetItem(str(int(self.CGTableJobs[i])+1))
        else:
            item = QtWidgets.QTableWidgetItem(str(self.CGTableJobs[i]))
        if(str(self.CGTableJobs[i]) != "X" and str(self.CGTableJobs[i]) != "C"):
            item.setBackground(QtGui.QColor(
                self.rgbRed[self.CGTableJobs[i]], self.rgbGreen[self.CGTableJobs[i]], self.rgbBlue[self.CGTableJobs[i]]))
            item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.GanttChartTable.setItem(0, i, item)
        item = QtWidgets.QTableWidgetItem(str(self.CGTableTimer[i]))
        if(str(self.CGTableJobs[i]) != "X" and str(self.CGTableJobs[i]) != "C"):
            item.setBackground(QtGui.QColor(
                self.rgbRed[self.CGTableJobs[i]], self.rgbGreen[self.CGTableJobs[i]], self.rgbBlue[self.CGTableJobs[i]]))
            item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.GanttChartTable.setItem(1, i, item)

    # setting the Percentage column
    self.setPerclist(self.storedPercentage[self.currTimer + 1])
    
    # setting the State column
    self.setStatelist(self.storedState[self.currTimer + 1])

    self.currTimer += 1
    
    # setting the progress bar
    self.ScheduleProgressBar.setValue((self.currTimer/self.totalTimeOfExecuting)*100)

    # setting the timer
    self.TimerLabel.setText(str(self.currTimer))