from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt

def graphBtnHandler(self):

    numberOfJobs = int(self.JobNo.text())

    #numberOfJobs = 5

    #self.CGTableJobs = ['X',1,1,2,2,3,3,4,4,4,5,5,5,5,1,1,2,3,4,5,5]
    #self.CGTableTimer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21] 
    #self.IOCGTableJobs = ['X','X','X',1,1,2,'X',3,3,3,4,4,'X','X','X','X','X','X','X','X','X']
    #self.IOCGTableTimer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

    print('------ Graph -----')
    print(self.IOCGTableJobs)

    JobStartTime = {}
    JobEndTime = {}

    if(self.TypeWithoutIOBT.isChecked()):
        for i in range(len(self.CGTableJobs)):
            currentJob = self.CGTableJobs[i]
            currentTime = self.CGTableTimer[i]
            if type(currentJob) is int:
                if currentJob not in JobStartTime:
                    JobStartTime[currentJob] = [currentTime]
                    JobEndTime[currentJob] = [currentTime]
                else:
                    flag = False
                    for j in range(len(JobEndTime[currentJob])):
                        if JobEndTime[currentJob][j] == currentTime-1:
                            JobEndTime[currentJob][j] = JobEndTime[currentJob][j] + 1
                            flag = True
                            break
                        if flag == False:
                            JobStartTime[currentJob].append(currentTime)
                            JobEndTime[currentJob].append(currentTime)

        fig, ax = plt.subplots()

        plt.title('Jobs vs in CPU time', color='white')
        plt.xlabel('Time', color='white')
        plt.ylabel('Jobs', color='white')

        plt.xlim(0, max(self.CGTableTimer))
        plt.xticks(self.CGTableTimer)
        plt.ylim(0, numberOfJobs+1)

        for i in JobStartTime:
            for j in range(len(JobStartTime[i])):
                start = JobStartTime[i][j]
                end = JobEndTime[i][j]
                x_values = [start-1, end]
                y_values = [i, i]
                plt.plot(x_values, y_values, color=self.colorHexCode[i-1])

        ax.set_facecolor('#232629')
        fig.patch.set_facecolor('#232629')

        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        plt.show(block=False)
    
    else:    
        
        for i in range(len(self.CGTableJobs)):
            currentJob = self.CGTableJobs[i]
            currentTime = self.CGTableTimer[i]
            if type(currentJob) is int:
                currentJob = int(currentJob) + 1
                if currentJob not in JobStartTime:
                    JobStartTime[currentJob] = [currentTime]
                    JobEndTime[currentJob] = [currentTime]
                else:
                    flag = False
                    for j in range(len(JobEndTime[currentJob])):
                        if JobEndTime[currentJob][j] == currentTime-1:
                            JobEndTime[currentJob][j] = JobEndTime[currentJob][j] + 1
                            flag = True
                            break
                        if flag == False:
                            JobStartTime[currentJob].append(currentTime)
                            JobEndTime[currentJob].append(currentTime)

        fig, ax = plt.subplots()

        plt.title('Jobs vs in CPU time', color='white')
        plt.xlabel('Time', color='white')
        plt.ylabel('Jobs', color='white')

        plt.xlim(0, max(self.CGTableTimer))
        plt.xticks(self.CGTableTimer)
        plt.ylim(0, numberOfJobs+1)

        for i in JobStartTime:
            for j in range(len(JobStartTime[i])):
                start = JobStartTime[i][j]
                end = JobEndTime[i][j]
                x_values = [start-1, end]
                y_values = [i, i]
                plt.plot(x_values, y_values, color=self.colorHexCode[i-1])

        ax.set_facecolor('#232629')
        fig.patch.set_facecolor('#232629')

        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        plt.show(block=False)

        JobStartTimeio = {}
        JobEndTimeio = {}

        for i in range(len(self.IOCGTableJobs)):
            currentJobio = self.IOCGTableJobs[i]
            currentTimeio = self.IOCGTableTimer[i]
            if type(currentJobio) is int:
                currentJobio = int(currentJobio) + 1
                if currentJobio not in JobStartTimeio:
                    JobStartTimeio[currentJobio] = [currentTimeio]
                    JobEndTimeio[currentJobio] = [currentTimeio]
                else:
                    flagio = False
                    for j in range(len(JobEndTimeio[currentJobio])):
                        if JobEndTimeio[currentJobio][j] == currentTimeio-1:
                            JobEndTimeio[currentJobio][j] = JobEndTimeio[currentJobio][j] + 1
                            flagio = True
                            break
                        if flagio == False:
                            JobStartTimeio[currentJobio].append(currentTimeio)
                            JobEndTimeio[currentJobio].append(currentTimeio)

        fig2, ax2 = plt.subplots()

        plt.title('Jobs vs in IO DEVICE time', color='white')
        plt.xlabel('Time', color='white')
        plt.ylabel('Jobs', color='white')

        plt.xlim(0, max(self.IOCGTableTimer))
        plt.xticks(self.IOCGTableTimer)
        plt.ylim(0, numberOfJobs+1)

        for i in JobStartTimeio:
            for j in range(len(JobStartTimeio[i])):
                startio = JobStartTimeio[i][j]
                endio = JobEndTimeio[i][j]
                x_valuesio = [startio-1, endio]
                y_valuesio = [i, i]
                plt.plot(x_valuesio, y_valuesio, color=self.colorHexCode[i-1])

        ax2.set_facecolor('#232629')
        fig2.patch.set_facecolor('#232629')

        ax2.spines['bottom'].set_color('white')
        ax2.spines['top'].set_color('white')
        ax2.spines['right'].set_color('white')
        ax2.spines['left'].set_color('white')

        ax2.tick_params(axis='x', colors='white')
        ax2.tick_params(axis='y', colors='white')

        plt.show(block=False)

