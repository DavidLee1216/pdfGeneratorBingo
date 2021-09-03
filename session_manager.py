from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sys, os
import images
import gui
import pdfWriter
import sessionDataDlg
import re
import mysql.connector

class SessionManager(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SessionManager, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgb(0, 104, 55);")
        self.writeFirstLine(self)
        self.writeSecondLine(self)
        self.writeThirdLine(self)
        self.writeFourthLine(self)
        self.writeFifthLine(self)
        self.writeSixthLine(self)
        
    def writeFirstLine(self, MainWindow):
        self.title_label = QtWidgets.QLabel(MainWindow)
        self.title_label.setGeometry(QtCore.QRect(80, 30, 900, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(100)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(255, 196, 37);border: none;")
        self.title_label.setText("Session Manager (90 number Game)")
        
        self.firstline_layout_widget = QtWidgets.QWidget(MainWindow)
        self.firstline_layout_widget.setGeometry(QtCore.QRect(50, 110, 800, 50))
        self.firstline_layout_widget.setObjectName("firstline_layout_widget")

        self.firstline_layout = QtWidgets.QHBoxLayout(self.firstline_layout_widget)
        self.firstline_layout_label = QtWidgets.QLabel(self.firstline_layout_widget)
        font = QtGui.QFont()
        # font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.firstline_layout_label.setFont(font)
        self.firstline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.firstline_layout_label.setText("Create a Name for the Session to Print Books for:")

        self.firstline_layout_edit = QtWidgets.QLineEdit(self.firstline_layout_widget)
        self.firstline_layout_edit.setObjectName("firstline_layout_edit")
        font = QtGui.QFont()
        # font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.firstline_layout_edit.setFont(font)
        self.firstline_layout_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 30px;")

        self.firstline_layout.addWidget(self.firstline_layout_label)
        self.firstline_layout.addWidget(self.firstline_layout_edit)
        
    def writeSecondLine(self, MainWindow):
        self.secondline_layout_widget = QtWidgets.QWidget(MainWindow)
        self.secondline_layout_widget.setGeometry(QtCore.QRect(50, 150, 800, 40))
        self.secondline_layout_widget.setObjectName("secondline_layout_widget")

        self.secondline_layout = QtWidgets.QHBoxLayout(self.secondline_layout_widget)
        self.secondline_layout_label = QtWidgets.QLabel(self.secondline_layout_widget)
        font = QtGui.QFont()
        # font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.secondline_layout_label.setFont(font)
        self.secondline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.secondline_layout_label.setText("(For example - Wednesday Morning, Thursday Evening etc.)")
        
        self.secondline_layout.addWidget(self.secondline_layout_label)
        
    def writeThirdLine(self, MainWindow):
        self.thirdline_layout_widget = QtWidgets.QWidget(MainWindow)
        self.thirdline_layout_widget.setGeometry(QtCore.QRect(40, 190, 850, 300))
        self.thirdline_layout_widget.setObjectName("thirdline_layout_widget")
        self.thirdline_layout = QtWidgets.QHBoxLayout(self.thirdline_layout_widget)
        self.setContentsMargins(0, 0, 0, 0)
        self.thirdline_layout_label = QtWidgets.QLabel(self.thirdline_layout_widget)
        font = QtGui.QFont()
        # font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.thirdline_layout_label.setFont(font)
        self.thirdline_layout_label.setStyleSheet("color: rgb(0, 0, 0); border: none; padding-bottom: 250;")
        self.thirdline_layout_label.setText("Please choose the date on which session will play:")
        
        self.calendar = QtWidgets.QCalendarWidget(self.thirdline_layout_widget)
        self.calendar.setStyleSheet("background-color: rgb(191, 239, 215); color: rgb(0,0,0);")
        
        self.thirdline_layout.addWidget(self.thirdline_layout_label)
        self.thirdline_layout.addWidget(self.calendar)

    def writeFourthLine(self, MainWindow):
        self.fourthline_layout_widget = QtWidgets.QWidget(MainWindow)
        self.fourthline_layout_widget.setGeometry(QtCore.QRect(50, 490, 800, 40))
        self.fourthline_layout_widget.setObjectName("fourthline_layout_widget")

        self.fourthline_layout = QtWidgets.QHBoxLayout(self.fourthline_layout_widget)
        self.fourthline_layout_label = QtWidgets.QLabel(self.fourthline_layout_widget)
        font = QtGui.QFont()
        # font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.fourthline_layout_label.setFont(font)
        self.fourthline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.fourthline_layout_label.setText("Will this be played at a specific time? Choose:")
        
        self.fourthline_layout.addWidget(self.fourthline_layout_label)

    def writeFifthLine(self, MainWindow):
        # self.fifthline_layout_widget = QtWidgets.QWidget(MainWindow)
        # self.fifthline_layout_widget.setGeometry(QtCore.QRect(40, 530, 700, 40))
        # self.fifthline_layout_widget.setObjectName("fifthline_layout_widget")
        
        # self.fifthline_layout = QtWidgets.QHBoxLayout(self.fifthline_layout_widget)

        self.anytime_checkbox = QtWidgets.QCheckBox("Anytime on the date", MainWindow)
        self.anytime_checkbox.setStyleSheet("QCheckBox::indicator { width: 40px; height: 40px;}")
        self.anytime_checkbox.setStyleSheet("color: rgb(255, 255, 255);")
        self.anytime_checkbox.setGeometry(QtCore.QRect(50, 530, 300, 40))
        self.anytime_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft) 
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.anytime_checkbox.setFont(font)
        self.anytime_checkbox.setChecked(True)
        self.anytimeChecked = True
        self.anytime_checkbox.stateChanged.connect(self.setAnytimeCheckBox)
        
        self.specifictime_checkbox = QtWidgets.QCheckBox("Specific time on the date", MainWindow)
        self.specifictime_checkbox.setStyleSheet("color: rgb(255, 255, 255); margin-left: 20px;")
        self.specifictime_checkbox.setGeometry(QtCore.QRect(380, 530, 350, 40))
        self.specifictime_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft) 
        self.specifictime_checkbox.setFont(font)
        self.specifictime_checkbox.stateChanged.connect(self.setSpecifictimeCheckBox)
        
        # self.fifthline_layout.addWidget(self.anytime_checkbox)
        # self.fifthline_layout.addWidget(self.specifictime_checkbox)
        
    def setAnytimeCheckBox(self, state):
        if state==QtCore.Qt.Checked:
            self.anytimeChecked = True
            self.specifictime_checkbox.setChecked(False)
        else:
            self.anytimeChecked = False
            self.specifictime_checkbox.setChecked(True)
    
    def setSpecifictimeCheckBox(self, state):
        if state==QtCore.Qt.Checked:
            self.specificChecked = True
            self.anytime_checkbox.setChecked(False)
        else:
            self.specificChecked = False
            self.anytime_checkbox.setChecked(True)
            
    def writeSixthLine(self, MainWindow):
        self.sixthline_from_label = QtWidgets.QLabel(MainWindow)
        self.sixthline_from_label.setGeometry(QtCore.QRect(380, 580, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.sixthline_from_label.setFont(font)
        self.sixthline_from_label.setStyleSheet("color: rgb(255, 255, 255);border: none;")
        self.sixthline_from_label.setText("From:")
        self.sixthline_to_label = QtWidgets.QLabel(MainWindow)
        self.sixthline_to_label.setGeometry(QtCore.QRect(630, 580, 40, 40))
        self.sixthline_to_label.setFont(font)
        self.sixthline_to_label.setStyleSheet("color: rgb(255, 255, 255);border: none;")
        self.sixthline_to_label.setText("To:")

        self.time_from = QtWidgets.QTimeEdit(MainWindow)
        self.time_from.setGeometry(QtCore.QRect(460, 580, 150, 70))
        self.time_from.setFont(font)
        self.time_from.setStyleSheet("background-color: rgb(254, 224, 17);")

        self.time_to = QtWidgets.QTimeEdit(MainWindow)
        self.time_to.setGeometry(QtCore.QRect(680, 580, 150, 70))
        self.time_to.setFont(font)
        self.time_to.setStyleSheet("background-color: rgb(254, 224, 17);")
        
        self.session_btn = gui.PicButton(QtGui.QPixmap('./images/create_session_button.png'), MainWindow)
        self.session_btn.setGeometry(QtCore.QRect(670, 700, 200, 40))
        self.session_btn.clicked.connect(self.create_session)
        
        self.session_data_btn = gui.PicButton(QtGui.QPixmap('./images/session_data_button.png'), MainWindow)
        self.session_data_btn.setGeometry(QtCore.QRect(370, 700, 200, 40))
        self.session_data_btn.clicked.connect(self.manage_session)

    def check_session_existance(self, session_name, today_str):
        mydb = gui.mydb
        mycursor = mydb.cursor()
        query = "select id from game_session_info where date >= '{}' and session_name='{}'".format(today_str, session_name)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
            pdfWriter.show_message('warning', 'Session name already exists.')
            return True
        return False
    
    @classmethod
    def check_session_name_validation(cls, session_name):
        regex = re.compile('@_!#$%^&*()<>?/\|~:;\'"')
        if regex.search(session_name) == None:
            return True
        else:
            return False
    
    def create_session(self):
        session_name = self.firstline_layout_edit.text()
        session_name = session_name.replace("'", "\\'")
        today = datetime.date.today()
        today_str = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
        if session_name=='':
            pdfWriter.show_message('warning', 'Session name can not be empty.')
            return
        if self.check_session_existance(session_name, today_str)==True:
            pdfWriter.show_message('warning', 'Session name for today already exists.')
            return
        if self.check_session_name_validation(session_name)==False:
            pdfWriter.show_message('warning', 'Session name includes special characters. Change the session name.')
            return
        if today > self.calendar.selectedDate():
            pdfWriter.show_message('warning', 'Can\'t set past date')
            return
        session_date = str(self.calendar.selectedDate().year())+'-'+str(self.calendar.selectedDate().month())+'-'+str(self.calendar.selectedDate().day())
        anytime_flag = 1 if self.anytimeChecked==True else 0
        time_from = "{:02d}".format(self.time_from.time().hour())+":{:02d}".format(self.time_from.time().minute())+':'+'00'
        time_to = "{:02d}".format(self.time_to.time().hour())+":{:02d}".format(self.time_from.time().minute())+':'+'00'
        mydb = gui.mydb
        mycursor = gui.mydb.cursor()
        self.addSessionToDatabase(mydb, mycursor, session_name, session_date, anytime_flag, time_from, time_to)
        pdfWriter.show_message('OK', 'Successfully created session.')
        
    def manage_session(self):
        Dialog = QtWidgets.QDialog()
        ui = sessionDataDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()

    def addSessionToDatabase(self, mydb, mycursor, session_name, session_date, anytime_flag, time_from, time_to):
        query = "insert into game_session_info (id, session_name, date, anytime_flag, time_from, time_to) values(NULL, '{}', '{}', '{}', '{}', '{}')".format(session_name, session_date, anytime_flag, time_from, time_to)
        mycursor.execute(query)
        mydb.commit()

        
        
