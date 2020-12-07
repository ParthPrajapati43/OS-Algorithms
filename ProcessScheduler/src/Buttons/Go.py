from PyQt5 import QtCore, QtGui, QtWidgets

def goBtnHandler(self):

    rows = self.JobNo.text()
    rows = int(rows)
    self.JobTable.setRowCount(rows)

    if(rows <= self.previousRows):
        self.previousRows = rows
        return

    for i in range(self.previousRows, rows):
        item = QtWidgets.QTableWidgetItem("Job "+str(i+1))
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setBackground(QtGui.QColor(
            self.rgbRed[i], self.rgbGreen[i], self.rgbBlue[i]))

        self.JobTable.setVerticalHeaderItem(i, item)
        
    # Call function to set items widget in each cell of table and align them.
    self.setWidgetsInCellsAndAlign()

    # Call function to set Non editable columns, whichever required.
    self.setNonEditableColumns()