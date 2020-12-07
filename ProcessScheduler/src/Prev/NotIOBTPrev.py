from PyQt5 import QtCore, QtGui, QtWidgets

def prevNotIOBT(self):
        
    if(self.currTimer > 0):
        # updating the current timer
        self.currTimer -= 1

        # setting the job queue
        self.JobQueue.setColumnCount(len(self.storedJobQueue[self.currTimer]))
        for i in range(len(self.storedJobQueue[self.currTimer])):
            item = QtWidgets.QTableWidgetItem(str(self.storedJobQueue[self.currTimer][i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[int(self.storedJobQueue[self.currTimer][i]) - 1], self.rgbGreen[int(self.storedJobQueue[self.currTimer][i]) - 1], self.rgbBlue[int(self.storedJobQueue[self.currTimer][i]) - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.JobQueue.setItem(0, i, item)

        # setting the ready queue
        self.ReadyQueue.setColumnCount(len(self.storedReadyQueue[self.currTimer]))
        for i in range(len(self.storedReadyQueue[self.currTimer])):
            item = QtWidgets.QTableWidgetItem(str(self.storedReadyQueue[self.currTimer][i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[int(self.storedReadyQueue[self.currTimer][i]) - 1], self.rgbGreen[int(self.storedReadyQueue[self.currTimer][i]) - 1], self.rgbBlue[int(self.storedReadyQueue[self.currTimer][i]) - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ReadyQueue.setItem(0, i, item)

        # setting the CPU
        self.CPU.setColumnCount(len(self.storedCPU[self.currTimer]))
        for i in range(len(self.storedCPU[self.currTimer])):
            item = QtWidgets.QTableWidgetItem(str(self.storedCPU[self.currTimer][i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[int(self.storedCPU[self.currTimer][i]) - 1], self.rgbGreen[int(self.storedCPU[self.currTimer][i]) - 1], self.rgbBlue[int(self.storedCPU[self.currTimer][i]) - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.CPU.setItem(0, i, item)

        # setting the terminated queue
        self.TerminatedQueue.setColumnCount(len(self.storedTerminatedQueue[self.currTimer]))
        for i in range(len(self.storedTerminatedQueue[self.currTimer])):
            item = QtWidgets.QTableWidgetItem(str(self.storedTerminatedQueue[self.currTimer][i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[int(self.storedTerminatedQueue[self.currTimer][i]) - 1], self.rgbGreen[int(self.storedTerminatedQueue[self.currTimer][i]) - 1], self.rgbBlue[int(self.storedTerminatedQueue[self.currTimer][i]) - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.TerminatedQueue.setItem(0, i, item)

        # setting the gantt chart
        self.GanttChartTable.setColumnCount(self.currTimer)
        for i in range(self.currTimer):
            item = QtWidgets.QTableWidgetItem(str(self.CGTableJobs[i]))
            if(str(self.CGTableJobs[i]) != "X" and str(self.CGTableJobs[i]) != "C"):
                item.setBackground(QtGui.QColor(
                    self.rgbRed[self.CGTableJobs[i]-1], self.rgbGreen[self.CGTableJobs[i]-1], self.rgbBlue[self.CGTableJobs[i]-1]))
                item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.GanttChartTable.setItem(0, i, item)
            item = QtWidgets.QTableWidgetItem(str(self.CGTableTimer[i]))
            if(str(self.CGTableJobs[i]) != "X" and str(self.CGTableJobs[i]) != "C"):
                item.setBackground(QtGui.QColor(
                    self.rgbRed[self.CGTableJobs[i]-1], self.rgbGreen[self.CGTableJobs[i]-1], self.rgbBlue[self.CGTableJobs[i]-1]))
                item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.GanttChartTable.setItem(1, i, item)
        
        # setting the Percentage column
        self.setPerclist(self.storedPercentage[self.currTimer])
        # setting the State column
        self.setStatelist(self.storedState[self.currTimer])
        print("Stored %: " + str(self.storedPercentage))
        print("Stored State: " + str(self.storedState))

        # setting the progress bar
        self.ScheduleProgressBar.setValue((self.currTimer/self.totalTimeOfExecuting)*100)
        
        # setting the timer
        self.TimerLabel.setText(str(self.currTimer))