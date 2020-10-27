from PyQt5 import QtCore, QtGui, QtWidgets

def nextFCFS(self):

    print("myTimer = " + str(self.myTimer) + " len = " + str(len(self.storedJobQueue)))
    #print("timer = " + str(len(self.storedJobQueue[self.myTimer])))
    print("currTimer = " + str(self.currTimer))
    #print("timer = " + str(len(self.storedJobQueue[self.currTimer])))


    if(self.currTimer < self.myTimer):
        
        # updating the current timer
        self.currTimer += 1

        if(self.currTimer > self.totalTimeOfExecuting + 1):
            self.currTimer -= 1
            return

        #Handle the case of out of index. Just update the termination queue.
        if(self.currTimer == self.totalTimeOfExecuting + 1):

            # setting the timer
            self.TimerLabel.setText(str(self.currTimer))

            newCellsOfJob = []
            totalJobs = self.TerminatedQueue.columnCount()
            for i in range(totalJobs):
                newCellsOfJob.append( int( self.TerminatedQueue.item(0, i).text() ) )

            totalJobs += 1
            newCellsOfJob.append( int( self.CPU.item(0, 0).text() ) )
            # Change State and % of last job from CPU to Termainated.
            self.JobTable.item(int( self.CPU.item(0, 0).text() ) - 1, 10).setText("Terminated")
            self.JobTable.item(int( self.CPU.item(0, 0).text() ) - 1, 9).setText("100%")
            self.TerminatedQueue.setColumnCount(totalJobs)
            self.CPU.setColumnCount(0)

            # Insert them in Terminated queue.
            for i in range(totalJobs):
                item = QtWidgets.QTableWidgetItem(str(newCellsOfJob[i]))
                item.setBackground(QtGui.QColor(
                    self.rgbRed[newCellsOfJob[i] - 1], self.rgbGreen[newCellsOfJob[i] - 1], self.rgbBlue[newCellsOfJob[i] - 1]) )
                item.setForeground(QtGui.QColor(0, 0, 0))
                item.setTextAlignment(
                    QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.TerminatedQueue.setItem(0, i, item)
            
            return
        
        
            
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

        # setting the progress bar
        self.ScheduleProgressBar.setValue((self.currTimer/self.totalTimeOfExecuting)*100)

        # setting the timer
        self.TimerLabel.setText(str(self.currTimer))

        return

    # Update Time.
    self.myTimer += 1
    # updating the current timer
    self.currTimer += 1

    if(self.myTimer > self.totalTimeOfExecuting + 1):
        self.myTimer -= 1
        # Limit the value of currTimer
        if(self.currTimer > self.myTimer):
            self.currTimer = self.myTimer
        return

    # Limit the value of currTimer
    if(self.currTimer > self.myTimer):
        self.currTimer = self.myTimer
    
    # Exit if user clicks after we finished executing all jobs.
    if(self.myTimer == self.totalTimeOfExecuting + 1):

        self.TimerLabel.setText(str(self.myTimer))

        newCellsOfJob = []
        totalJobs = self.TerminatedQueue.columnCount()
        for i in range(totalJobs):
            newCellsOfJob.append( int( self.TerminatedQueue.item(0, i).text() ) )

        totalJobs += 1
        newCellsOfJob.append( int( self.CPU.item(0, 0).text() ) )
        # Change State and % of last job from CPU to Termainated.
        self.JobTable.item(int( self.CPU.item(0, 0).text() ) - 1, 10).setText("Terminated")
        self.JobTable.item(int( self.CPU.item(0, 0).text() ) - 1, 9).setText("100%")
        self.TerminatedQueue.setColumnCount(totalJobs)
        self.CPU.setColumnCount(0)

        # Insert them in Terminated queue.
        for i in range(totalJobs):
            item = QtWidgets.QTableWidgetItem(str(newCellsOfJob[i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[newCellsOfJob[i] - 1], self.rgbGreen[newCellsOfJob[i] - 1], self.rgbBlue[newCellsOfJob[i] - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.TerminatedQueue.setItem(0, i, item)
        return

    
    
    self.TimerLabel.setText(str(self.myTimer))

    # Gantt Chart Play Update
    self.GanttChartTable.setColumnCount(self.myTimer)
    for i in range(self.myTimer):
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

    # If the timer == last cell's ATlist of it, remove from job Queue.
    # and add it into ready queue.

    isJobQueueEmpty = 1
    currJob = 0
    if(self.JobQueue.columnCount() != 0):
        isJobQueueEmpty = 0
        currJob = int(self.JobQueue.item(0, 0).text())
    
    print(str(currJob) +  " " + str(isJobQueueEmpty))
    while( isJobQueueEmpty == 0 and self.myTimer == self.myJobDetails[currJob][0] ):

        # Delete last item of Job Queue and save remaining in array newCellsOfJob.
        newCellsOfJob = []
        totalJobs = self.JobQueue.columnCount()
        for i in range(1, totalJobs):
            newCellsOfJob.append( int( self.JobQueue.item(0, i).text() ) )
        
        self.JobQueue.setColumnCount(totalJobs - 1)
        totalJobs -= 1

        if(totalJobs == 0):
            isJobQueueEmpty = 1
        
        # Update the table of Job Queue.
        for i in range(totalJobs):
            item = QtWidgets.QTableWidgetItem(str(newCellsOfJob[i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[newCellsOfJob[i] - 1], self.rgbGreen[newCellsOfJob[i] - 1], self.rgbBlue[newCellsOfJob[i] - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.JobQueue.setItem(0, i, item)
        
        # Save items of Ready Queue in newCellsofJob and new Job to add in it. 
        newCellsOfJob = []
        totalJobs = self.ReadyQueue.columnCount()
        for i in range(totalJobs):
            newCellsOfJob.append( int( self.ReadyQueue.item(0, i).text() ) )

        totalJobs += 1
        newCellsOfJob.append( int(currJob) )
        self.ReadyQueue.setColumnCount(totalJobs)

        # Change state of Currjob to ready
        self.JobTable.item(int(currJob) - 1, 10).setText("Ready")

        # Insert them in Ready queue.
        for i in range(totalJobs):
            item = QtWidgets.QTableWidgetItem(str(newCellsOfJob[i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[newCellsOfJob[i] - 1], self.rgbGreen[newCellsOfJob[i] - 1], self.rgbBlue[newCellsOfJob[i] - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ReadyQueue.setItem(0, i, item)

        if(isJobQueueEmpty == 0):
            # Update next item coming Job queue.
            currJob = int(self.JobQueue.item(0, 0).text())

        
    # Adding Job from Ready to CPU Queue.

    # Last Cell of Gantt Chart.
    lastColValueAtGantt = self.GanttChartTable.item(0, self.myTimer - 1).text()

    print(lastColValueAtGantt)
    # # No need to update from R -> C, if we have empty ready or No job execution.
    # if(lastColValueAtGantt == "X" or lastColValueAtGantt == 'C'):
    #     return

    # else, we need to push from ready to CPU Queue,only if we finished Burst Time of The job executing at CPU (OR) CPU block is empty
    print("here " + str(self.CPU.columnCount() ) ) 

    # Update Perc of Current executing CPU Job.
    if(self.myTimer - self.latestTimerStart != self.latestTimer and self.CPU.columnCount() == 1):
        perc = round( (self.myTimer - self.latestTimerStart)/self.latestTimer, 2 ) * 100 
        self.JobTable.item( int( self.CPU.item(0, 0).text() ) - 1, 9 ).setText( str(str(perc) + "%" ) )

    if( self.myTimer - self.latestTimerStart == self.latestTimer or self.CPU.columnCount() == 0):

        # Delete last item of Ready Queue and save remaining in array newCellsOfJob.
        isTerminated = 0
        lastCpuJob = 0
        if(self.CPU.columnCount() == 1):
            isTerminated = 1
            lastCpuJob = int( self.CPU.item(0, 0).text() ) 

        isXorC = 0
        if(lastColValueAtGantt == "X" or lastColValueAtGantt == 'C'):
            isXorC = 1
        
        if(self.ReadyQueue.columnCount() and lastColValueAtGantt != "X" and lastColValueAtGantt != 'C' ):
            lastJobAtReady = int( self.ReadyQueue.item(0, 0).text() ) 

            newCellsOfJob = []
            totalJobs = self.ReadyQueue.columnCount()
            for i in range(1, totalJobs):
                newCellsOfJob.append( int( self.ReadyQueue.item(0, i).text() ) )
            
            self.ReadyQueue.setColumnCount(totalJobs - 1)
            totalJobs -= 1

            # Update the table of Ready Queue after deletion of last item.
            for i in range(totalJobs):
                item = QtWidgets.QTableWidgetItem(str(newCellsOfJob[i]))
                item.setBackground(QtGui.QColor(
                    self.rgbRed[newCellsOfJob[i] - 1], self.rgbGreen[newCellsOfJob[i] - 1], self.rgbBlue[newCellsOfJob[i] - 1]) )
                item.setForeground(QtGui.QColor(0, 0, 0))
                item.setTextAlignment(
                    QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.ReadyQueue.setItem(0, i, item)
            
            # Update CPU Block.
            self.CPU.setColumnCount(1)
            print("lastjobready " + str(lastJobAtReady) )
            item = QtWidgets.QTableWidgetItem(str(lastJobAtReady))
            item.setBackground(QtGui.QColor(
                self.rgbRed[lastJobAtReady - 1], self.rgbGreen[lastJobAtReady - 1], self.rgbBlue[lastJobAtReady - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.CPU.setItem(0, 0, item)

            # Change state to CPU.
            self.JobTable.item(int(lastJobAtReady) - 1, 10).setText("CPU")

            # Update Timer of Newly inserted Job at CPU.
            self.latestTimerStart = self.myTimer
            self.latestTimer = self.myJobDetails[lastJobAtReady][1]

        if(isTerminated == 0):
            # saving the states in a list so that we can use it for Previous Step Button
            # saving Job Queue
            templist = []
            templen = self.JobQueue.columnCount()
            for i in range(templen):
                item = self.JobQueue.item(0, i)
                valueHere = item.text()
                templist.append(int(valueHere))
            print("templistJ = " + str(templist))
            print("storedlistJ = " + str(self.storedJobQueue))
            self.storedJobQueue.append(templist)
            # saving Ready Queue
            templist = []
            templen = self.ReadyQueue.columnCount()
            for i in range(templen):
                item = self.ReadyQueue.item(0, i)
                valueHere = item.text()
                templist.append(int(valueHere))
            self.storedReadyQueue.append(templist)
            # saving CPU
            templist = []
            templen = self.CPU.columnCount()
            for i in range(templen):
                item = self.CPU.item(0, i)
                valueHere = item.text()
                templist.append(int(valueHere))
            self.storedCPU.append(templist)
            # saving Terminated Queue
            templist = []
            templen = self.TerminatedQueue.columnCount()
            for i in range(templen):
                item = self.TerminatedQueue.item(0, i)
                valueHere = item.text()
                templist.append(int(valueHere))
            self.storedTerminatedQueue.append(templist)
            # saving Percentage from the table
            self.storedPercentage.append(self.getPercList())
            # saving State from the table
            self.storedState.append(self.getStateList())
            print("Stored %: " + str(self.storedPercentage))
            print("Stored State: " + str(self.storedState))
            
            # setting the progress bar
            self.ScheduleProgressBar.setValue((self.myTimer/self.totalTimeOfExecuting)*100)
            return

        if(isXorC):
            self.CPU.setColumnCount(0)

        # Save items of Terminated Queue in newCellsofJob and new finished Job to add in it.
                
        newCellsOfJob = []
        totalJobs = self.TerminatedQueue.columnCount()
        for i in range(totalJobs):
            newCellsOfJob.append( int( self.TerminatedQueue.item(0, i).text() ) )

        totalJobs += 1
        newCellsOfJob.append( lastCpuJob )
        self.TerminatedQueue.setColumnCount(totalJobs)

        # Update the cell of the lastCpuJob to Terminated.
        print("last" + str(lastCpuJob - 1))
        self.JobTable.item(lastCpuJob - 1, 10).setText("Terminated")
        self.JobTable.item(lastCpuJob - 1, 9).setText("100%")

        # Insert them in Terminated queue.
        for i in range(totalJobs):
            item = QtWidgets.QTableWidgetItem(str(newCellsOfJob[i]))
            item.setBackground(QtGui.QColor(
                self.rgbRed[newCellsOfJob[i] - 1], self.rgbGreen[newCellsOfJob[i] - 1], self.rgbBlue[newCellsOfJob[i] - 1]) )
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.TerminatedQueue.setItem(0, i, item)
    
    # saving the states in a list so that we can use it for Previous Step Button
    # saving Job Queue
    templist = []
    templen = self.JobQueue.columnCount()
    for i in range(templen):
        item = self.JobQueue.item(0, i)
        valueHere = item.text()
        templist.append(int(valueHere))
    print("templistJ = " + str(templist))
    print("storedlistJ = " + str(self.storedJobQueue))
    self.storedJobQueue.append(templist)
    # saving Ready Queue
    templist = []
    templen = self.ReadyQueue.columnCount()
    for i in range(templen):
        item = self.ReadyQueue.item(0, i)
        valueHere = item.text()
        templist.append(int(valueHere))
    self.storedReadyQueue.append(templist)
    # saving CPU
    templist = []
    templen = self.CPU.columnCount()
    for i in range(templen):
        item = self.CPU.item(0, i)
        valueHere = item.text()
        templist.append(int(valueHere))
    self.storedCPU.append(templist)
    # saving Terminated Queue
    templist = []
    templen = self.TerminatedQueue.columnCount()
    for i in range(templen):
        item = self.TerminatedQueue.item(0, i)
        valueHere = item.text()
        templist.append(int(valueHere))
    self.storedTerminatedQueue.append(templist)
    # saving Percentage from the table
    self.storedPercentage.append(self.getPercList())
    # saving State from the table
    self.storedState.append(self.getStateList())
    
    # setting the progress bar
    self.ScheduleProgressBar.setValue((self.myTimer/self.totalTimeOfExecuting)*100)