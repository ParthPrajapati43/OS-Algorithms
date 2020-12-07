from PyQt5 import QtCore, QtGui, QtWidgets
import xlsxwriter
from win32com import client
import os
import datetime
import subprocess

def downloadBtnHandler(self):

    # creating the object
    workbook = xlsxwriter.Workbook("download.xlsx")

    # object used to add new worksheet
    worksheet = workbook.add_worksheet()
    
    # setting the column width parameters: (start col no, end col no, width)
    worksheet.set_column(0,500,2)

    # creating a parameter for formating the text
    bold_format = workbook.add_format({'bold':True})
    merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'})

    worksheet.merge_range('A1:AG1', 'PROCESS SCHEDULER', merge_format)

    worksheet.merge_range('A3:F3', 'Algorithm:', bold_format)
    worksheet.merge_range('G3:L3', str(self.AlgoSelector.currentText()))
    
    worksheet.merge_range('A4:F4', 'Mode:', bold_format)
    if(self.ModeNonPreemptive.isChecked()):
        worksheet.merge_range('G4:L4', 'Non Preemptive')
    else:
        worksheet.merge_range('G4:L4', 'Preemptive')
    
    worksheet.merge_range('A5:F5', 'Type:', bold_format)
    if(self.TypeWithoutIOBT.isChecked()):
        worksheet.merge_range('G5:L5', 'Without IOBT')
    else:
        worksheet.merge_range('G5:L5', 'With IOBT')
    
    worksheet.merge_range('A6:F6', 'Context Switch:', bold_format)
    worksheet.merge_range('G6:L6', str(self.ContextSwitchSelector.value()) + ' seconds')
    
    worksheet.merge_range('A7:F7', 'Time Quantum:', bold_format)
    worksheet.merge_range('G7:L7', str(self.TimeQuantumSelector.value()) + ' seconds')
    
    worksheet.merge_range('A9:C9', 'Job ID', bold_format)
    worksheet.merge_range('D9:F9', 'Priority', bold_format)
    worksheet.merge_range('G9:H9', 'AT', bold_format)
    worksheet.merge_range('I9:J9', 'BT', bold_format)
    worksheet.merge_range('K9:L9', 'IOBT', bold_format)
    worksheet.merge_range('M9:N9', 'BT', bold_format)
    worksheet.merge_range('O9:P9', 'CT', bold_format)
    worksheet.merge_range('Q9:R9', 'TAT', bold_format)
    worksheet.merge_range('S9:T9', 'WT', bold_format)
    worksheet.merge_range('U9:V9', 'RT', bold_format)
    worksheet.merge_range('W9:Y9', '%', bold_format)
    worksheet.merge_range('Z9:AB9', 'State', bold_format)

    for i in range(self.JobNo.value()):
        worksheet.merge_range('A' + str(i+10) + ':C' + str(i+10), 'Job ' + str(i+1), workbook.add_format({'bg_color':self.colorHexCode[i]}))
        item = self.JobTable.item(i, 0)
        value = item.text()
        worksheet.merge_range('D' + str(i+10) + ':F' + str(i+10), value)
        item = self.JobTable.item(i, 1)
        value = item.text()
        worksheet.merge_range('G' + str(i+10) + ':H' + str(i+10), value)
        item = self.JobTable.item(i, 2)
        value = item.text()
        worksheet.merge_range('I' + str(i+10) + ':J' + str(i+10), value)
        item = self.JobTable.item(i, 3)
        value = item.text()
        worksheet.merge_range('K' + str(i+10) + ':L' + str(i+10), value)
        item = self.JobTable.item(i, 4)
        value = item.text()
        worksheet.merge_range('M' + str(i+10) + ':N' + str(i+10), value)
        item = self.JobTable.item(i, 5)
        value = item.text()
        worksheet.merge_range('O' + str(i+10) + ':P' + str(i+10), value)
        item = self.JobTable.item(i, 6)
        value = item.text()
        worksheet.merge_range('Q' + str(i+10) + ':R' + str(i+10), value)
        item = self.JobTable.item(i, 7)
        value = item.text()
        worksheet.merge_range('S' + str(i+10) + ':T' + str(i+10), value)
        item = self.JobTable.item(i, 8)
        value = item.text()
        worksheet.merge_range('U' + str(i+10) + ':V' + str(i+10), value)
        item = self.JobTable.item(i, 9)
        value = item.text()
        worksheet.merge_range('W' + str(i+10) + ':Y' + str(i+10), value)
        item = self.JobTable.item(i, 10)
        value = item.text()
        worksheet.merge_range('Z' + str(i+10) + ':AB' + str(i+10), value)

    # avg. TAT
    worksheet.merge_range('A' + str(self.JobNo.value() + 11) + ':D' + str(self.JobNo.value() + 11), 'Avg. TAT:', bold_format)
    worksheet.merge_range('E' + str(self.JobNo.value() + 11) + ':K' + str(self.JobNo.value() + 11), str(self.AvgTAT.text()) + ' seconds')
    
    # avg. WT
    worksheet.merge_range('A' + str(self.JobNo.value() + 12) + ':D' + str(self.JobNo.value() + 12), 'Avg. WT:', bold_format)
    worksheet.merge_range('E' + str(self.JobNo.value() + 12) + ':K' + str(self.JobNo.value() + 12), str(self.AvgWT.text()) + ' seconds')

    # avg. RT
    worksheet.merge_range('A' + str(self.JobNo.value() + 13) + ':D' + str(self.JobNo.value() + 13), 'Avg. RT:', bold_format)    
    worksheet.merge_range('E' + str(self.JobNo.value() + 13) + ':K' + str(self.JobNo.value() + 13), str(self.AvgRT.text()) + ' seconds')
    
    worksheet.merge_range('A' + str(self.JobNo.value() + 15) + ':L' + str(self.JobNo.value() + 15), 'Gantt Chart (CPU)', bold_format)
    worksheet.merge_range('A' + str(self.JobNo.value() + 17) + ':B' + str(self.JobNo.value() + 17), 'Job', bold_format)
    worksheet.merge_range('A' + str(self.JobNo.value() + 18) + ':B' + str(self.JobNo.value() + 18), 'Time', bold_format)

    lastrow = self.JobNo.value() + 18
    checker=[]
    changed = False
    if(self.GCchangeBtn.text() != 'IO Gantt Chart'):
        self.GCchangeBtnHandler()
        changed = True
    for i in range(2):
        for j in range(1,len(self.CGTableJobs) + 1):
            item = self.GanttChartTable.item(i, j - 1)
            value = item.text()
            if(j > 31):
                colid = j % 31
                if(colid == 0):
                    colid = 31
                colid -= 1
                rowid = self.JobNo.value() + 16 + ((j-1)//31)*3
                lastrow = rowid
                if(i == 0):
                    checker.append(value)
                    if(value != 'C' and value != 'X'):
                        worksheet.write(rowid, colid, value, workbook.add_format({'bg_color':self.colorHexCode[int(value)-1]}))
                    else:
                        worksheet.write(rowid, colid, value)
                else:
                    if(checker[j-1] != 'C' and checker[j-1] != 'X'):
                        if(j > 99):
                            worksheet.write(rowid + 1, colid, value, workbook.add_format({'bg_color':self.colorHexCode[int(checker[j-1])-1], 'font_size':7}))
                        else:
                            worksheet.write(rowid + 1, colid, value, workbook.add_format({'bg_color':self.colorHexCode[int(checker[j-1])-1]}))
                    else:
                        if(j > 99):
                            worksheet.write(rowid + 1, colid, value, workbook.add_format({'font_size':7}))
                        else:
                            worksheet.write(rowid + 1, colid, value)    
            else:
                if(i == 0):
                    checker.append(value)
                    if(value != 'C' and value != 'X'):
                        worksheet.write(self.JobNo.value() + 16, j + 1, value, workbook.add_format({'bg_color':self.colorHexCode[int(value)-1]}))
                    else:
                        worksheet.write(self.JobNo.value() + 16, j + 1, value)
                else:
                    if(checker[j-1] != 'C' and checker[j-1] != 'X'):
                        worksheet.write(self.JobNo.value() + 17, j + 1, value, workbook.add_format({'bg_color':self.colorHexCode[int(checker[j-1])-1]}))
                    else:
                        worksheet.write(self.JobNo.value() + 17, j + 1, value)
    if(changed):
        self.GCchangeBtnHandler()
    
    if(self.TypeWithIOBT.isChecked()):
        lastrow += 2
        worksheet.merge_range('A' + str(lastrow + 2) + ':L' + str(lastrow + 2), 'Gantt Chart (IO)', bold_format)
        worksheet.merge_range('A' + str(lastrow + 4) + ':B' + str(lastrow + 4), 'Job', bold_format)
        worksheet.merge_range('A' + str(lastrow + 5) + ':B' + str(lastrow + 5), 'Time', bold_format)
        checker=[]
        changed = False
        if(self.GCchangeBtn.text() == 'IO Gantt Chart'):
            self.GCchangeBtnHandler()
            changed = True
        for i in range(2):
            for j in range(1,len(self.IOCGTableJobs) + 1):
                item = self.GanttChartTable.item(i, j - 1)
                value = item.text()
                if(j > 31):
                    colid = j % 31
                    if(colid == 0):
                        colid = 31
                    colid -= 1
                    rowid = lastrow + 3 + ((j-1)//31)*3
                    if(i == 0):
                        checker.append(value)
                        if(value != 'C' and value != 'X'):
                            worksheet.write(rowid, colid, value, workbook.add_format({'bg_color':self.colorHexCode[int(value)-1]}))
                        else:
                            worksheet.write(rowid, colid, value)
                    else:
                        if(checker[j-1] != 'C' and checker[j-1] != 'X'):
                            if(j > 99):
                                worksheet.write(rowid + 1, colid, value, workbook.add_format({'bg_color':self.colorHexCode[int(checker[j-1])-1], 'font_size':7}))
                            else:
                                worksheet.write(rowid + 1, colid, value, workbook.add_format({'bg_color':self.colorHexCode[int(checker[j-1])-1]}))
                        else:
                            if(j > 99):
                                worksheet.write(rowid + 1, colid, value, workbook.add_format({'font_size':7}))
                            else:
                                worksheet.write(rowid + 1, colid, value)    
                else:
                    if(i == 0):
                        checker.append(value)
                        if(value != 'C' and value != 'X'):
                            worksheet.write(lastrow + 3, j + 1, value, workbook.add_format({'bg_color':self.colorHexCode[int(value)-1]}))
                        else:
                            worksheet.write(lastrow + 3, j + 1, value)
                    else:
                        if(checker[j-1] != 'C' and checker[j-1] != 'X'):
                            worksheet.write(lastrow + 4, j + 1, value, workbook.add_format({'bg_color':self.colorHexCode[int(checker[j-1])-1]}))
                        else:
                            worksheet.write(lastrow + 4, j + 1, value)
        if(changed):
            self.GCchangeBtnHandler()        

    # closing (or maybe destroying) the object
    workbook.close()
    
    current_time = datetime.datetime.now() 
    nameoffile = str(self.AlgoSelector.currentText()) + "_" + str(current_time.day) + "_" + str(current_time.month) + "_" + str(current_time.year) + "__" + str(current_time.hour) + "_" + str(current_time.minute) + "_" + str(current_time.second) 

    xlApp = client.Dispatch("Excel.Application")
    fileadd = os.path.realpath(__file__)
    abspath = os.path.dirname(fileadd)
    abspath = abspath[:-(12)]
    books = xlApp.Workbooks.Open(str(abspath)+'\\download.xlsx')
    ws = books.Worksheets[0]
    ws.Visible = 1
    ws.ExportAsFixedFormat(0, str(abspath)+'\\'+str(nameoffile)+'.pdf')
    books.Close()
    
    openfile = str(abspath)+'\\'+str(nameoffile)+'.pdf'
    subprocess.Popen([openfile],shell=True) 