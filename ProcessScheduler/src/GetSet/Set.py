from PyQt5 import QtCore, QtGui, QtWidgets

def setCTlist(self, CTlist):
    totalRows = self.JobTable.rowCount()

    col = 5
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        item.setText(str(CTlist[row]))

def setTATlist(self, TATlist):
    totalRows = self.JobTable.rowCount()

    col = 6
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        item.setText(str(TATlist[row]))

def setWTlist(self, WTlist):
    totalRows = self.JobTable.rowCount()

    col = 7
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        item.setText(str(WTlist[row]))

def setRTlist(self, RTlist):
    totalRows = self.JobTable.rowCount()

    col = 8
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        item.setText(str(RTlist[row]))

def setPerclist(self, Perclist):
    totalRows = self.JobTable.rowCount()
    
    col = 9
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        item.setText(str(Perclist[row]))


def setStatelist(self, Statelist):
    totalRows = self.JobTable.rowCount()

    col = 10
    for row in range(totalRows):
        item = self.JobTable.item(row, col)
        item.setText(str(Statelist[row]))

# Function to set items widget in each cell of table and align them.

def setWidgetsInCellsAndAlign(self):

    rows = self.JobTable.rowCount()
    rows = int(rows)
    cols = self.JobTable.columnCount()

    if(self.fromImport):
        self.previousRows = 0

    for col in range(cols):
        for row in range(self.previousRows,rows):
            #self.JobTable.setItemDelegateForColumn(col, DoubleOnlyDelegate(self.MainWindow))
            item = QtWidgets.QTableWidgetItem("")
            item.setTextAlignment(
                QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            #self.JobTable.setValidator(QtGui.QIntValidator(1,1000))
            self.JobTable.setItem(
                row, col, item)
    
    self.previousRows = rows


# Function for setting non editable columns whichever requried.

def setNonEditableColumns(self):

    rows = self.JobTable.rowCount()
    cols = self.JobTable.columnCount()

    if self.TypeWithoutIOBT.isChecked():
        for row in range(rows):
            item = self.JobTable.item(row, 3)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item = self.JobTable.item(row, 4)
            item.setFlags(QtCore.Qt.ItemIsEnabled)

    if(str(self.AlgoSelector.currentText()) != "Priority"):
        for row in range(rows):
            item = self.JobTable.item(row, 0)
            item.setFlags(QtCore.Qt.ItemIsEnabled)

    for col in range(5, cols):
        for row in range(rows):
            item = self.JobTable.item(row, col)
            item.setFlags(QtCore.Qt.ItemIsEnabled)