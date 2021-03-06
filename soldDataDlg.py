# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soldDataDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pdfWriter
import gui

class Ui_Dialog(object):
    session_name = ""
    session_id = 0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(695, 594)
        Dialog.setStyleSheet("QDialog{background-color: orange;}")
        self.sessionName = QtWidgets.QLabel(Dialog)
        self.sessionName.setGeometry(QtCore.QRect(400, 10, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sessionName.setFont(font)
        self.sessionName.setObjectName("label")
        
        self.soldInfoList = QtWidgets.QTableView(Dialog)
        self.soldInfoList.setGeometry(QtCore.QRect(40, 50, 611, 471))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.soldInfoList.setFont(font)
        self.soldInfoList.setObjectName("tableView")
        self.soldDataModel = QtGui.QStandardItemModel()
        self.soldDataModel.setHorizontalHeaderLabels(['kind', 'print id', 'from', 'to', 'price', 'quantity', 'customer', 'sold_date'])
        self.soldInfoList.setModel(self.soldDataModel)
        self.soldInfoList.setColumnWidth(0, 80)
        self.soldInfoList.setColumnWidth(1, 80)
        self.soldInfoList.setColumnWidth(2, 100)
        self.soldInfoList.setColumnWidth(3, 100)
        self.soldInfoList.setColumnWidth(4, 80)
        self.soldInfoList.setColumnWidth(5, 80)
        self.soldInfoList.setColumnWidth(6, 150)
        self.soldInfoList.setColumnWidth(7, 150)
        self.soldInfoList.setShowGrid(False)
        self.soldInfoList.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(400, 540, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.reject)
        
        self.cancelSoldButton = QtWidgets.QPushButton(Dialog)
        self.cancelSoldButton.setGeometry(QtCore.QRect(170, 540, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancelSoldButton.setFont(font)
        self.cancelSoldButton.setObjectName("cancelSoldButton")
        self.cancelSoldButton.clicked.connect(self.cancelSoldClick)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.loadSoldInfo()

    def cancelSoldClick(self):
        index = self.soldInfoList.currentIndex()
        idx = index.row()
        if idx==-1:
            pdfWriter.show_message('warning', 'Please select sold info to cancel')
            return
        print_id = int(self.soldInfoList.model().item(idx, 1).text())
        perm_from = int(self.soldInfoList.model().item(idx, 2).text())
        perm_to = int(self.soldInfoList.model().item(idx, 3).text())
        customer = self.soldInfoList.model().item(idx, 6).text()
        ret = pdfWriter.show_message('Confirm', 'Do you really want to cancel sold data for print_id = {} ?\r\ncustomer:"{}", perm_from:"{}", perm_to:"{}"'
                                     .format(str(print_id), customer, perm_from, perm_to), 'MB_YESNO')
        if ret==0:
            return
        query = "delete from sell_info where print_id='{}' and perm_from='{}' and perm_to='{}' and customer_name='{}'".format(print_id, perm_from, perm_to, customer)
        mycursor = gui.mydb.cursor()
        mycursor.execute(query)
        query = "update print_info set sold='0' where id='{}'".format(print_id)
        mycursor.execute(query)
        query = "update soldtickets_new set sold='0' where print_id='{}' and panel_id>='{}' and panel_id<='{}'".format(print_id, perm_from, perm_to)
        mycursor.execute(query)
        gui.mydb.commit()
        self.loadSoldInfo()
        pdfWriter.show_message('', 'Successfully cancelled.')

    def loadSoldInfo(self):
        self.soldDataModel.clear()
        # self.soldDataModel.setHorizontalHeaderLabels(['kind', 'print id', 'from', 'to'])
        query = "select * from sell_info where session_id='{}' order by id".format(self.session_id)
        mydb = gui.mydb
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myres = mycursor.fetchall()
        for res in myres:
            if res[3]==0:
                kind = "single"
            elif res[3]==1:
                kind = "double"
            else:
                kind = "sheet"
            print_id = str(res[2])
            print_from = str(res[4])
            print_to = str(res[5])
            quantity = str(res[7])
            price = str(res[6])
            customer = str(res[8])
            sold_date = str(res[9])
            self.soldDataModel.appendRow([QtGui.QStandardItem(kind), QtGui.QStandardItem(print_id), QtGui.QStandardItem(print_from), QtGui.QStandardItem(print_to)
                                          , QtGui.QStandardItem(price), QtGui.QStandardItem(quantity), QtGui.QStandardItem(customer), QtGui.QStandardItem(sold_date)])
        self.soldInfoList.model().layoutChanged.emit()
        self.soldDataModel.setHorizontalHeaderLabels(['kind', 'print id', 'from', 'to', 'price', 'quantity', 'customer', 'sold_date'])
        self.soldInfoList.setModel(self.soldDataModel)
        self.soldInfoList.setColumnWidth(0, 80)
        self.soldInfoList.setColumnWidth(1, 80)
        self.soldInfoList.setColumnWidth(2, 100)
        self.soldInfoList.setColumnWidth(3, 100)
        self.soldInfoList.setColumnWidth(4, 80)
        self.soldInfoList.setColumnWidth(5, 80)
        self.soldInfoList.setColumnWidth(6, 150)
        self.soldInfoList.setColumnWidth(7, 150)
        self.soldInfoList.setShowGrid(False)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sold Data"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.cancelSoldButton.setText(_translate("Dialog", "Cancel Sold"))
        self.label.setText(_translate("Dialog", "Sold Data for session"))
        self.sessionName.setText(_translate("Dialog", self.session_name))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
