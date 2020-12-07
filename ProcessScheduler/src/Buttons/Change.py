from PyQt5 import QtCore, QtGui, QtWidgets

def GCchangeBtnHandler(self):
    
    if(self.GCchangeBtn.text() == 'IO Gantt Chart'):
        # set IO GC chart
        self.GCchangeBtn.setText('CPU Gantt Chart')
        self.GanttChartLabel.setText('Gantt Chart (IO)')
        self.GanttChartTable.setColumnCount(len(self.IOCGTableJobs))
        for i in range(len(self.IOCGTableJobs)):
            if(self.IOCGTableJobs[i] != 'C' and self.IOCGTableJobs[i] != 'X'):
                item = QtWidgets.QTableWidgetItem(str(int(self.IOCGTableJobs[i])+1))
            else:
                item = QtWidgets.QTableWidgetItem(str(self.IOCGTableJobs[i]))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            if(self.IOCGTableJobs[i] != 'C' and self.IOCGTableJobs[i] != 'X'):
                item.setBackground(QtGui.QColor(
                        self.rgbRed[int(self.IOCGTableJobs[i])], self.rgbGreen[int(self.IOCGTableJobs[i])], self.rgbBlue[int(self.IOCGTableJobs[i])]))
                item.setForeground(QtGui.QColor(0, 0, 0))
            self.GanttChartTable.setItem(0, i, item)
            item = QtWidgets.QTableWidgetItem(str(i+1))
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            if(self.IOCGTableJobs[i] != 'C' and self.IOCGTableJobs[i] != 'X'):
                item.setBackground(QtGui.QColor(
                        self.rgbRed[int(self.IOCGTableJobs[i])], self.rgbGreen[int(self.IOCGTableJobs[i])], self.rgbBlue[int(self.IOCGTableJobs[i])]))
                item.setForeground(QtGui.QColor(0, 0, 0))
            self.GanttChartTable.setItem(1, i, item)
    else:
        # set CPU GC chart
        self.GCchangeBtn.setText('IO Gantt Chart')
        self.GanttChartLabel.setText('Gantt Chart (CPU)')
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