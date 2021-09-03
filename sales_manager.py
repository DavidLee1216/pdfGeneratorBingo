from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import images
import datetime
import gui
import soldDataDlg
import pdfWriter

class SalesManager(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SalesManager, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.totalMoney = 0
        self.boardMargin = 20
        self.session_id = 0
        self.setStyleSheet("background-color: rgb(155, 97, 35);")
        self.writeFirstLine(self)
        self.writeSecondLine(self)
        self.writeThirdLine(self)
        self.writeFourthLine(self)
        self.writeFifthLine(self)
        self.writeSixthLine(self)
        self.writeSeventhLine(self)
        self.writeEighthLine(self)
        self.writeNinethLine(self)
        self.writePreprintedInfo(self)

    def loadSessions(self):
        self.session_ids = []
        mydb = gui.mydb
        mycursor = mydb.cursor()
        today = datetime.date.today()
        today_str = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
        query = "select * from game_session_info where date >= '{}'".format(today_str)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        self.session_combobox.clear()
        for result in myresult:
            self.session_combobox.addItem(result[1])
            self.session_ids.append(int(result[0]))
        if len(self.session_ids) > 0:
            self.session_id = self.session_ids[0]
            self.loadPrintInfo(self.session_id)

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
        self.title_label.setText("Sales Manager (90 number Game)")
        
        self.firstline_layout_label = QtWidgets.QLabel(MainWindow)
        self.firstline_layout_label.setGeometry(QtCore.QRect(370, 110, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.firstline_layout_label.setFont(font)
        self.firstline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.firstline_layout_label.setText("Select Session to Sell Books for:")

        self.session_combobox = QtWidgets.QComboBox(MainWindow)
        self.session_combobox.setGeometry(QtCore.QRect(700, 110, 210, 35))
        self.session_combobox.setObjectName("session_combobox")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.session_combobox.setFont(font)
        self.session_combobox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.session_combobox.currentIndexChanged.connect(self.session_combobox_changed)

    def session_combobox_changed(self, i):
        if len(self.session_ids) > 0 and i >= 0:
            self.session_id = self.session_ids[i]
            self.loadPrintInfo(self.session_id)
            
    def loadPrintInfo(self, session_id):
        self.preprintedModel.clear()
        self.preprintedModel.setHorizontalHeaderLabels(['kind', 'print id', 'from', 'to'])
        query = "select * from print_info where session_id='{}' and sold='0' order by id".format(session_id)
        mydb = gui.mydb
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myres = mycursor.fetchall()
        for res in myres:
            if res[2]==0:
                kind = "single"
            elif res[2]==1:
                kind = "double"
            else:
                kind = "sheet"
            print_id = str(res[0])
            print_from = str(res[3])
            print_to = str(res[4])
            self.preprintedModel.appendRow([QtGui.QStandardItem(kind), QtGui.QStandardItem(print_id), QtGui.QStandardItem(print_from), QtGui.QStandardItem(print_to)])
        self.preprintedInfoList.model().layoutChanged.emit()
        self.preprintedInfoList.setColumnWidth(0, 60)
        self.preprintedInfoList.setColumnWidth(1, 60)
        self.preprintedInfoList.setColumnWidth(2, 80)
        self.preprintedInfoList.setColumnWidth(3, 80)
        self.preprintedInfoList.setShowGrid(False)
        self.loadProductInfo()

    def writeSecondLine(self, MainWindow):
        self.secondline_layout_label = QtWidgets.QLabel(MainWindow)
        self.secondline_layout_label.setGeometry(QtCore.QRect(370, 150, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.secondline_layout_label.setFont(font)
        self.secondline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.secondline_layout_label.setText("Please enter price for single book")

        self.secondline_layout_edit = QtWidgets.QLineEdit(MainWindow)
        self.secondline_layout_edit.setGeometry(QtCore.QRect(700, 150, 210, 35))
        self.secondline_layout_edit.setObjectName("secondline_layout_edit")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.secondline_layout_edit.setFont(font)
        self.secondline_layout_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 30px;")

    def writeThirdLine(self, MainWindow):
        self.thirdline_layout_label = QtWidgets.QLabel(MainWindow)
        self.thirdline_layout_label.setGeometry(QtCore.QRect(370, 190, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.thirdline_layout_label.setFont(font)
        self.thirdline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.thirdline_layout_label.setText("Please enter price for double book")

        self.thirdline_layout_edit = QtWidgets.QLineEdit(MainWindow)
        self.thirdline_layout_edit.setGeometry(QtCore.QRect(700, 190, 210, 35))
        self.thirdline_layout_edit.setObjectName("thirdline_layout_edit")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.thirdline_layout_edit.setFont(font)
        self.thirdline_layout_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 30px;")
        
    def writeFourthLine(self, MainWindow):
        self.fourthline_layout_label = QtWidgets.QLabel(MainWindow)
        self.fourthline_layout_label.setGeometry(QtCore.QRect(370, 230, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.fourthline_layout_label.setFont(font)
        self.fourthline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.fourthline_layout_label.setText("Please enter price for single sheet")

        self.fourthline_layout_edit = QtWidgets.QLineEdit(MainWindow)
        self.fourthline_layout_edit.setGeometry(QtCore.QRect(700, 230, 210, 35))
        self.fourthline_layout_edit.setObjectName("fourthline_layout_edit")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.fourthline_layout_edit.setFont(font)
        self.fourthline_layout_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 30px;")

    def writeFifthLine(self, MainWindow):
        self.fifthline_layout_label = QtWidgets.QLabel(MainWindow)
        self.fifthline_layout_label.setGeometry(QtCore.QRect(370, 270, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.fifthline_layout_label.setFont(font)
        self.fifthline_layout_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.fifthline_layout_label.setText("Please enter the customers name:")

        self.fifthline_layout_edit = QtWidgets.QLineEdit(MainWindow)
        self.fifthline_layout_edit.setGeometry(QtCore.QRect(400, 310, 450, 35))
        self.fifthline_layout_edit.setObjectName("fifthline_layout_edit")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.fifthline_layout_edit.setFont(font)
        self.fifthline_layout_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 30px;")
        
    def writePreprintedInfo(self, MainWindow):
        self.preprintedInfoLabel = QtWidgets.QLabel(MainWindow)
        self.preprintedInfoLabel.setGeometry(QtCore.QRect(700, 345+self.boardMargin, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.preprintedInfoLabel.setFont(font)
        self.preprintedInfoLabel.setStyleSheet("background-color: rgb(179, 124, 58);")
        self.preprintedInfoLabel.setText("Pre Printed Info")
        
        self.preprintedInfoList = QtWidgets.QTableView(MainWindow)
        self.preprintedInfoList.setGeometry(QtCore.QRect(640, 390+self.boardMargin, 330, 310))
        self.preprintedModel = QtGui.QStandardItemModel()
        self.preprintedModel.setHorizontalHeaderLabels(['kind', 'print id', 'from', 'to'])
        self.preprintedInfoList.setModel(self.preprintedModel)
        self.preprintedInfoList.setColumnWidth(0, 60)
        self.preprintedInfoList.setColumnWidth(1, 60)
        self.preprintedInfoList.setColumnWidth(2, 80)
        self.preprintedInfoList.setColumnWidth(3, 80)
        self.preprintedInfoList.setShowGrid(False)
        self.preprintedInfoList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.preprintedInfoList.clicked.connect(self.getPreprintedInfo)

    def writeSixthLine(self, MainWindow):
        self.background_label = QtWidgets.QLabel(MainWindow)
        self.background_label.setGeometry(QtCore.QRect(370, 345+self.boardMargin, 610, 450))
        self.background_label.setStyleSheet("background-color: rgb(179, 124, 58);")
        
        self.Sixthline_layout_label = QtWidgets.QLabel(MainWindow)
        self.Sixthline_layout_label.setGeometry(QtCore.QRect(380, 360+self.boardMargin, 90, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.Sixthline_layout_label.setFont(font)
        self.Sixthline_layout_label.setStyleSheet("background-color: rgb(255, 255, 0); color: rgb(0, 0, 0);border: 1px solid black;")
        self.Sixthline_layout_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Sixthline_layout_label.setText("Pre printed\nSingle\nBook")
        
        # self.SixthEnterRange_label = QtWidgets.QLabel(MainWindow)
        # self.SixthEnterRange_label.setGeometry(QtCore.QRect(470, 350+self.boardMargin, 300, 40))
        # font = QtGui.QFont()
        # font.setPointSize(13)
        # font.setBold(True)
        # font.setWeight(50)
        # self.SixthEnterRange_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0); padding-left: 10px;")
        # self.SixthEnterRange_label.setFont(font)
        # self.SixthEnterRange_label.setText("Enter Range:")
        
        self.SixthFrom_label = QtWidgets.QLabel(MainWindow)
        self.SixthFrom_label.setGeometry(QtCore.QRect(470, 390+self.boardMargin, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.SixthFrom_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0);")
        self.SixthFrom_label.setAlignment(QtCore.Qt.AlignRight)
        self.SixthFrom_label.setFont(font)
        self.SixthFrom_label.setText("From:")

        self.single_from_edit = QtWidgets.QLineEdit(MainWindow)
        self.single_from_edit.setReadOnly(True)
        self.single_from_edit.setGeometry(QtCore.QRect(530, 390+self.boardMargin, 100, 30))
        self.single_from_edit.setObjectName("single_from_edit")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.single_from_edit.setFont(font)
        self.single_from_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 10px;")

        self.SixthTo_label = QtWidgets.QLabel(MainWindow)
        self.SixthTo_label.setGeometry(QtCore.QRect(470, 430+self.boardMargin, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.SixthTo_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0);")
        self.SixthTo_label.setAlignment(QtCore.Qt.AlignRight)
        self.SixthTo_label.setFont(font)
        self.SixthTo_label.setText("To:")

        self.single_to_edit = QtWidgets.QLineEdit(MainWindow)
        self.single_to_edit.setReadOnly(True)
        self.single_to_edit.setGeometry(QtCore.QRect(530, 430+self.boardMargin, 100, 30))
        self.single_to_edit.setObjectName("single_to_edit")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.single_to_edit.setFont(font)
        self.single_to_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 10px;")

    def writeSeventhLine(self, MainWindow):
        self.Seventhline_layout_label = QtWidgets.QLabel(MainWindow)
        self.Seventhline_layout_label.setGeometry(QtCore.QRect(380, 480+self.boardMargin, 90, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.Seventhline_layout_label.setFont(font)
        self.Seventhline_layout_label.setStyleSheet("background-color: rgb(237, 28, 36); color: rgb(0, 0, 0);border: 1px solid black;")
        self.Seventhline_layout_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Seventhline_layout_label.setText("Pre printed\nDouble\nBook")
        
        # self.SeventhEnterRange_label = QtWidgets.QLabel(MainWindow)
        # self.SeventhEnterRange_label.setGeometry(QtCore.QRect(470, 470+self.boardMargin, 300, 40))
        # font = QtGui.QFont()
        # font.setPointSize(13)
        # font.setBold(True)
        # font.setWeight(50)
        # self.SeventhEnterRange_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0); padding-left: 10px;")
        # self.SeventhEnterRange_label.setFont(font)
        # self.SeventhEnterRange_label.setText("Enter Range:")
        
        self.SeventhFrom_label = QtWidgets.QLabel(MainWindow)
        self.SeventhFrom_label.setGeometry(QtCore.QRect(470, 510+self.boardMargin, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.SeventhFrom_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0);")
        self.SeventhFrom_label.setAlignment(QtCore.Qt.AlignRight)
        self.SeventhFrom_label.setFont(font)
        self.SeventhFrom_label.setText("From:")

        self.double_from_edit = QtWidgets.QLineEdit(MainWindow)
        self.double_from_edit.setReadOnly(True)
        self.double_from_edit.setGeometry(QtCore.QRect(530, 510+self.boardMargin, 100, 30))
        self.double_from_edit.setObjectName("double_from_edit")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.double_from_edit.setFont(font)
        self.double_from_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 10px;")

        self.SeventhTo_label = QtWidgets.QLabel(MainWindow)
        self.SeventhTo_label.setGeometry(QtCore.QRect(470, 550+self.boardMargin, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.SeventhTo_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0);")
        self.SeventhTo_label.setAlignment(QtCore.Qt.AlignRight)
        self.SeventhTo_label.setFont(font)
        self.SeventhTo_label.setText("To:")

        self.double_to_edit = QtWidgets.QLineEdit(MainWindow)
        self.double_to_edit.setReadOnly(True)
        self.double_to_edit.setGeometry(QtCore.QRect(530, 550+self.boardMargin, 100, 30))
        self.double_to_edit.setObjectName("double_to_edit")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.double_to_edit.setFont(font)
        self.double_to_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 10px;")

    def writeEighthLine(self, MainWindow):
        self.Eighthline_layout_label = QtWidgets.QLabel(MainWindow)
        self.Eighthline_layout_label.setGeometry(QtCore.QRect(380, 600+self.boardMargin, 90, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.Eighthline_layout_label.setFont(font)
        self.Eighthline_layout_label.setStyleSheet("background-color: rgb(140, 198, 63); color: rgb(0, 0, 0);border: 1px solid black;")
        self.Eighthline_layout_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Eighthline_layout_label.setText("Pre printed\nSingle\nSheet")
        
        self.EighthEnterRange_label = QtWidgets.QLabel(MainWindow)
        self.EighthEnterRange_label.setGeometry(QtCore.QRect(470, 590+self.boardMargin, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.EighthEnterRange_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0); padding-left: 10px;")
        self.EighthEnterRange_label.setFont(font)
        self.EighthEnterRange_label.setText("Enter Range:")
        
        self.EighthFrom_label = QtWidgets.QLabel(MainWindow)
        self.EighthFrom_label.setGeometry(QtCore.QRect(470, 630+self.boardMargin, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.EighthFrom_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0);")
        self.EighthFrom_label.setAlignment(QtCore.Qt.AlignRight)
        self.EighthFrom_label.setFont(font)
        self.EighthFrom_label.setText("From:")

        self.sheet_from_edit = QtWidgets.QLineEdit(MainWindow)
        self.sheet_from_edit.setGeometry(QtCore.QRect(530, 630+self.boardMargin, 100, 30))
        self.sheet_from_edit.setObjectName("sheet_from_edit")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.sheet_from_edit.setFont(font)
        self.sheet_from_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 10px;")

        self.EighthTo_label = QtWidgets.QLabel(MainWindow)
        self.EighthTo_label.setGeometry(QtCore.QRect(470, 670+self.boardMargin, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.EighthTo_label.setStyleSheet("background-color: rgb(179, 124, 58); color:rgb(0, 0, 0);")
        self.EighthTo_label.setAlignment(QtCore.Qt.AlignRight)
        self.EighthTo_label.setFont(font)
        self.EighthTo_label.setText("To:")

        self.sheet_to_edit = QtWidgets.QLineEdit(MainWindow)
        self.sheet_to_edit.setGeometry(QtCore.QRect(530, 670+self.boardMargin, 100, 30))
        self.sheet_to_edit.setObjectName("sheet_to_edit")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(50)
        self.sheet_to_edit.setFont(font)
        self.sheet_to_edit.setStyleSheet("background-color: rgb(255, 255, 255); margin-left: 10px;")
        
    def writeNinethLine(self, MainWindow):
        self.sell_btn = gui.PicButton(QtGui.QPixmap('./images/sell_books_button.png'), MainWindow)
        self.sell_btn.setGeometry(QtCore.QRect(470, 730+self.boardMargin, 250, 50))
        self.sell_btn.clicked.connect(self.sell_book)
        
        self.sold_data_btn = gui.PicButton(QtGui.QPixmap('./images/sold_data_button.png'), MainWindow)
        self.sold_data_btn.setGeometry(QtCore.QRect(750, 730+self.boardMargin, 150, 50))
        self.sold_data_btn.clicked.connect(self.show_sold_data)

        self.product_list = QtWidgets.QTableView(MainWindow)
        self.product_list.setGeometry(QtCore.QRect(30, 110, 320, 600))
        self.product_list_Model = QtGui.QStandardItemModel()
        self.product_list_Model.setHorizontalHeaderLabels(['Product', 'Quantity', 'Price', 'Subtotal'])
        self.product_list.setModel(self.product_list_Model)
        self.product_list.setColumnWidth(0, 100)
        self.product_list.setColumnWidth(1, 70)
        self.product_list.setColumnWidth(2, 70)
        self.product_list.setColumnWidth(3, 100)
        self.product_list.setRowHeight(0, 150)
        self.product_list.setShowGrid(False)
        self.product_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.NinethTotal_label = QtWidgets.QLabel(MainWindow)
        self.NinethTotal_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(100)
        self.NinethTotal_label.setGeometry(QtCore.QRect(50, 710, 120, 100))
        self.NinethTotal_label.setFont(font)
        self.NinethTotal_label.setText("Total\nOrder:")
        
        self.NinethTotal_edit = QtWidgets.QLineEdit(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(100)
        self.NinethTotal_edit.setGeometry(QtCore.QRect(170, 730, 180, 60))
        self.NinethTotal_edit.setFont(font)
        self.NinethTotal_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NinethTotal_edit.setReadOnly(True)
        self.NinethTotal_edit.setText("€")
        
    def show_sold_data(self):
        if self.session_id==0:
            return
        Dialog = QtWidgets.QDialog()
        ui = soldDataDlg.Ui_Dialog()
        ui.session_name = self.session_combobox.currentText()
        ui.session_id = self.session_id
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        self.loadProductInfo()
        self.loadPrintInfo(self.session_id)
        
    def getPreprintedInfo(self):
        index = self.preprintedInfoList.currentIndex()
        idx = index.row()
        kind = self.preprintedInfoList.model().item(idx, 0).text()
        print_id = int(self.preprintedInfoList.model().item(idx, 1).text())
        perm_from = int(self.preprintedInfoList.model().item(idx, 2).text())
        perm_to = int(self.preprintedInfoList.model().item(idx, 3).text())
        if kind=='single':
            self.single_from_edit.setText(str(perm_from))
            self.single_to_edit.setText(str(perm_to))
            self.sheet_from_edit.setStyleSheet("background-color: white; margin-left: 10px;")
            self.sheet_to_edit.setStyleSheet("background-color: white; margin-left: 10px;")
        elif kind=='double':
            self.double_from_edit.setText(str(perm_from))
            self.double_to_edit.setText(str(perm_to))
            self.sheet_from_edit.setStyleSheet("background-color: white; margin-left: 10px;")
            self.sheet_to_edit.setStyleSheet("background-color: white; margin-left: 10px;")
        else:
            self.sheet_from_edit.setStyleSheet("background-color: yellow; margin-left: 10px;")
            self.sheet_to_edit.setStyleSheet("background-color: yellow; margin-left: 10px;")
    def sell_book(self):
        index = self.preprintedInfoList.currentIndex()
        idx = index.row()
        if idx==-1:
            pdfWriter.show_message('warning', 'Please select preprinted info to sell')
            return
        kind = self.preprintedInfoList.model().item(idx, 0).text()
        print_id = int(self.preprintedInfoList.model().item(idx, 1).text())
        perm_from = int(self.preprintedInfoList.model().item(idx, 2).text())
        perm_to = int(self.preprintedInfoList.model().item(idx, 3).text())
        single_book_price = self.secondline_layout_edit.text()
        double_book_price = self.thirdline_layout_edit.text()
        sheet_book_price = self.fourthline_layout_edit.text()
        customer_name = self.fifthline_layout_edit.text()
        sold_from = perm_from
        sold_to = perm_to
        if customer_name == "":
            ret = pdfWriter.show_message('warning', 'Do you really sell book without customer\'s name?', 'MB_YESNO')
            if ret == 0:
                return
        if kind=='single':
            if single_book_price=="":
                pdfWriter.show_message('warning', 'Please set the price of single book.')
                return
            if single_book_price.isnumeric()==False:
                pdfWriter.show_message('warning', 'Please set the price of single book to number.')
                return
            single_from = self.single_from_edit.text()
            single_to = self.single_to_edit.text()
            if single_from=="" or single_to=="":
                pdfWriter.show_message('warning', 'Please set the range of perm for single book.')
                return
            elif single_from.isnumeric()==False or single_to.isnumeric()==False:
                pdfWriter.show_message('warning', 'Please set the range of perm for single book to number.')
                return
            elif int(single_from) > int(single_to):
                pdfWriter.show_message('warning', 'The value \'From\' must be smaller than \'to\'')
                return
            if int(single_from) > perm_to or int(single_to) < perm_from:
                pdfWriter.show_message('warning', 'The perm range to sell is out of printed perm range.')
                return
            if self.checkSellInfo(print_id, single_from, single_to):
                self.addToDatabaseAndList(kind, int(single_from), int(single_to), print_id, float(single_book_price), customer_name)
        elif kind=='double':    
            if double_book_price=="":
                pdfWriter.show_message('warning', 'Please set the price of double book.')
                return
            if double_book_price.isnumeric()==False:
                pdfWriter.show_message('warning', 'Please set the price of double book to number.')
                return
            double_from = self.double_from_edit.text()
            double_to = self.double_to_edit.text()
            if double_from=="" or double_to=="":
                pdfWriter.show_message('warning', 'Please set the range of perm for double book.')
                return
            elif double_from.isnumeric()==False or double_to.isnumeric()==False:
                pdfWriter.show_message('warning', 'Please set the range of perm for double book to number.')
                return
            elif int(double_from) > int(double_to):
                pdfWriter.show_message('warning', 'The value \'From\' must be smaller than \'to\'')
                return
            if int(double_from) > perm_to or int(double_to) < perm_from:
                pdfWriter.show_message('warning', 'The perm range to sell is out of printed perm range.')
                return
            if self.checkSellInfo(print_id, double_from, double_to):
                self.addToDatabaseAndList(kind, int(double_from), int(double_to), print_id, float(double_book_price), customer_name)
        elif kind=='sheet':
            if sheet_book_price=="":
                pdfWriter.show_message('warning', 'Please set the price of sheet book.')
                return
            if sheet_book_price.isnumeric()==False:
                pdfWriter.show_message('warning', 'Please set the price of sheet book to number.')
                return
            sheet_from = self.sheet_from_edit.text()
            sheet_to = self.sheet_to_edit.text()
            if sheet_from=="" or sheet_to=="":
                pdfWriter.show_message('warning', 'Please set the range of perm for sheet book.')
                return
            elif sheet_from.isnumeric()==False or sheet_to.isnumeric()==False:
                pdfWriter.show_message('warning', 'Please set the range of perm for sheet book to number.')
                return
            elif int(sheet_from) > int(sheet_to):
                pdfWriter.show_message('warning', 'The value \'From\' must be smaller than \'to\'')
                return
            sold_from = int(sheet_from)
            sold_to = int(sheet_to)
            if not (sold_from >= perm_from and sold_from <= perm_to and sold_to >= perm_from and sold_to <= perm_to):
                pdfWriter.show_message('warning', 'The perm range to sell is out of printed perm range.')
                return
            if self.checkValidPermRange(int(sheet_from), int(sheet_to))==False:
                pdfWriter.show_message('warning', 'Please enter valid perm range.')
                return
            if self.checkSellInfo(print_id, sheet_from, sheet_to):
                self.addToDatabaseAndList(kind, int(sheet_from), int(sheet_to), print_id, float(sheet_book_price), customer_name)
        self.loadPrintInfo(self.session_id)
        session_name = self.session_combobox.currentText()
        filename = "books/{}-{}-({}-{}).pdf".format(session_name, kind, perm_from, perm_to)
        if os.path.isfile(filename):
            if customer_name!="":
                pdfWriter.makePdfUsingCustomerNameWithPdfrw(filename, self.session_id, kind, sold_from, sold_to, customer_name, perm_from, perm_to)
        else:
            pdfWriter.show_message('warning', 'pdf file to add customer name doesn\'t exist')

    def checkValidPermRange(self, perm_from, perm_to):
        nTableId = perm_from % 6
        if nTableId != 1:
            return False
        if perm_to%6 != 0:
            return False
        if perm_to <= perm_from:
            return False
        
    def checkSellInfo(self, print_id, perm_from, perm_to):
        query = "select *from sell_info where ((perm_from>='{}' and perm_from<='{}') or (perm_to>='{}' and perm_to<='{}') or (perm_from<='{}' and perm_to>='{}') or (perm_from<='{}' and perm_to>='{}')) and print_id='{}'".format(perm_from, perm_to, perm_from, perm_to, perm_from, perm_from, perm_to, perm_to, print_id)
        mydb = gui.mydb
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myres = mycursor.fetchall()
        if len(myres) > 0:
            pdfWriter.show_message('warning', 'You have set already sold perm range. [{}-{}] {}'.format(myres[0][4], myres[0][5], myres[0][8]))
            return False
        return True
        
    def addToDatabaseAndList(self, kind, perm_from, perm_to, print_id, price, customer):
        query = "update soldtickets_new set sold='1', price='{}', customer_name='{}' where session_id='{}' and print_id='{}' and panel_id>='{}' and panel_id<='{}'".format(price, customer, self.session_id, print_id, perm_from, perm_to)
        mydb = gui.mydb
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        product_str = kind + "[{}-{}]".format(perm_from, perm_to)
        quantity = perm_to-perm_from+1
        if kind=="double" or kind=="single":
            quantity = 1
        else:
            quantity = quantity/6
        quantity_str = str(quantity)
        price_str = "{:.2f}".format(price)
        subtotal_str = "{:.2f}".format(quantity*price)
        self.totalMoney = self.totalMoney + quantity*price
        self.product_list_Model.appendRow([QtGui.QStandardItem(product_str), QtGui.QStandardItem(quantity_str), QtGui.QStandardItem(price_str), QtGui.QStandardItem(subtotal_str)])
        self.product_list.model().layoutChanged.emit()
        totalMoney = "€ {}".format(self.totalMoney)
        today = datetime.date.today()
        today_str = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
        nKind = 0
        if kind=="double":
            nKind = 1
        elif kind=="sheet":
            nKind = 2
        query = "insert into sell_info (id, session_id, print_id, kind, perm_from, perm_to, price, quantity, customer_name, sold_date) values(NULL\
            , '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                self.session_id, print_id, nKind, perm_from, perm_to, price, quantity, customer, today_str)
        mycursor.execute(query)
        mydb.commit()
        self.NinethTotal_edit.setText(totalMoney)
        if kind=='single' or kind=='double':
            query = "update print_info set sold='1' where id='{}'".format(print_id)
            mycursor.execute(query)
            mydb.commit()
        else:
            query = "select count(*) from soldtickets_new where print_id='{}' and sold='1'".format(print_id)
            mycursor.execute(query)
            myres = mycursor.fetchone()
            sold_count = myres[0]
            query = "select perm_from, perm_to from print_info where id='{}' and print_kind='2'".format(print_id)
            mycursor.execute(query)
            myres = mycursor.fetchone()
            print_count = int(myres[1])-int(myres[0])+1
            if print_count==sold_count:
                query = "update print_info set sold='1' where id='{}'".format(print_id)
                mycursor.execute(query)
                mydb.commit()
        self.loadProductInfo()
            

    def loadProductInfo(self):
        # today = datetime.date.today()
        # today_str = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
        # query = "select *from sell_info where sold_date='{}'".format(today_str)
        if self.session_id==0:
            return
        self.product_list_Model.clear()
        self.product_list_Model.setHorizontalHeaderLabels(['Product', 'Quantity', 'Price', 'Subtotal'])
        self.product_list.setModel(self.product_list_Model)
        self.product_list.setColumnWidth(0, 100)
        self.product_list.setColumnWidth(1, 70)
        self.product_list.setColumnWidth(2, 70)
        self.product_list.setColumnWidth(3, 100)
        query = "select *from sell_info where session_id='{}'".format(self.session_id)
        mydb = gui.mydb
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myres = mycursor.fetchall()
        self.totalMoney = 0
        for res in myres:
            kind = 'single'
            if res[3]==1:
                kind = 'double'
            elif res[3]==2:
                kind = 'sheet'
            product_str = "{}[{}-{}]".format(kind, res[4], res[5])
            quantity = int(res[7])
            quantity_str = str(quantity)
            price_str = "{:.2f}".format(res[6])
            subtotal = quantity*float(res[6])
            subtotal_str = "{:.2f}".format(subtotal)
            self.totalMoney = self.totalMoney + subtotal
            self.product_list_Model.appendRow([QtGui.QStandardItem(product_str), QtGui.QStandardItem(quantity_str), QtGui.QStandardItem(price_str), QtGui.QStandardItem(subtotal_str)])
        self.product_list.model().layoutChanged.emit()
            
        totalMoney = "€ {}".format(self.totalMoney)
        self.NinethTotal_edit.setText(totalMoney)

            