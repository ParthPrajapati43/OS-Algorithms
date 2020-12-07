from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

def importBtnHandler(self):
    self.fromImport = True
    data=pd.read_csv('inputs.csv')
    r=data.shape[0]
    r=int(r)
    data.set_index('Jobs',inplace=True)
    i=0
    j=0
    
    rows = r
    self.JobNo.setValue(rows)
    #self.previousRows = rows
    self.JobTable.setRowCount(rows)

    for i in range(rows):
        item = QtWidgets.QTableWidgetItem("Job "+str(i+1))
        item.setForeground(QtGui.QColor(0, 0, 0))
        item.setBackground(QtGui.QColor(
            self.rgbRed[i], self.rgbGreen[i], self.rgbBlue[i]))

        self.JobTable.setVerticalHeaderItem(i, item)

    # Call function to set items widget in each cell of table and align them.
    self.setWidgetsInCellsAndAlign()

    # Call function to set Non editable columns, whichever required.
    self.setNonEditableColumns()


    algo=self.AlgoSelector.currentText()
    #algo_type=self.TypeWithIOBT.clicked.connect(self.type_IOBT())
    
    
    i=0
    if self.TypeWithIOBT.isChecked():
        if algo!='Priority':
            columns=['AT','BT','IOBT','BT2']
            for jobs in data.index:
                for feature in columns:
                    item = QtWidgets.QTableWidgetItem()
                    q=data.loc[jobs,feature]
                    item.setText(str(q))
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.JobTable.setItem(i,(j%4)+1,item)
                    j+=1
                i+=1
        else:
            i=0
            j=0
            for jobs in data.index:
                columns=['Priority','AT','BT','IOBT','BT2']   
                for feature in columns:
                    item = QtWidgets.QTableWidgetItem()
                    q=data.loc[jobs,feature]
                    item.setText(str(q))
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.JobTable.setItem(i,(j%5),item)
                    j+=1
                i+=1
    if self.TypeWithoutIOBT.isChecked():
        i=0
        j=0
        if algo!='Priority':
            columns=['AT','BT']
            for jobs in data.index:
                for feature in columns:
                    item = QtWidgets.QTableWidgetItem()
                    q=data.loc[jobs,feature]
                    item.setText(str(q))
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.JobTable.setItem(i,(j%2)+1,item)
                    j+=1
                i+=1
        else:
            for jobs in data.index:
                columns=['Priority','AT','BT']        
                for feature in columns:
                    item = QtWidgets.QTableWidgetItem()
                    q=data.loc[jobs,feature]
                    item.setText(str(q))
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.JobTable.setItem(i,(j%3),item)
                    j+=1
                i+=1