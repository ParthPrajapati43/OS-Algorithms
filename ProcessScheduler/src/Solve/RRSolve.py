from PyQt5 import QtCore, QtGui, QtWidgets

def solveRR(self):

    if(self.TimeQuantumSelector.value() == 0):
        self.TimeQuantumSelector.setValue(99)

    totalJobs = self.JobTable.rowCount()
    ATlist = self.getATList()
    BTlist = self.getBTList()
    self.CPU.setColumnCount(0) 
    # print(str(self.AlgoSelector.currentText()))

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

    # algorithm

    # array for job serial number for reference after sorting according to AT
    jobNumber = []
    for srno in range(totalJobs):
        jobNumber.append(srno)

    # sorting
    for i in range(totalJobs):
        for j in range(i, totalJobs):
            if(ATlist[j] < ATlist[i]):
                ATlist[j], ATlist[i] = ATlist[i], ATlist[j]
                BTlist[j], BTlist[i] = BTlist[i], BTlist[j]
                jobNumber[j], jobNumber[i] = jobNumber[i], jobNumber[j]

    # Update global arrays
    self.myATlist = ATlist
    self.myBTlist = BTlist
    self.myjobNumber = jobNumber

    # Create a list with totalJobs + 1 elements, to store pairs of [AT, BT] indexed for jobnumber(i).
    self.myJobDetails = [None] * (totalJobs + 1)
    for i in range(totalJobs):
        self.myJobDetails[jobNumber[i] + 1]  = [ATlist[i], BTlist[i]]
        # print(self.myJobDetails[jobNumber[i] + 1])

    # declaring all the column list
    CTlist = []
    TATlist = []
    WTlist = []
    RTlist = []
    startedAt = []

    for i in range(totalJobs):
        CTlist.append(0)
        TATlist.append(0)
        WTlist.append(0)
        RTlist.append(0)
        startedAt.append(-1)

    currTime = 0
    totalTAT = 0
    totalWT = 0
    totalRT = 0

    curr = 0
    finished = 0
    completed = []
    started = []
    for i in range(totalJobs):
        completed.append(False)
        started.append(False)
    
    queue = []

    self.GanttChartTable.setColumnCount(5000)
    BTlistbefore = []
    for i in range(len(BTlist)):
        BTlistbefore.append(BTlist[i])

    while(finished != totalJobs):
        print('curr start: ' + str(curr))
        print('BT start: ' + str(BTlist))
        print('AT: ' + str(ATlist))
        print('Queue at start: ' + str(queue))
        
        isthere = False

        # check if any process is available or not
        if(len(queue) > 0):
            isthere = True

        for i in range(totalJobs):
            if((not started[i]) and (ATlist[i] <= curr)):
                started[i] = True
                queue.append(i)
                isthere = True

        print('Queue after ins: ' + str(queue))
        # if not available make the current timer to the next closest Job
        if(not isthere):
            GCdone = False
            for i in range(totalJobs):
                if(not started[i]):
                    started[i] = True
                    queue.append(i)
                    if(not GCdone):
                        GCdone = True
                        # add X in gantt chart
                        for j in range(curr, ATlist[i]):
                            item = QtWidgets.QTableWidgetItem("X")
                            item.setTextAlignment(
                                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                            self.GanttChartTable.setItem(0, j, item)
                            item = QtWidgets.QTableWidgetItem(str(j+1))
                            item.setTextAlignment(
                                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                            self.GanttChartTable.setItem(1, j, item)
                            self.CGTableJobs.append("X")
                            self.CGTableTimer.append(j+1)
                        curr = ATlist[i]
                    break

            for i in range(totalJobs):
                if((not started[i]) and (curr == ATlist[i])):
                    started[i] = True
                    queue.append(i)

        print('Queue after ins2: ' + str(queue))
        # we got the process in present, work upon it

        runtill = 0
        if(self.TimeQuantumSelector.value() >= BTlist[queue[0]]):
            runtill = curr + BTlist[queue[0]]
        else:
            runtill =  curr + self.TimeQuantumSelector.value()
        
        # add 'Job i' in Gantt Chart
        for j in range(curr, runtill):
            item = QtWidgets.QTableWidgetItem(str(jobNumber[queue[0]]+1))
            item.setBackground(QtGui.QColor(
                self.rgbRed[jobNumber[queue[0]]], self.rgbGreen[jobNumber[queue[0]]], self.rgbBlue[jobNumber[queue[0]]]))
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.GanttChartTable.setItem(0, j, item)
            item = QtWidgets.QTableWidgetItem(str(j+1))
            item.setBackground(QtGui.QColor(
                self.rgbRed[jobNumber[queue[0]]], self.rgbGreen[jobNumber[queue[0]]], self.rgbBlue[jobNumber[queue[0]]]))
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.GanttChartTable.setItem(1, j, item)
            self.CGTableJobs.append(jobNumber[queue[0]]+1)
            self.CGTableTimer.append(j+1)
        
        if(self.TimeQuantumSelector.value() < BTlist[queue[0]]):
            if(startedAt[queue[0]] == -1):
                startedAt[queue[0]] = curr
            curr += self.TimeQuantumSelector.value()
            BTlist[queue[0]] -= self.TimeQuantumSelector.value()
            queue.append(queue[0])
        else:
            if(startedAt[queue[0]] == -1):
                startedAt[queue[0]] = curr
            print(str(queue[0]) + ' completed')
            curr += BTlist[queue[0]]
            BTlist[queue[0]] = 0
            CTlist[queue[0]] = curr
            TATlist[queue[0]] = CTlist[queue[0]] - ATlist[queue[0]]
            WTlist[queue[0]] = TATlist[queue[0]] - BTlistbefore[queue[0]]
            RTlist[queue[0]] = curr - BTlistbefore[queue[0]] - ATlist[queue[0]]
            totalTAT += TATlist[queue[0]]
            totalWT += WTlist[queue[0]]
            totalRT += RTlist[queue[0]]
            finished += 1
            completed[queue[0]] = True
            print('WTlist: ' + str(WTlist))
            print('RTlist: ' + str(RTlist))

        queue.pop(0)
        print('Queue at end: ' + str(queue))
        print('BT start: ' + str(BTlist))
        print('curr end: ' + str(curr))
        print('')

        if(finished != totalJobs):
            # add 'C' in Gantt Chart
            for j in range(curr, curr+self.ContextSwitchSelector.value()):
                item = QtWidgets.QTableWidgetItem("C")
                item.setTextAlignment(
                    QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.GanttChartTable.setItem(0, j, item)
                item = QtWidgets.QTableWidgetItem(str(j+1))
                item.setTextAlignment(
                    QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.GanttChartTable.setItem(1, j, item)
                self.CGTableJobs.append("C")
                self.CGTableTimer.append(j+1)
            
            # adding the context switch time
            curr += self.ContextSwitchSelector.value()

    self.GanttChartTable.setColumnCount(curr)
    
    # Add all Jobs to JobQueue.
    self.JobQueue.setColumnCount(totalJobs)
    for i in range(totalJobs):
        item = QtWidgets.QTableWidgetItem(str(jobNumber[i]+1))
        item.setBackground(QtGui.QColor(
            self.rgbRed[jobNumber[i]], self.rgbGreen[jobNumber[i]], self.rgbBlue[jobNumber[i]]))
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.JobQueue.setItem(0, i, item)
        # print(str(i) + " " + str(jobNumber[i] + 1))
    templist = []
    templen = self.JobQueue.columnCount()
    for i in range(templen):
        item = self.JobQueue.item(0, i)
        valueHere = item.text()
        templist.append(int(valueHere))
    self.storedJobQueue.append(templist)
    self.storedReadyQueue.append([])
    self.storedCPU.append([])
    self.storedTerminatedQueue.append([])
    templist = []
    templen = self.JobTable.rowCount()
    for i in range(templen):
        templist.append("0%")
    self.setPerclist(templist)
    self.storedPercentage.append(templist)
    templist = []
    templen = self.JobTable.rowCount()
    for i in range(templen):
        templist.append("Job")
    self.setStatelist(templist)
    self.storedState.append(templist)
        
    # sorting back
    for i in range(totalJobs):
        for j in range(i, totalJobs):
            if(jobNumber[j] < jobNumber[i]):
                ATlist[j], ATlist[i] = ATlist[i], ATlist[j]
                BTlist[j], BTlist[i] = BTlist[i], BTlist[j]
                CTlist[j], CTlist[i] = CTlist[i], CTlist[j]
                TATlist[j], TATlist[i] = TATlist[i], TATlist[j]
                WTlist[j], WTlist[i] = WTlist[i], WTlist[j]
                RTlist[j], RTlist[i] = RTlist[i], RTlist[j]
                jobNumber[j], jobNumber[i] = jobNumber[i], jobNumber[j]

    self.setCTlist(CTlist)
    self.setTATlist(TATlist)
    self.setWTlist(WTlist)
    self.setRTlist(RTlist)

    self.AvgTAT.setText(str(round(totalTAT/totalJobs, 5)))
    self.AvgWT.setText(str(round(totalWT/totalJobs, 5)))
    self.AvgRT.setText(str(round(totalRT/totalJobs, 5)))

    # Store total Time took to execute program.
    self.totalTimeOfExecuting = int( self.GanttChartTable.item(1, self.GanttChartTable.columnCount() - 1).text() )
