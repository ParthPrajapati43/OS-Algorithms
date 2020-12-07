from PyQt5 import QtCore, QtGui, QtWidgets
from copy import deepcopy

def solveLRTFIO(self):

    totalJobs = self.JobTable.rowCount()
    ATlist = self.getATList()
    BTlist = self.getBTList()
    IOBTlist = self.getIOBTList()
    BT2list = self.getBT2List()
    self.CPU.setColumnCount(0) 
    # print(str(self.AlgoSelector.currentText()))

    self.CGTableJobs = []
    self.CGTableTimer = []
    self.IOCGTableJobs = []
    self.IOCGTableTimer = []
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

    # algorithm

    # array for job serial number for reference after sorting according to AT
    jobNumber = []
    for srno in range(totalJobs):
        jobNumber.append(srno)
    
    # sorting
    # for i in range(totalJobs):
        # for j in range(i, totalJobs):
            # if((ATlist[j] < ATlist[i]) or (ATlist[j] == ATlist[i] and BTlist[j] > BTlist[i])):
                # ATlist[j], ATlist[i] = ATlist[i], ATlist[j]
                # BTlist[j], BTlist[i] = BTlist[i], BTlist[j]
                # IOBTlist[j], IOBTlist[i] = IOBTlist[i], IOBTlist[j]
                # BT2list[j], BT2list[i] = BT2list[i], BT2list[j]
                # jobNumber[j], jobNumber[i] = jobNumber[i], jobNumber[j]
    
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
    BTlistbefore = []
    startedAt = []
    started = []

    for i in range(totalJobs):
        CTlist.append(0)
        TATlist.append(0)
        WTlist.append(0)
        RTlist.append(0)
        BTlistbefore.append(BTlist[i])
        startedAt.append(-1)
        started.append(False)
        #self.JOBqueue.append(jobNumber[i])

    currTime = 0
    totalTAT = 0
    totalWT = 0
    totalRT = 0
    completed = 0
    JobTemp = []
    ReadyTemp = []
    CPUTemp = []
    IOTemp = []
    IODeviceTemp = []
    TerminatedTemp = []
    StateTemp = []
    PercTemp = []
    CStime = self.ContextSwitchSelector.value()
    CStimeIO = self.ContextSwitchSelector.value()
    if(self.ModeNonPreemptive.isChecked()):
        TQtime = 1
        TQtimeIO = 1
    else:
        TQtime = 0
        TQtimeIO = 0

    templen = self.JobTable.rowCount()
    for i in range(templen):
        PercTemp.append("0%")
    self.setPerclist(PercTemp)
    self.storedPercentage.append(PercTemp)
    templen = self.JobTable.rowCount()
    for i in range(templen):
        StateTemp.append("Job")
    self.setStatelist(StateTemp)
    self.storedState.append(StateTemp)

    for i in range(totalJobs):
        JobTemp.append(jobNumber[i])
    
    while(completed != totalJobs):
        
        IOCSdone = False
        """ print('Time: ' + str(currTime))
        print('------- START -------')
        print('Job: ' + str(JobTemp))
        print('Ready: ' + str(ReadyTemp))
        print('CPU: ' + str(CPUTemp))
        print('IOQueue: ' + str(IOTemp))
        print('IO: ' + str(IODeviceTemp))
        print('Terminated: ' + str(TerminatedTemp)) """

        self.CGTableJobs.append('X')
        self.CGTableTimer.append(currTime + 1)
        self.IOCGTableJobs.append('X')
        self.IOCGTableTimer.append(currTime + 1)

        # if any job has arrived, remove them from job queue and add them in ready queue
        for i in range(totalJobs):
            if(ATlist[jobNumber[i]] == currTime and (not started[jobNumber[i]])):
                ReadyTemp.append(deepcopy(jobNumber[i]))
                for j in range(len(JobTemp)):
                    if(JobTemp[j] == jobNumber[i]):
                        JobTemp.pop(j)
                        break
        
        # sorting the ready Queue according to longest job
        for i in range(len(ReadyTemp)):
            for j in range(i, len(ReadyTemp)):
                if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                    if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                    if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                    if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                    if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]

        # sorting the IO queue according to longest job
        for i in range(len(IOTemp)):
            for j in range(i, len(IOTemp)):
                if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                    if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                    if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                    if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                    if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]

        # if any job has done with IO, check for BT2
        if(len(IODeviceTemp) != 0):
            TQtimeIO -= 1
            IOBTlist[IODeviceTemp[0]] -= 1
            # check if IO is finished!
            if(IOBTlist[IODeviceTemp[0]] == 0):
                # check if it has BT2
                if(BT2list[IODeviceTemp[0]] == 0):
                    # remove it from IO Device and move it terminated
                    if(CStimeIO == self.ContextSwitchSelector.value()):
                        CTlist[IODeviceTemp[0]] = currTime
                        TATlist[IODeviceTemp[0]] = CTlist[IODeviceTemp[0]] - ATlist[IODeviceTemp[0]]
                        WTlist[IODeviceTemp[0]] = TATlist[IODeviceTemp[0]] - BTlist[IODeviceTemp[0]]
                        RTlist[IODeviceTemp[0]] = startedAt[IODeviceTemp[0]] - ATlist[IODeviceTemp[0]]
                        totalTAT += TATlist[IODeviceTemp[0]]
                        totalWT += WTlist[IODeviceTemp[0]]
                        totalRT += RTlist[IODeviceTemp[0]]
                        completed += 1
                        TerminatedTemp.append(deepcopy(IODeviceTemp[0]))
                        IODeviceTemp.pop(0)
                        TQtimeIO = 1
                        if(CStimeIO != 0):
                            CStimeIO -= 1
                            self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = 'C'
                            IOCSdone = True
                        else:
                            # add next job to IO
                            if(len(IOTemp) != 0):
                                # sorting the IO queue according to longest job
                                for i in range(len(IOTemp)):
                                    for j in range(i, len(IOTemp)):
                                        if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                            if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                        elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                            if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                        elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                            if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                        elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                            if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IOTemp[0]
                                IODeviceTemp.append(deepcopy(IOTemp[0]))
                                IOTemp.pop(0)
                    elif(CStimeIO == 0):
                        IOCSdone = True
                        CStimeIO = self.ContextSwitchSelector.value()
                        # add next job to IO
                        if(len(IOTemp) != 0):
                            # sorting the IO queue according to longest job
                            for i in range(len(IOTemp)):
                                for j in range(i, len(IOTemp)):
                                    if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                        if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                        if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                        if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                        if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IOTemp[0]
                            IODeviceTemp.append(deepcopy(IOTemp[0]))
                            IOTemp.pop(0)
                    else:
                        IOCSdone = True
                        self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = 'C'
                        CStimeIO -= 1
                else:
                    if(CStimeIO == self.ContextSwitchSelector.value()):
                        # remove it from IO Device and move it to ready Queue
                        ReadyTemp.append(deepcopy(IODeviceTemp[0]))
                        IODeviceTemp.pop(0)
                        TQtimeIO = 1
                        if(CStimeIO != 0):
                            IOCSdone = True
                            CStimeIO -= 1
                            self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = 'C'
                        else:
                            # add next job to IO
                            if(len(IOTemp) != 0):
                                # sorting the IO queue according to longest job
                                for i in range(len(IOTemp)):
                                    for j in range(i, len(IOTemp)):
                                        if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                            if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                        elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                            if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                        elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                            if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                        elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                            if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                                IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IOTemp[0]
                                IODeviceTemp.append(deepcopy(IOTemp[0]))
                                IOTemp.pop(0)
                    elif(CStimeIO == 0):
                        IOCSdone = True
                        CStimeIO = self.ContextSwitchSelector.value()
                        # add next job to IO
                        if(len(IOTemp) != 0):
                            # sorting the IO queue according to longest job
                            for i in range(len(IOTemp)):
                                for j in range(i, len(IOTemp)):
                                    if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                        if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                        if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                        if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                        if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IOTemp[0]
                            IODeviceTemp.append(deepcopy(IOTemp[0]))
                            IOTemp.pop(0)
                    else:
                        IOCSdone = True
                        CStimeIO -= 1
                        self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = 'C'
            else:
                self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IODeviceTemp[0]
                if(TQtimeIO == 0):
                    # append the job in cpu to ready and make IO Device blank
                    IOTemp.append(deepcopy(IODeviceTemp[0]))
                    IODeviceTemp.pop(0)
                    if(CStimeIO != 0):
                        CStimeIO -= 1
                        self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = 'C'
                    else:
                        # switching due to time quantum
                        CStimeIO = self.ContextSwitchSelector.value()
                        # sorting the IO queue according to longest job
                        for i in range(len(IOTemp)):
                            for j in range(i, len(IOTemp)):
                                if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                    if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                    if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                    if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                    if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                        IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                        IODeviceTemp.append(deepcopy(IOTemp[0]))
                        IOTemp.pop(0)
                        self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IODeviceTemp[0]
                    
                    TQtimeIO = 1
        else:
            TQtimeIO = 1
            # check if any other job is available for IO
            if(CStimeIO == self.ContextSwitchSelector.value()):
                # if there is any job available for CPU, move it from ready to CPU
                if(len(IOTemp) != 0):
                    # sorting the IO queue according to longest job
                    for i in range(len(IOTemp)):
                        for j in range(i, len(IOTemp)):
                            if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                    self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IOTemp[0]
                    IODeviceTemp.append(deepcopy(IOTemp[0]))
                    IOTemp.pop(0)
            elif(CStimeIO == 0):
                IOCSdone = True
                CStimeIO = self.ContextSwitchSelector.value()
                # add next process
                if(len(IOTemp) != 0):
                    # sorting the IO queue according to longest job
                    for i in range(len(IOTemp)):
                        for j in range(i, len(IOTemp)):
                            if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                    IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                    self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IOTemp[0]
                    IODeviceTemp.append(deepcopy(IOTemp[0]))
                    IOTemp.pop(0)
            else:
                IOCSdone = True
                CStimeIO -= 1
                self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = 'C'

        # if any job is there in cpu and the BT is finished, check for IO else move to terminated
        if(len(CPUTemp) != 0):
            if(BTlist[CPUTemp[0]] != 0):
                BTlist[CPUTemp[0]] -= 1
            else:
                BT2list[CPUTemp[0]] -= 1
            TQtime -= 1
            # if BT is over 
            if(BTlist[CPUTemp[0]] == 0):
                # if there is no IOBT
                if(IOBTlist[CPUTemp[0]] == 0):
                    # if there is no BT2
                    if(BT2list[CPUTemp[0]] == 0):
                        # remove the job from cpu and send it to terminated queue
                        if(CStime == self.ContextSwitchSelector.value()):
                            CTlist[CPUTemp[0]] = currTime
                            TATlist[CPUTemp[0]] = CTlist[CPUTemp[0]] - ATlist[CPUTemp[0]]
                            WTlist[CPUTemp[0]] = TATlist[CPUTemp[0]] - BTlist[CPUTemp[0]]
                            RTlist[CPUTemp[0]] = startedAt[CPUTemp[0]] - ATlist[CPUTemp[0]]
                            totalTAT += TATlist[CPUTemp[0]]
                            totalWT += WTlist[CPUTemp[0]]
                            totalRT += RTlist[CPUTemp[0]]
                            completed += 1
                            TerminatedTemp.append(deepcopy(CPUTemp[0]))
                            CPUTemp.pop(0)
                            TQtime = 1
                            if(CStime != 0):
                                CStime -= 1
                                self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'
                            else:
                                # add next process
                                if(len(ReadyTemp) != 0):
                                    # sorting the ready Queue according to longest job
                                    for i in range(len(ReadyTemp)):
                                        for j in range(i, len(ReadyTemp)):
                                            if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                                if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                            elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                                if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                                if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                                if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                    self.CGTableJobs[len(self.CGTableJobs)-1] = ReadyTemp[0]
                                    CPUTemp.append(deepcopy(ReadyTemp[0]))
                                    ReadyTemp.pop(0)
                        elif(CStime == 0):
                            CStime = self.ContextSwitchSelector.value()
                            # add next process
                            if(len(ReadyTemp) != 0):
                                # sorting the ready Queue according to longest job
                                for i in range(len(ReadyTemp)):
                                    for j in range(i, len(ReadyTemp)):
                                        if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                            if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                            if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                            if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                            if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                self.CGTableJobs[len(self.CGTableJobs)-1] = ReadyTemp[0]
                                CPUTemp.append(deepcopy(ReadyTemp[0]))
                                ReadyTemp.pop(0)
                        else:
                            CStime -= 1
                            self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'
                    else:
                        item = self.JobTable.item(CPUTemp[0], 4)
                        BT2curr = item.text()
                        if(int(BT2curr) == BT2list[CPUTemp[0]]):
                            # remove the job from cpu and send it to ready queue
                            ReadyTemp.append(deepcopy(CPUTemp[0]))
                            CPUTemp.pop(0)
                            if(CStime != 0):
                                CStime -= 1
                                self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'
                            else:
                                # switching due to time quantum
                                CStimeIO = self.ContextSwitchSelector.value()
                                # sorting the ready Queue according to longest job
                                for i in range(len(ReadyTemp)):
                                    for j in range(i, len(ReadyTemp)):
                                        if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                            if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                            if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                            if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                            if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                CPUTemp.append(deepcopy(ReadyTemp[0]))
                                ReadyTemp.pop(0)
                                self.CGTableJobs[len(self.CGTableJobs)-1] = CPUTemp[0]
                                
                            TQtime = 1
                        else:
                            self.CGTableJobs[len(self.CGTableJobs)-1] = CPUTemp[0]
                            if(TQtime == 0):
                                # remove job from CPU and send it to Ready queue
                                ReadyTemp.append(deepcopy(CPUTemp[0]))
                                CPUTemp.pop(0)
                                if(CStime != 0):
                                    CStime -= 1
                                    self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'
                                else:
                                    # switching due to time quantum
                                    CStimeIO = self.ContextSwitchSelector.value()
                                    # sorting the ready Queue according to longest job
                                    for i in range(len(ReadyTemp)):
                                        for j in range(i, len(ReadyTemp)):
                                            if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                                if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                            elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                                if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                                if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                                if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                    CPUTemp.append(deepcopy(ReadyTemp[0]))
                                    ReadyTemp.pop(0)
                                    self.CGTableJobs[len(self.CGTableJobs)-1] = CPUTemp[0]
                                
                                TQtime = 1
                else:
                    # check if IO device is available or not
                    # cs
                    if(CStime == self.ContextSwitchSelector.value()):
                        IOTemp.append(deepcopy(CPUTemp[0]))
                        CPUTemp.pop(0)    
                        TQtime = 1
                        if(CStime != 0):
                            CStime -= 1
                            self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'
                        else:
                            # add next process
                            if(len(ReadyTemp) != 0):
                                # sorting the ready Queue according to longest job
                                for i in range(len(ReadyTemp)):
                                    for j in range(i, len(ReadyTemp)):
                                        if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                            if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                            if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                            if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                        elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                            if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                                ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                self.CGTableJobs[len(self.CGTableJobs)-1] = ReadyTemp[0]
                                CPUTemp.append(deepcopy(ReadyTemp[0]))
                                ReadyTemp.pop(0)    
                    elif(CStime == 0):
                        CStime = self.ContextSwitchSelector.value()
                        # add next process
                        if(len(ReadyTemp) != 0):
                            # sorting the ready Queue according to longest job
                            for i in range(len(ReadyTemp)):
                                for j in range(i, len(ReadyTemp)):
                                    if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                        if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                            ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                    elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                        if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                            ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                    elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                        if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                            ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                    elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                        if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                            ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                            self.CGTableJobs[len(self.CGTableJobs)-1] = ReadyTemp[0]
                            CPUTemp.append(deepcopy(ReadyTemp[0]))
                            ReadyTemp.pop(0)
                    else:
                        CStime -= 1
                        self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'
                    # check if any other job is available for IO
                    if(CStimeIO == self.ContextSwitchSelector.value()):
                        if(len(IODeviceTemp) == 0):
                            # if IO is device is available , remove the job from cpu and send it to IO Device
                            # sorting the IO queue according to longest job
                            for i in range(len(IOTemp)):
                                for j in range(i, len(IOTemp)):
                                    if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                        if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                        if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                        if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                        if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            IODeviceTemp.append(deepcopy(IOTemp[0]))
                            IOTemp.pop(0)
                            self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IODeviceTemp[0]
                    elif(CStimeIO == 0 and (not IOCSdone)):
                        CStimeIO = self.ContextSwitchSelector.value()
                        # add next process
                        if(len(IODeviceTemp) != 0):
                            # sorting the IO queue according to longest job
                            for i in range(len(IOTemp)):
                                for j in range(i, len(IOTemp)):
                                    if(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] > 0):
                                        if(BTlist[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] > 0 and BTlist[IOTemp[j]] == 0):
                                        if(BTlist[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] > 0):
                                        if(BT2list[IOTemp[i]] < BTlist[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                                    elif(BTlist[IOTemp[i]] == 0 and BTlist[IOTemp[j]] == 0):
                                        if(BT2list[IOTemp[i]] < BT2list[IOTemp[j]]):
                                            IOTemp[i], IOTemp[j] = IOTemp[j], IOTemp[i]
                            self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = IOTemp[0]
                            IODeviceTemp.append(deepcopy(IOTemp[0]))
                            IOTemp.pop(0)
                    elif(not IOCSdone):
                        CStimeIO -= 1
                        self.IOCGTableJobs[len(self.IOCGTableJobs)-1] = 'C'
            else:
                self.CGTableJobs[len(self.CGTableJobs)-1] = CPUTemp[0]
                if(TQtime == 0):
                    # remove job from CPU and send it to Ready queue
                    ReadyTemp.append(deepcopy(CPUTemp[0]))
                    CPUTemp.pop(0)
                    if(CStime != 0):
                        CStime -= 1
                        self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'
                    else:
                        # switching due to time quantum
                        CStimeIO = self.ContextSwitchSelector.value()
                        # sorting the ready Queue according to longest job
                        for i in range(len(ReadyTemp)):
                            for j in range(i, len(ReadyTemp)):
                                if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                    if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                    if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                    if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                                elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                    if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                        ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                        CPUTemp.append(deepcopy(ReadyTemp[0]))
                        ReadyTemp.pop(0)
                        self.CGTableJobs[len(self.CGTableJobs)-1] = CPUTemp[0]
                    
                    TQtime = 1
        else:
            TQtime = 1
            if(CStime == self.ContextSwitchSelector.value()):
                # if there is any job available for CPU, move it from ready to CPU
                if(len(ReadyTemp) != 0):
                    # sorting the ready Queue according to longest job
                    for i in range(len(ReadyTemp)):
                        for j in range(i, len(ReadyTemp)):
                            if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                            elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                    self.CGTableJobs[len(self.CGTableJobs)-1] = ReadyTemp[0]
                    CPUTemp.append(deepcopy(ReadyTemp[0]))
                    ReadyTemp.pop(0)
            elif(CStime == 0):
                CStime = self.ContextSwitchSelector.value()
                # add next process
                if(len(ReadyTemp) != 0):
                    # sorting the ready Queue according to longest job
                    for i in range(len(ReadyTemp)):
                        for j in range(i, len(ReadyTemp)):
                            if(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] > 0):
                                if(BTlist[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                            elif(BTlist[ReadyTemp[i]] > 0 and BTlist[ReadyTemp[j]] == 0):
                                if(BTlist[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] > 0):
                                if(BT2list[ReadyTemp[i]] < BTlist[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                            elif(BTlist[ReadyTemp[i]] == 0 and BTlist[ReadyTemp[j]] == 0):
                                if(BT2list[ReadyTemp[i]] < BT2list[ReadyTemp[j]]):
                                    ReadyTemp[i], ReadyTemp[j] = ReadyTemp[j], ReadyTemp[i]
                    self.CGTableJobs[len(self.CGTableJobs)-1] = ReadyTemp[0]
                    CPUTemp.append(deepcopy(ReadyTemp[0]))
                    ReadyTemp.pop(0)
            else:
                CStime -= 1
                self.CGTableJobs[len(self.CGTableJobs)-1] = 'C'

        currTime += 1

        self.JOBqueue.append(deepcopy(JobTemp))
        self.READYqueue.append(deepcopy(ReadyTemp))
        self.inCPU.append(deepcopy(CPUTemp))
        self.IOqueue.append(deepcopy(IOTemp))
        self.inIO.append(deepcopy(IODeviceTemp))
        self.TERMINATEDqueue.append(deepcopy(TerminatedTemp))

        for i in range(totalJobs):
            totalBT = 0
            for j in range(2,5):
                item = self.JobTable.item(i, j)
                valueHere = item.text()
                totalBT += int(valueHere)
            perc = float(float(totalBT - (BTlist[i] + IOBTlist[i] + BT2list[i])) / totalBT) * 100.0
            if(totalBT == (BTlist[i] + IOBTlist[i] + BT2list[i] + 1) and startedAt[i] == -1):
                startedAt[i] = currTime - 2
            perc = round(perc, 2)
            PercTemp[i] = str(perc) + "%"
            for j in range(len(JobTemp)):
                if(JobTemp[j] == i):
                    StateTemp[i] = "Job"
                    break
            for j in range(len(ReadyTemp)):
                if(ReadyTemp[j] == i):
                    StateTemp[i] = "Ready"
                    break
            for j in range(len(CPUTemp)):
                if(CPUTemp[j] == i):
                    StateTemp[i] = "CPU"
                    break
            for j in range(len(IOTemp)):
                if(IOTemp[j] == i):
                    StateTemp[i] = "IO Queue"
                    break
            for j in range(len(IODeviceTemp)):
                if(IODeviceTemp[j] == i):
                    StateTemp[i] = "IO Device"
                    break
            for j in range(len(TerminatedTemp)):
                if(TerminatedTemp[j] == i):
                    StateTemp[i] = "Terminated"
                    break
        
        self.storedPercentage.append(deepcopy(PercTemp))
        self.storedState.append(deepcopy(StateTemp))


        print('------- END OF LOOP -------')
        print('JobTemp: ' + str(JobTemp))
        print('self.JOBqueue: ' + str(self.JOBqueue))
        """ print('------- END -------')
        print('Job: ' + str(JobTemp))
        print('Ready: ' + str(ReadyTemp))
        print('CPU: ' + str(CPUTemp))
        print('IOQueue: ' + str(IOTemp))
        print('IO: ' + str(IODeviceTemp))
        print('Terminated: ' + str(TerminatedTemp)) """

    for i in range(totalJobs):
        PercTemp = "100%"
        StateTemp = "Terminated"
    
    self.storedPercentage.append(deepcopy(PercTemp))
    self.storedState.append(deepcopy(StateTemp))

    # removing the extra 'X' from the end of Gantt Chart
    while(self.IOCGTableJobs[len(self.IOCGTableJobs)-1] == 'X' or self.IOCGTableJobs[len(self.IOCGTableJobs)-1] == 'C'):
        print(self.IOCGTableJobs)
        self.IOCGTableJobs.pop(len(self.IOCGTableJobs)-1)
        self.IOCGTableTimer.pop(len(self.IOCGTableTimer)-1)
    while(self.CGTableJobs[len(self.CGTableJobs)-1] == 'X' or self.CGTableJobs[len(self.CGTableJobs)-1] == 'C'):
        print(self.CGTableJobs)
        self.CGTableJobs.pop(len(self.CGTableJobs)-1)
        self.CGTableTimer.pop(len(self.CGTableTimer)-1)
    
    # setting the gantt chart
    print('------- GANTT CHART -------')
    print(self.CGTableJobs)
    print(self.CGTableTimer)
    self.GanttChartTable.setColumnCount(len(self.CGTableJobs))
    for i in range(len(self.CGTableJobs)):
        if(self.CGTableJobs[i] != 'C' and self.CGTableJobs[i] != 'X'):
            item = QtWidgets.QTableWidgetItem(str(int(self.CGTableJobs[i])+1))
        else:
            item = QtWidgets.QTableWidgetItem(str(self.CGTableJobs[i]))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        if(self.CGTableJobs[i] != 'C' and self.CGTableJobs[i] != 'X'):
            item.setBackground(QtGui.QColor(
                    self.rgbRed[int(self.CGTableJobs[i])], self.rgbGreen[int(self.CGTableJobs[i])], self.rgbBlue[int(self.CGTableJobs[i])]))
            item.setForeground(QtGui.QColor(0, 0, 0))
        self.GanttChartTable.setItem(0, i, item)
        item = QtWidgets.QTableWidgetItem(str(i+1))
        item.setTextAlignment(
            QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        if(self.CGTableJobs[i] != 'C' and self.CGTableJobs[i] != 'X'):
            item.setBackground(QtGui.QColor(
                    self.rgbRed[int(self.CGTableJobs[i])], self.rgbGreen[int(self.CGTableJobs[i])], self.rgbBlue[int(self.CGTableJobs[i])]))
            item.setForeground(QtGui.QColor(0, 0, 0))
        self.GanttChartTable.setItem(1, i, item)


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
    
        
    # sorting back
    """ for i in range(totalJobs):
        for j in range(i, totalJobs):
            if(jobNumber[j] < jobNumber[i]):
                ATlist[j], ATlist[i] = ATlist[i], ATlist[j]
                BTlist[j], BTlist[i] = BTlist[i], BTlist[j]
                CTlist[j], CTlist[i] = CTlist[i], CTlist[j]
                TATlist[j], TATlist[i] = TATlist[i], TATlist[j]
                WTlist[j], WTlist[i] = WTlist[i], WTlist[j]
                RTlist[j], RTlist[i] = RTlist[i], RTlist[j]
                jobNumber[j], jobNumber[i] = jobNumber[i], jobNumber[j] """

    self.setCTlist(CTlist)
    self.setTATlist(TATlist)
    self.setWTlist(WTlist)
    self.setRTlist(RTlist)

    self.AvgTAT.setText(str(round(totalTAT/totalJobs, 5)))
    self.AvgWT.setText(str(round(totalWT/totalJobs, 5)))
    self.AvgRT.setText(str(round(totalRT/totalJobs, 5)))

    # Store total Time took to execute program.
    self.totalTimeOfExecuting = int( self.GanttChartTable.item(1, self.GanttChartTable.columnCount() - 1).text() )