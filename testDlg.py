# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-70, 240, 351, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.red = QtWidgets.QRadioButton(Dialog)
        self.red.setGeometry(QtCore.QRect(50, 20, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red.setFont(font)
        self.red.setObjectName("red")
        self.green = QtWidgets.QRadioButton(Dialog)
        self.green.setGeometry(QtCore.QRect(50, 60, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.green.setFont(font)
        self.green.setObjectName("green")
        self.blue = QtWidgets.QRadioButton(Dialog)
        self.blue.setGeometry(QtCore.QRect(50, 100, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.blue.setFont(font)
        self.blue.setObjectName("blue")
        self.cyan = QtWidgets.QRadioButton(Dialog)
        self.cyan.setGeometry(QtCore.QRect(50, 140, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cyan.setFont(font)
        self.cyan.setObjectName("cyan")
        self.pink = QtWidgets.QRadioButton(Dialog)
        self.pink.setGeometry(QtCore.QRect(50, 180, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pink.setFont(font)
        self.pink.setObjectName("pink")
        self.yellow = QtWidgets.QRadioButton(Dialog)
        self.yellow.setGeometry(QtCore.QRect(160, 20, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yellow.setFont(font)
        self.yellow.setObjectName("yellow")
        self.white = QtWidgets.QRadioButton(Dialog)
        self.white.setGeometry(QtCore.QRect(160, 60, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.white.setFont(font)
        self.white.setObjectName("white")
        self.purple = QtWidgets.QRadioButton(Dialog)
        self.purple.setGeometry(QtCore.QRect(160, 100, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.purple.setFont(font)
        self.purple.setObjectName("purple")
        self.red_9 = QtWidgets.QRadioButton(Dialog)
        self.red_9.setGeometry(QtCore.QRect(160, 140, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red_9.setFont(font)
        self.red_9.setObjectName("red_9")
        self.red_10 = QtWidgets.QRadioButton(Dialog)
        self.red_10.setGeometry(QtCore.QRect(160, 180, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red_10.setFont(font)
        self.red_10.setObjectName("red_10")
        self.red_11 = QtWidgets.QRadioButton(Dialog)
        self.red_11.setGeometry(QtCore.QRect(270, 20, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red_11.setFont(font)
        self.red_11.setObjectName("red_11")
        self.red_12 = QtWidgets.QRadioButton(Dialog)
        self.red_12.setGeometry(QtCore.QRect(270, 60, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red_12.setFont(font)
        self.red_12.setObjectName("red_12")
        self.red_13 = QtWidgets.QRadioButton(Dialog)
        self.red_13.setGeometry(QtCore.QRect(270, 100, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red_13.setFont(font)
        self.red_13.setObjectName("red_13")
        self.red_14 = QtWidgets.QRadioButton(Dialog)
        self.red_14.setGeometry(QtCore.QRect(270, 140, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red_14.setFont(font)
        self.red_14.setObjectName("red_14")
        self.red_15 = QtWidgets.QRadioButton(Dialog)
        self.red_15.setGeometry(QtCore.QRect(270, 180, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.red_15.setFont(font)
        self.red_15.setObjectName("red_15")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.red.setText(_translate("Dialog", "Red"))
        self.green.setText(_translate("Dialog", "Green"))
        self.blue.setText(_translate("Dialog", "Blue"))
        self.cyan.setText(_translate("Dialog", "Cyan"))
        self.pink.setText(_translate("Dialog", "Pink"))
        self.yellow.setText(_translate("Dialog", "Yellow"))
        self.white.setText(_translate("Dialog", "White"))
        self.purple.setText(_translate("Dialog", "Purple"))
        self.red_9.setText(_translate("Dialog", "Red"))
        self.red_10.setText(_translate("Dialog", "Red"))
        self.red_11.setText(_translate("Dialog", "Red"))
        self.red_12.setText(_translate("Dialog", "Red"))
        self.red_13.setText(_translate("Dialog", "Red"))
        self.red_14.setText(_translate("Dialog", "Red"))
        self.red_15.setText(_translate("Dialog", "Red"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
