#!/usr/bin/python3


# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import db_worker
import mail
import json_csv as js

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from tinydb import TinyDB, Query

db_groups = TinyDB('../DBs/groups.json')
db_courses = TinyDB('../DBs/courses.json')
db_empls = TinyDB('../DBs/employees.json')
db_points = TinyDB('../DBs/points.json')
db_wrkflg = TinyDB('../DBs/work_flags.json')

"""
NOTES
columns and rows... 

columns should be calculate like this (from JSON stuct):
    |name|-----------INFO---------------

rows should be calculate only from ID (len(json))
"""

#Some generated code
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Quit_btn.setGeometry(QtCore.QRect(980, 670, 90, 28))
        self.Quit_btn.setObjectName("Quit_btn")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 0, 1081, 661))
        self.tabs.setObjectName("tabs")
        self.groups_tab = QtWidgets.QWidget()
        self.groups_tab.setObjectName("groups_tab")
        self.delGroup_btn = QtWidgets.QPushButton(self.groups_tab)
        self.delGroup_btn.setGeometry(QtCore.QRect(100, 600, 90, 28))
        self.delGroup_btn.setObjectName("delGroup_btn")

        #######################################
        #Table groups
        self.group_tbl = QtWidgets.QTableWidget(self.groups_tab)
        self.group_tbl.setGeometry(QtCore.QRect(0, 11, 800, 581))
        self.group_tbl.setObjectName("group_tbl")
        self.group_tbl.setColumnCount(self.ColumnInit(db_groups))
        self.group_tbl.setRowCount(self.RowsInit(db_groups))
        
        self.group_tbl.setHorizontalHeaderLabels([\
                'Zkratka',\
                'Ročník',\
                'Semestr',\
                'Studentů',\
                'Forma',\
                'Stupeň',\
                'Jazyk'\
             ])

        self.TableFeeder(self.group_tbl,db_groups) #Let's feed table with data
        
        self.group_tbl.resizeColumnsToContents()
        self.group_tbl.resizeRowsToContents()
        #######################################

        self.addGroup_btn = QtWidgets.QPushButton(self.groups_tab)
        self.addGroup_btn.setGeometry(QtCore.QRect(0, 600, 90, 28))
        self.addGroup_btn.setObjectName("addGroup_btn")
        self.tabs.addTab(self.groups_tab, "")
        self.courses_tab = QtWidgets.QWidget()
        self.courses_tab.setObjectName("courses_tab")

        #######################################
        #Table courses  
        self.courses_tbl = QtWidgets.QTableWidget(self.courses_tab)
        self.courses_tbl.setGeometry(QtCore.QRect(0, 10, 800, 581))
        self.courses_tbl.setObjectName("courses_tbl")
        self.courses_tbl.setColumnCount(self.ColumnInit(db_courses))
        self.courses_tbl.setRowCount(self.RowsInit(db_courses))
        self.courses_tbl.setHorizontalHeaderLabels([\
                'Zkratka',\
                'Týdny',\
                'Přednášky',\
                'Cvičení',\
                'Semináře',\
                'Zakončení',\
                'Jazyk',\
                'Kapacita',\
                'Skupiny'\
            ])

        self.TableFeeder(self.courses_tbl,db_courses) #Let's feed table with data
        
        self.courses_tbl.resizeColumnsToContents()
        self.courses_tbl.resizeRowsToContents()
        #######################################

        self.addLec_btn = QtWidgets.QPushButton(self.courses_tab)
        self.addLec_btn.setGeometry(QtCore.QRect(0, 600, 90, 28))
        self.addLec_btn.setObjectName("addLec_btn")
        self.delLec_btn = QtWidgets.QPushButton(self.courses_tab)
        self.delLec_btn.setGeometry(QtCore.QRect(100, 600, 90, 28))
        self.delLec_btn.setObjectName("delLec_btn")
        self.tabs.addTab(self.courses_tab, "courses_tab")

        self.employes_tab = QtWidgets.QWidget()
        self.employes_tab.setObjectName("employes_tab")
        #######################################
        #Table workers
        self.employee_tbl = QtWidgets.QTableWidget(self.employes_tab)
        self.employee_tbl.setGeometry(QtCore.QRect(0, 10, 1000, 581))
        self.employee_tbl.setObjectName("employee_tbl")
        self.employee_tbl.setColumnCount(self.ColumnInit(db_empls))
        self.employee_tbl.setRowCount(self.RowsInit(db_empls))
        
        self.employee_tbl.setHorizontalHeaderLabels([\
                'Jméno',\
                'Příjmení',\
                'Celé jméno',\
                'Prac. e-mail',\
                'Soukr. e-mail',\
                'Body bez EN výuky',\
                'Body s EN výukou',\
                'Doktorské \n studium',\
                'Úvazek',\
                'Štítky',\
            ])

        self.TableFeeder(self.employee_tbl,db_empls) #Let's feed table with data
        
        self.employee_tbl.resizeColumnsToContents()
        self.employee_tbl.resizeRowsToContents()
        #######################################
        
        self.addEmpl_btn = QtWidgets.QPushButton(self.employes_tab)
        self.addEmpl_btn.setGeometry(QtCore.QRect(0, 600, 90, 28))
        self.addEmpl_btn.setObjectName("addEmpl_btn")
        self.delEmpl_btn = QtWidgets.QPushButton(self.employes_tab)
        self.delEmpl_btn.setGeometry(QtCore.QRect(100, 600, 90, 28))
        self.delEmpl_btn.setObjectName("delEmpl_btn")
        self.tabs.addTab(self.employes_tab, "")
        self.flags_tab = QtWidgets.QWidget()
        self.flags_tab.setObjectName("flags_tab")

        #######################################
        #Table flags
        self.flags_tbl = QtWidgets.QTableWidget(self.flags_tab)
        self.flags_tbl.setGeometry(QtCore.QRect(0, 10, 800, 581))
        self.flags_tbl.setObjectName("flags_tbl")

        self.flags_tbl.setColumnCount(self.ColumnInit(db_wrkflg))
        self.flags_tbl.setRowCount(self.RowsInit(db_wrkflg))
        self.flags_tbl.setHorizontalHeaderLabels([\
                'Štítek',\
                'Zaměstnanec',\
                'Předmět',\
                'Typ štítku',\
                'Studenti',\
                'Hodin',\
                'Týdny',\
                'Jazyk',\
                'Body',\
            ])

        self.TableFeeder(self.flags_tbl,db_wrkflg) #Let's feed table with data
        
        self.flags_tbl.resizeColumnsToContents()
        self.flags_tbl.resizeRowsToContents()
        #######################################

        self.addFlag_btn = QtWidgets.QPushButton(self.flags_tab)
        self.addFlag_btn.setGeometry(QtCore.QRect(0, 600, 90, 28))
        self.addFlag_btn.setObjectName("addFlag_btn")
        self.delFlag_btn = QtWidgets.QPushButton(self.flags_tab)
        self.delFlag_btn.setGeometry(QtCore.QRect(100, 600, 90, 28))
        self.delFlag_btn.setObjectName("delFlag_btn")
        self.tabs.addTab(self.flags_tab, "flags_tab")
        self.points_tab = QtWidgets.QWidget()
        self.points_tab.setObjectName("points_tab")

        #######################################
        #Table points
        self.points_tbl = QtWidgets.QTableWidget(self.points_tab)
        self.points_tbl.setGeometry(QtCore.QRect(0, 10, 800, 581))
        self.points_tbl.setObjectName("points_tbl")
        self.points_tbl.resizeColumnsToContents()
        self.points_tbl.resizeRowsToContents()
        #######################################
        
        self.tabs.addTab(self.points_tab, "points_tab")

        #######################################
        #Table points
        self.email_tab = QtWidgets.QWidget()
        self.email_tab.setObjectName("email_tab")
        self.send_emails = QtWidgets.QPushButton(self.email_tab)
        self.send_emails.setGeometry(QtCore.QRect(0, 600, 90, 28))
        self.send_emails.setObjectName("send_emails")
        
        self.email_list = QtWidgets.QColumnView(self.email_tab)
        self.email_list.setGeometry(QtCore.QRect(0, 10, 800, 581))
        self.email_list.setObjectName("email_list")
        self.tabs.addTab(self.email_tab, "email_tab")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.export_xls = QtWidgets.QPushButton(self.email_tab)
        self.export_xls.setGeometry(QtCore.QRect(90, 600, 90, 28))
        self.export_xls.setObjectName("Export")

        self.retranslateUi(MainWindow)
        self.addGroup_btn.clicked['bool'].connect(self.Click_addGroup_btn)
        self.addEmpl_btn.clicked['bool'].connect(self.Click_addEmpl_btn)
        self.addFlag_btn.clicked['bool'].connect(self.Click_addFlag_btn)
        self.addLec_btn.clicked['bool'].connect(self.Click_addLec_btn)
        self.delEmpl_btn.clicked['bool'].connect(self.Click_delEmpl_btn)
        self.delFlag_btn.clicked['bool'].connect(self.Click_delFlag_btn)
        self.delGroup_btn.clicked['bool'].connect(self.Click_delGroup_btn)
        self.delLec_btn.clicked['bool'].connect(self.Click_delLec_btn)
        self.send_emails.clicked['bool'].connect(self.Click_send_emails)
        self.export_xls.clicked['bool'].connect(self.Click_export_xls)
        self.Quit_btn.clicked['bool'].connect(self.Quit_btn_clicked)

        self.courses_tbl.itemChanged.connect(self.CoursesChanged)
        self.flags_tbl.itemChanged.connect(self.FlagsChanged)
        self.points_tbl.itemChanged.connect(self.PointsChanged)
        self.employee_tbl.itemChanged.connect(self.EmployeeChanged)
        self.group_tbl.itemChanged.connect(self.GroupChanged)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Softik pro tajemnika"))
        self.Quit_btn.setText(_translate("MainWindow", "Quit"))
        self.delGroup_btn.setText(_translate("MainWindow", "Odebrat"))
        self.addGroup_btn.setText(_translate("MainWindow", "Přidat"))
        self.tabs.setTabText(self.tabs.indexOf(self.groups_tab), _translate("MainWindow", "Skupiny"))
        self.addLec_btn.setText(_translate("MainWindow", "Přidat"))
        self.delLec_btn.setText(_translate("MainWindow", "Odebrat"))
        self.tabs.setTabText(self.tabs.indexOf(self.courses_tab), _translate("MainWindow", "Předměty"))
        self.addEmpl_btn.setText(_translate("MainWindow", "Přidat"))
        self.delEmpl_btn.setText(_translate("MainWindow", "Odebrat"))
        self.tabs.setTabText(self.tabs.indexOf(self.employes_tab), _translate("MainWindow", "Zaměstnanci"))
        self.addFlag_btn.setText(_translate("MainWindow", "Přidat"))
        self.delFlag_btn.setText(_translate("MainWindow", "Odebrat"))
        self.tabs.setTabText(self.tabs.indexOf(self.flags_tab), _translate("MainWindow", "Pracovní štítky"))
        self.tabs.setTabText(self.tabs.indexOf(self.points_tab), _translate("MainWindow", "Body"))
        self.send_emails.setText(_translate("MainWindow", "Send"))
        self.export_xls.setText(_translate("MainWindow", "Export"))
        self.tabs.setTabText(self.tabs.indexOf(self.email_tab), _translate("MainWindow", "e-mail"))

#End of generated code 
    def RowsInit(self, data):
        file = data.all()
        return(len(file))

    def ColumnInit(self, data):
        file = data.all()
        return(len(file[0]['info']))

    def TableFeeder(self,table,data):
        file = data.all()

        for y in range(len(file)):
            column = 0
            for x in file[y]['info']:
                val = file[y]['info'][x]
                table.setItem(y,column,QTableWidgetItem(str(val)))
                column+=1

        return(print("ghettoFeeder"))

################################################################################
#Cell changed
    def CoursesChanged(self):
        idx = self.courses_tbl.currentRow()
        idy = self.courses_tbl.currentColumn()
        itm = self.courses_tbl.item(idx,idy).text()
        
        db_worker.update_db(db_courses, idx, idy, itm)
        print('Row: ', idx, 'Column: ', idy, 'Item:', str(itm))


    def FlagsChanged(self):
        idx = self.flags_tbl.currentRow()
        idy = self.flags_tbl.currentColumn()
        itm = self.flags_tbl.item(idx,idy).text()
        
        db_worker.update_db(db_wrkflg, idx, idy, itm)        
        print('Row: ', idx, 'Column: ', idy, 'Item:', itm)


    def PointsChanged(self):
        idx = self.points_tbl.currentRow()
        idy = self.points_tbl.currentColumn()
        itm = self.points_tbl.item(idx,idy).text()

        db_worker.update_db(db_points, idx, idy, itm)        
        print('Row: ', idx, 'Column: ', idy, 'Item:', itm) 


    def EmployeeChanged(self):
        idx = self.employee_tbl.currentRow()
        idy = self.employee_tbl.currentColumn()
        itm = self.employee_tbl.item(idx,idy).text()
        
        db_worker.update_db(db_empls, idx, idy, itm)        
        print('Row: ', idx, 'Column: ', idy, 'Item:', itm)
    
    
    def GroupChanged(self):
        idx = self.group_tbl.currentRow()
        idy = self.group_tbl.currentColumn()
        itm = self.group_tbl.item(idx,idy).text()
        
        db_worker.update_db(db_groups, idx, idy, itm)        
        print('Row: ', idx, 'Column: ', idy, 'Item:', itm)


################################################################################
#ButtonActions
    def Click_addGroup_btn(self):
        print("addGroup_btn.click")

        #Call function associated to button > render output (for actual values)
        #db_worker.test() #imported test fnc >> only for testing purpose
        
        #create empty record to DB
        db_worker.create_group('NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL'\
                                )
        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(0)
    
    def Click_addEmpl_btn(self):
        print("addEmpl_btn.click")
        #Call function associated to button > render output (for actual values)

        db_worker.create_empl('NULL',\
                              'NULL',\
                              'NULL',\
                              'NULL',\
                              'NULL',\
                              'NULL',\
                              'NULL',\
                              'NULL',\
                              'NULL'\
                              )

        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(2)
    
    def Click_addFlag_btn(self):
        print("addFlag_btn.click")
        #Call function associated to button > render output (for actual values)
        #db_worker.test() #imported test fnc >> only for testing purpose

        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(3)
    
    def Click_addLec_btn(self):
        print("addLec_btn.click")
        #Call function associated to button > render output (for actual values)
        #db_worker.test() #imported test fnc >> only for testing purpose
        

        db_worker.create_course('NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL',\
                                'NULL'\
                                )


        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(1)
    
    def Click_delEmpl_btn(self):
        print("delEmpl_btn.click")
        #Call function associated to button > render output (for actual values)
        #db_worker.test() #imported test fnc >> only for testing purpose
        idx = self.employee_tbl.currentRow()
        db_worker.delete_record(db_empls,idx)

        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(2)
    
    def Click_delFlag_btn(self):
        print("delFlag_btn.click")
        #Call function associated to button > render output (for actual values)

        idx = self.flags_tbl.currentRow()
        print(idx)

        db_worker.delete_record(db_wrkflg,idx)

        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(3)
    
    def Click_delGroup_btn(self):
        print("delGroup_btn.click")

        idx = self.group_tbl.currentRow()
        db_worker.delete_record(db_groups,idx)

        print(idx)
        #db_worker.delete_record(db_groups,idx) #upravit mazani v DB podle indexu
        
        #Call function associated to button > render output (for actual values)
        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(0)
    
    def Click_delLec_btn(self):
        print("delLec_btn.click")

        #Call function associated to button > render output (for actual values)
        #db_worker.test() #imported test fnc >> only for testing purpose
        idx = self.courses_tbl.currentRow()
        db_worker.delete_record(db_courses,idx)

        print(idx)

        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(1)
    
    def Click_send_emails(self):
        print("send_emails.click")
        mail.send_email()
        #Call function associated to button > render output (for actual values)
        #db_worker.test() #imported test fnc >> only for testing purpose

        self.setupUi(MainWindow)
        self.tabs.setCurrentIndex(5)

    def Click_export_xls(self):
        js.Export()

    def Quit_btn_clicked(self):
        sys.exit(app.exec_())  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())