from PyQt5 import QtCore, QtGui, QtWidgets

def getPriorityList(self):
    Prioritylist = []
    totalRows = self.JobTable.rowCount()

    col = 0
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        valueHere = item.text()
        Prioritylist.append(int(valueHere))

    return Prioritylist

def getATList(self):

    ATlist = []
    totalRows = self.JobTable.rowCount()
    col = 1
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        valueHere = item.text()
        ATlist.append(int(valueHere))

    return ATlist

def getBTList(self):
    BTlist = []
    totalRows = self.JobTable.rowCount()

    col = 2
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        valueHere = item.text()
        BTlist.append(int(valueHere))

    return BTlist

def getIOBTList(self):
    IOBTlist = []
    totalRows = self.JobTable.rowCount()

    col = 3
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        valueHere = item.text()
        IOBTlist.append(int(valueHere))

    return IOBTlist

def getBT2List(self):
    BTlist = []
    totalRows = self.JobTable.rowCount()

    col = 4
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        valueHere = item.text()
        BTlist.append(int(valueHere))

    return BTlist

def getPercList(self):
    Perclist = []
    totalRows = self.JobTable.rowCount()

    col = 9
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        valueHere = item.text()
        Perclist.append(valueHere)

    return Perclist

def getStateList(self):
    Statelist = []
    totalRows = self.JobTable.rowCount()

    col = 10
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        valueHere = item.text()
        Statelist.append(valueHere)

    return Statelist