from PyQt5 import QtCore, QtGui, QtWidgets

def nextNotIOBT(self):

    # print("myTimer = " + str(self.myTimer) + " len = " + str(len(self.storedJobQueue)))
    # #print("timer = " + str(len(self.storedJobQueue[self.myTimer])))
    # print("currTimer = " + str(self.currTimer))
    # #print("timer = " + str(len(self.storedJobQueue[self.currTimer])))

    # ----------- USE Already STORED STATES ----------------------

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

    # --------------------- UPDATE TIMES and MINIMAL CHECKS ----------------------

    # Update Time.
    self.myTimer += 1
    # updating the current timer
    self.currTimer += 1

    # We have already finished executing all tasks. Do Nothing.
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
        # Empty The CPU.
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

    # ------------------- GANTT CHART UPDATE --------------------

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

   
    # -------------------------- MAIN CODE ---------------------

    myJobList = []
    myReadyList = []
    myCPUList = []
    myTerminatedList = []

    totalJobs = self.JobTable.rowCount()
    totalJobs += 1
    totalExecuting = [None] * (totalJobs)
    inCPU = [None] * (totalJobs)
    for i in range(1, totalJobs):
        totalExecuting[i] = 0
        inCPU[i] = 0

    for time in range(self.myTimer):
        sJob = self.CGTableJobs[time]
        if (sJob == "X" or sJob == "C"): continue
        job = int(sJob)
        totalExecuting[job] += 1
        if (totalExecuting[job] == self.myJobDetails[job][1]):
            if (time < self.myTimer - 1): 
                myTerminatedList.append(job) 
                totalExecuting[job] += 1
        if (time == self.myTimer - 1 and totalExecuting[job] <= self.myJobDetails[job][1] ):
            myCPUList.append(job) 
            inCPU[job] = 1

    
    for job in range(1, totalJobs):
        print("JOB => " + str(job) + "EXEC " + str(totalExecuting[job]) + "REQEXEC " + str(self.myJobDetails[job][1]) )
        if (totalExecuting[job] < self.myJobDetails[job][1]):
            if (self.myTimer < self.myJobDetails[job][0]):
                myJobList.append(job)
            elif (self.myTimer >= self.myJobDetails[job][0] and inCPU[job] == 0):
                myReadyList.append(job)
        perc = float(totalExecuting[job] / self.myJobDetails[job][1]) * 100.0
        self.JobTable.item(job - 1, 9).setText(str(perc) + "%")

    
    # ------------------ ADD INTO ANIMATION ---------------------------

    totalJobs = len(myJobList)
    self.JobQueue.setColumnCount(totalJobs)
    for i in range(totalJobs):
        item = QtWidgets.QTableWidgetItem(str(myJobList[i]))
        item.setBackground(QtGui.QColor(
            self.rgbRed[myJobList[i] - 1], self.rgbGreen[myJobList[i] - 1], self.rgbBlue[myJobList[i] - 1]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.JobQueue.setItem(0, i, item)
        self.JobTable.item(myJobList[i] - 1, 10).setText("Job")
    
    totalJobs = len(myReadyList)
    self.ReadyQueue.setColumnCount(totalJobs)
    for i in range(totalJobs):
        item = QtWidgets.QTableWidgetItem(str(myReadyList[i]))
        item.setBackground(QtGui.QColor(
            self.rgbRed[myReadyList[i] - 1], self.rgbGreen[myReadyList[i] - 1], self.rgbBlue[myReadyList[i] - 1]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.ReadyQueue.setItem(0, i, item)
        self.JobTable.item(myReadyList[i] - 1, 10).setText("Ready")

    totalJobs = len(myCPUList)
    self.CPU.setColumnCount(totalJobs)
    for i in range(totalJobs):
        item = QtWidgets.QTableWidgetItem(str(myCPUList[i]))
        item.setBackground(QtGui.QColor(
            self.rgbRed[myCPUList[i] - 1], self.rgbGreen[myCPUList[i] - 1], self.rgbBlue[myCPUList[i] - 1]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.CPU.setItem(0, i, item)
        self.JobTable.item(myCPUList[i] - 1, 10).setText("CPU")
    
    totalJobs = len(myTerminatedList)
    self.TerminatedQueue.setColumnCount(totalJobs)
    for i in range(totalJobs):
        item = QtWidgets.QTableWidgetItem(str(myTerminatedList[i]))
        item.setBackground(QtGui.QColor(
            self.rgbRed[myTerminatedList[i] - 1], self.rgbGreen[myTerminatedList[i] - 1], self.rgbBlue[myTerminatedList[i] - 1]) )
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.TerminatedQueue.setItem(0, i, item)
        self.JobTable.item(myTerminatedList[i] - 1, 10).setText("Terminated")
        self.JobTable.item(myTerminatedList[i] - 1, 9).setText("100%")
    

    # ------------------------- SAVE CURRENT TIMER STATES --------------------


    # saving the states in a list so that we can use it for Previous Step Button
    # saving Job Queue
    templist = []
    templen = self.JobQueue.columnCount()
    for i in range(templen):
        item = self.JobQueue.item(0, i)
        valueHere = item.text()
        templist.append(int(valueHere))
    # print("templistJ = " + str(templist))
    # print("storedlistJ = " + str(self.storedJobQueue))
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