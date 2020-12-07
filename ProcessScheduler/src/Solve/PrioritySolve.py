from PyQt5 import QtCore, QtGui, QtWidgets

def solvePriority(self):

    totalJobs = self.JobTable.rowCount()
    Prioritylist = self.getPriorityList()
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
    for i in range(totalJobs):
        completed.append(False)
    
    self.GanttChartTable.setColumnCount(5000)
    BTlistbefore = []
    for i in range(len(BTlist)):
        BTlistbefore.append(BTlist[i])
    
    while(finished != totalJobs):
        
        isthere = False

        # sorting
        for i in range(totalJobs):
            for j in range(i, totalJobs):
                if((ATlist[j] < ATlist[i]) or (ATlist[j] == ATlist[i] and Prioritylist[j] < Prioritylist[i])):
                    Prioritylist[j], Prioritylist[i] = Prioritylist[i], Prioritylist[j]
                    ATlist[j], ATlist[i] = ATlist[i], ATlist[j]
                    BTlist[j], BTlist[i] = BTlist[i], BTlist[j]
                    BTlistbefore[j], BTlistbefore[i] = BTlistbefore[i], BTlistbefore[j]
                    CTlist[j], CTlist[i] = CTlist[i], CTlist[j]
                    TATlist[j], TATlist[i] = TATlist[i], TATlist[j]
                    WTlist[j], WTlist[i] = WTlist[i], WTlist[j]
                    RTlist[j], RTlist[i] = RTlist[i], RTlist[j]
                    startedAt[j], startedAt[i] = startedAt[i], startedAt[j]
                    jobNumber[j], jobNumber[i] = jobNumber[i], jobNumber[j]

        # check if any process is available or not
        for i in range(totalJobs):
            if((not completed[i]) and (ATlist[i] <= curr)):
                isthere = True
                break
        
        # if not available make the current timer to the next closest Job
        if(not isthere):
            for i in range(totalJobs):
                if(not completed[i]):
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

        # get the list of all available Jobs
        available = []
        for i in range(totalJobs):
            if((not completed[i]) and (ATlist[i] <= curr)):
                available.append(int(i))

        # now get the Job with the lowest priority
        present = available[0]
        Priority = Prioritylist[available[0]]
        for i in range(len(available)):
            if((Prioritylist[available[i]] < Priority) or (Prioritylist[available[i]] == Priority and jobNumber[available[i]] < jobNumber[present])):
                Priority = Prioritylist[available[i]]
                present = available[i]
        
        # we got the process in present, work upon it

        runtill = 0
        if(self.ModePreemptive.isChecked()):
            runtill = curr + 1
        else:
            runtill =  curr+BTlist[present]
        
        # add 'Job i' in Gantt Chart
        for j in range(curr, runtill):
            item = QtWidgets.QTableWidgetItem(str(jobNumber[present]+1))
            item.setBackground(QtGui.QColor(
                self.rgbRed[jobNumber[present]], self.rgbGreen[jobNumber[present]], self.rgbBlue[jobNumber[present]]))
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.GanttChartTable.setItem(0, j, item)
            item = QtWidgets.QTableWidgetItem(str(j+1))
            item.setBackground(QtGui.QColor(
                self.rgbRed[jobNumber[present]], self.rgbGreen[jobNumber[present]], self.rgbBlue[jobNumber[present]]))
            item.setForeground(QtGui.QColor(0, 0, 0))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.GanttChartTable.setItem(1, j, item)
            self.CGTableJobs.append(jobNumber[present]+1)
            self.CGTableTimer.append(j+1)
        
        if(self.ModePreemptive.isChecked() and BTlist[present] > 1):
            if(startedAt[present] == -1):
                startedAt[present] = curr
            curr += 1
            BTlist[present] -= 1
        else:
            if(startedAt[present] == -1):
                startedAt[present] = curr
            curr += BTlist[present]
            CTlist[present] = curr
            TATlist[present] = CTlist[present] - ATlist[present]
            WTlist[present] = TATlist[present] - BTlistbefore[present]
            RTlist[present] = startedAt[present] - ATlist[present]
            totalTAT += TATlist[present]
            totalWT += WTlist[present]
            totalRT += RTlist[present]
            finished += 1
            completed[present] = True

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
                Prioritylist[j], Prioritylist[i] = Prioritylist[i], Prioritylist[j]
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
