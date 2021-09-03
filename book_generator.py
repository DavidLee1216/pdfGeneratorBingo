from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import images
import datetime
import colorDlg
import pdfWriter
import gui

class BookGenerator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(BookGenerator, self).__init__(parent=parent)
        self.book_kind = 0
        self.setupUi()
        
    def setupUi(self):
        self.setStyleSheet("background-color: #0067b1;")
        self.setWindowTitle("Bingo Ticket Generator")
        self.writeFirstLine(self)
        self.writeSecondLine(self)
        self.writeThirdLine(self)
        self.writeFourthLine(self)
        self.writeFifthLine(self)
        self.writeSixthLine(self)
        # self.writeSeventhLine(self)
        # self.writeEighthLine(self)
        self.drawButtons()
        self.setDefaultColors()
        
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


    def drawButtons(self):
        self.print_btn = gui.PicButton(QtGui.QPixmap('./images/print_button.png'), self)
        self.print_btn.move(650, 750)
        self.print_btn.resize(200,40)
        self.print_btn.clicked.connect(self.print)

    def writeFirstLine(self, MainWindow):
        self.title_label = QtWidgets.QLabel(MainWindow)
        self.title_label.setGeometry(QtCore.QRect(80, 30, 600, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(100)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(255, 196, 37);border: none;")
        self.title_label.setText("Bingo Book Generator")
        
        self.session_label = QtWidgets.QLabel(MainWindow)
        self.session_label.setGeometry(QtCore.QRect(80, 80, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.session_label.setFont(font)
        self.session_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.session_label.setText("Select Session to Print Books for:")
                        
        self.session_combobox = QtWidgets.QComboBox(MainWindow)
        self.session_combobox.setGeometry(QtCore.QRect(540, 80, 150, 30))
        self.session_combobox.setObjectName("session_combobox")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.session_combobox.setFont(font)
        self.session_combobox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.loadSessions()
        self.session_combobox.currentIndexChanged.connect(self.session_combobox_changed)
        
        self.panel_per_page_label = QtWidgets.QLabel(MainWindow)
        self.panel_per_page_label.setGeometry(QtCore.QRect(80, 120, 480, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.panel_per_page_label.setFont(font)
        self.panel_per_page_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.panel_per_page_label.setText("Please enter how many bingo pages per book")
        self.small_panel_per_page_label = QtWidgets.QLabel(MainWindow)
        self.small_panel_per_page_label.setGeometry(QtCore.QRect(560, 127, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.small_panel_per_page_label.setFont(font)
        self.small_panel_per_page_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.small_panel_per_page_label.setText("(6 panels per page)")
        self.colon_panel_per_page_label = QtWidgets.QLabel(MainWindow)
        self.colon_panel_per_page_label.setGeometry(QtCore.QRect(660, 120, 10, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.colon_panel_per_page_label.setFont(font)
        self.colon_panel_per_page_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.colon_panel_per_page_label.setText(":")

        self.panelPerPageEdit = QtWidgets.QLineEdit(MainWindow)
        self.panelPerPageEdit.setGeometry(QtCore.QRect(680, 120, 150, 30))
        self.panelPerPageEdit.setObjectName("panelPerPageEdit")
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.panelPerPageEdit.setFont(font)
        self.panelPerPageEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
    
    def session_combobox_changed(self, i):
        if len(self.session_ids) > 0 and i >= 0:
            self.session_id = self.session_ids[i]
        
    def writeSecondLine(self, MainWindow):
        self.panel_per_page_label2 = QtWidgets.QLabel(MainWindow)
        self.panel_per_page_label2.setGeometry(QtCore.QRect(80, 160, 600, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.panel_per_page_label2.setFont(font)
        self.panel_per_page_label2.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.panel_per_page_label2.setText("Please enter how many single bingo books to be printed:")

        self.booksCountEdit = QtWidgets.QLineEdit(MainWindow)
        self.booksCountEdit.setGeometry(QtCore.QRect(680, 160, 150, 30))
        self.booksCountEdit.setObjectName("panelPerPageEdit")
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.booksCountEdit.setFont(font)
        self.booksCountEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.single_book_radio = QtWidgets.QRadioButton(MainWindow)
        self.single_book_radio.setChecked(True)
        self.single_book_radio.setGeometry(QtCore.QRect(840, 160, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_book_radio.clicked.connect(self.single_book_radio_clicked)

        self.panel_per_page_label3 = QtWidgets.QLabel(MainWindow)
        self.panel_per_page_label3.setGeometry(QtCore.QRect(80, 200, 600, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.panel_per_page_label3.setFont(font)
        self.panel_per_page_label3.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.panel_per_page_label3.setText("Please enter how many double bingo books to be printed:")

        self.booksDoubleCountEdit = QtWidgets.QLineEdit(MainWindow)
        self.booksDoubleCountEdit.setGeometry(QtCore.QRect(680, 200, 150, 30))
        self.booksDoubleCountEdit.setObjectName("panelPerPageEdit")
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.booksDoubleCountEdit.setFont(font)
        self.booksDoubleCountEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.double_book_radio = QtWidgets.QRadioButton(MainWindow)
        self.double_book_radio.setGeometry(QtCore.QRect(840, 200, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.double_book_radio.clicked.connect(self.double_book_radio_clicked)

        self.panel_per_page_label4 = QtWidgets.QLabel(MainWindow)
        self.panel_per_page_label4.setGeometry(QtCore.QRect(80, 240, 600, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.panel_per_page_label4.setFont(font)
        self.panel_per_page_label4.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.panel_per_page_label4.setText("Please enter how many single page(sheets) to be printed:")

        self.sheetsCountEdit = QtWidgets.QLineEdit(MainWindow)
        self.sheetsCountEdit.setGeometry(QtCore.QRect(680, 240, 150, 30))
        self.sheetsCountEdit.setObjectName("panelPerPageEdit")
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.sheetsCountEdit.setFont(font)
        self.sheetsCountEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.sheet_book_radio = QtWidgets.QRadioButton(MainWindow)
        self.sheet_book_radio.setGeometry(QtCore.QRect(840, 240, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sheet_book_radio.clicked.connect(self.sheet_book_radio_clicked)

        self.singlePageGameLabel = QtWidgets.QLabel(MainWindow)
        self.singlePageGameLabel.setGeometry(QtCore.QRect(80, 280, 380, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.singlePageGameLabel.setFont(font)
        self.singlePageGameLabel.setStyleSheet("color: rgb(0, 0, 0); border: none;")
        self.singlePageGameLabel.setText("Single Page (Sheet) Game Colour:")
        
        self.single_sheet_game_color = QtWidgets.QLabel(MainWindow)
        self.single_sheet_game_color.setGeometry(QtCore.QRect(470, 287, 80, 20))
        self.single_sheet_game_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        button_icon = QtGui.QIcon("./images/button.png")
        self.single_sheet_game_color_btn = QtWidgets.QPushButton(MainWindow)
        self.single_sheet_game_color_btn.setGeometry(QtCore.QRect(560, 282, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.single_sheet_game_color_btn.setFont(font)
        self.single_sheet_game_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.single_sheet_game_color_btn.setIcon(button_icon)
        self.single_sheet_game_color_btn.setIconSize(QtCore.QSize(self.single_sheet_game_color_btn.width(), self.single_sheet_game_color_btn.height()))
        self.single_sheet_game_color_btn.clicked.connect(self.browseSingleSheetColor)
        
        self.single_sheet_a4_label = QtWidgets.QLabel(MainWindow)
        self.single_sheet_a4_label.setGeometry(QtCore.QRect(690, 280, 250, 30))
        self.single_sheet_a4_label.setFont(font)
        self.single_sheet_a4_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.single_sheet_a4_label.setText("NB will print 3 per A4 page")
        
    def single_book_radio_clicked(self):
        self.book_kind = 0

    def double_book_radio_clicked(self):
        self.book_kind = 1

    def sheet_book_radio_clicked(self):
        self.book_kind = 2

    def writeThirdLine(self, MainWindow):
        v_extra_height = 120
        self.panel_per_page_label5 = QtWidgets.QLabel(MainWindow)
        self.panel_per_page_label5.setGeometry(QtCore.QRect(80, 200+v_extra_height, 560, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.panel_per_page_label5.setFont(font)
        self.panel_per_page_label5.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.panel_per_page_label5.setText("Please enter the perm range for the books(If known):")

        self.perm_from_label = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.perm_from_label.setGeometry(QtCore.QRect(350, 245+v_extra_height, 100, 30))
        self.perm_from_label.setFont(font)
        self.perm_from_label.setText("From:")
        self.perm_to_label = QtWidgets.QLabel(MainWindow)
        self.perm_to_label.setGeometry(QtCore.QRect(630, 245+v_extra_height, 100, 30))
        self.perm_to_label.setFont(font)
        self.perm_to_label.setText("To:")

        self.permFromEdit = QtWidgets.QLineEdit(MainWindow)
        self.permFromEdit.setGeometry(QtCore.QRect(420, 245+v_extra_height, 150, 30))
        self.permFromEdit.setObjectName("permFromEdit")
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.permFromEdit.setFont(font)
        self.permFromEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.permFromEdit.textEdited.connect(self.changePermFrom)
        self.permToEdit = QtWidgets.QLineEdit(MainWindow)
        self.permToEdit.setGeometry(QtCore.QRect(680, 245+v_extra_height, 150, 30))
        self.permToEdit.setObjectName("permToEdit")
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.permToEdit.setFont(font)
        self.permToEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

    def writeFourthLine(self, MainWindow):
        v_extra_height = 120
        self.page_title_label1 = QtWidgets.QLabel(MainWindow)
        self.page_title_label1.setGeometry(QtCore.QRect(80, 275+v_extra_height, 280, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.page_title_label1.setFont(font)
        self.page_title_label1.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.page_title_label1.setText("Please enter the page title")
        self.page_title_label2 = QtWidgets.QLabel(MainWindow)
        self.page_title_label2.setGeometry(QtCore.QRect(80, 305+v_extra_height, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.page_title_label2.setFont(font)
        self.page_title_label2.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.page_title_label2.setText("(25 Characters Max):")

        self.pageTitleEdit = QtWidgets.QLineEdit(MainWindow)
        self.pageTitleEdit.setGeometry(QtCore.QRect(380, 295+v_extra_height, 450, 30))
        self.pageTitleEdit.setObjectName("pageTitleEdit")
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.pageTitleEdit.setFont(font)
        self.pageTitleEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

    def writeFifthLine(self, MainWindow):
        v_extra_height = 120
        self.choose_logo_label = QtWidgets.QLabel(MainWindow)
        self.choose_logo_label.setGeometry(QtCore.QRect(80, 350+v_extra_height, 430, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.choose_logo_label.setFont(font)
        self.choose_logo_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.choose_logo_label.setText("Choose a logo or image for top of page:")

        self.logo_browse_btn = QtWidgets.QPushButton(MainWindow)
        self.logo_browse_btn.setGeometry(QtCore.QRect(520, 345+v_extra_height, 120, 30))
        self.logo_browse_btn.setFont(font)
        self.logo_browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#        self.logo_browse_btn.setStyleSheet("background-color: #0067b1;")
#        pixmap = QtGui.QPixmap("./images/button.png")
#        self.logo_browse_btn.setPixmap(pixmap)
        button_icon = QtGui.QIcon("./images/button.png")
        self.logo_browse_btn.setIcon(button_icon)
        self.logo_browse_btn.setIconSize(QtCore.QSize(self.logo_browse_btn.width(), self.logo_browse_btn.height()))
        self.logo_browse_btn.clicked.connect(self.browseLogoImage)

        self.chooseLogoEdit = QtWidgets.QLineEdit(MainWindow)
        self.chooseLogoEdit.setGeometry(QtCore.QRect(650, 345+v_extra_height, 180, 30))
        self.chooseLogoEdit.setObjectName("chooseLogoEdit")
        self.chooseLogoEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

    def writeSixthLine(self, MainWindow):
        v_interval = 40
        v_extra_height = 120
        self.game1_color_label = QtWidgets.QLabel(MainWindow)
        self.game1_color_label.setGeometry(QtCore.QRect(80, 395+v_extra_height, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        self.game1_color_label.setFont(font)
        self.game1_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game1_color_label.setText("Game 1 Colour:")
        self.game1_color = QtWidgets.QLabel(MainWindow)
        self.game1_color.setGeometry(QtCore.QRect(220, 402+v_extra_height, 80, 20))
        self.game1_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        button_icon = QtGui.QIcon("./images/button.png")

        self.game1_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game1_color_btn.setGeometry(QtCore.QRect(310, 397+v_extra_height, 120, 30))
        self.game1_color_btn.setFont(font)
        self.game1_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game1_color_btn.setIcon(button_icon)
        self.game1_color_btn.setIconSize(QtCore.QSize(self.game1_color_btn.width(), self.game1_color_btn.height()))
        self.game1_color_btn.clicked.connect(self.browseColor1)

        self.game2_color_label = QtWidgets.QLabel(MainWindow)
        self.game2_color_label.setGeometry(QtCore.QRect(460, 395+v_extra_height, 160, 30))
        self.game2_color_label.setFont(font)
        self.game2_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game2_color_label.setText("Game 2 Colour:")
        self.game2_color = QtWidgets.QLabel(MainWindow)
        self.game2_color.setGeometry(QtCore.QRect(620, 402+v_extra_height, 80, 20))
        self.game2_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game2_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game2_color_btn.setGeometry(QtCore.QRect(710, 397+v_extra_height, 120, 30))
        self.game2_color_btn.setFont(font)
        self.game2_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game2_color_btn.setIcon(button_icon)
        self.game2_color_btn.setIconSize(QtCore.QSize(self.game1_color_btn.width(), self.game1_color_btn.height()))
        self.game2_color_btn.clicked.connect(self.browseColor2)

        self.game3_color_label = QtWidgets.QLabel(MainWindow)
        self.game3_color_label.setGeometry(QtCore.QRect(80, 395+v_interval+v_extra_height, 160, 30))
        self.game3_color_label.setFont(font)
        self.game3_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game3_color_label.setText("Game 3 Colour:")
        self.game3_color = QtWidgets.QLabel(MainWindow)
        self.game3_color.setGeometry(QtCore.QRect(220, 402+v_interval+v_extra_height, 80, 20))
        self.game3_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game3_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game3_color_btn.setGeometry(QtCore.QRect(310, 397+v_interval+v_extra_height, 120, 30))
        self.game3_color_btn.setFont(font)
        self.game3_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game3_color_btn.setIcon(button_icon)
        self.game3_color_btn.setIconSize(QtCore.QSize(self.game3_color_btn.width(), self.game3_color_btn.height()))
        self.game3_color_btn.clicked.connect(self.browseColor3)

        self.game4_color_label = QtWidgets.QLabel(MainWindow)
        self.game4_color_label.setGeometry(QtCore.QRect(460, 395+v_interval+v_extra_height, 160, 30))
        self.game4_color_label.setFont(font)
        self.game4_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game4_color_label.setText("Game 4 Colour:")
        self.game4_color = QtWidgets.QLabel(MainWindow)
        self.game4_color.setGeometry(QtCore.QRect(620, 402+v_interval+v_extra_height, 80, 20))
        self.game4_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game4_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game4_color_btn.setGeometry(QtCore.QRect(710, 397+v_interval+v_extra_height, 120, 30))
        self.game4_color_btn.setFont(font)
        self.game4_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game4_color_btn.setIcon(button_icon)
        self.game4_color_btn.setIconSize(QtCore.QSize(self.game4_color_btn.width(), self.game4_color_btn.height()))
        self.game4_color_btn.clicked.connect(self.browseColor4)

        self.game5_color_label = QtWidgets.QLabel(MainWindow)
        self.game5_color_label.setGeometry(QtCore.QRect(80, 395+v_interval*2+v_extra_height, 160, 30))
        self.game5_color_label.setFont(font)
        self.game5_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game5_color_label.setText("Game 5 Colour:")
        self.game5_color = QtWidgets.QLabel(MainWindow)
        self.game5_color.setGeometry(QtCore.QRect(220, 402+v_interval*2+v_extra_height, 80, 20))
        self.game5_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game5_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game5_color_btn.setGeometry(QtCore.QRect(310, 397+v_interval*2+v_extra_height, 120, 30))
        self.game5_color_btn.setFont(font)
        self.game5_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game5_color_btn.setIcon(button_icon)
        self.game5_color_btn.setIconSize(QtCore.QSize(self.game5_color_btn.width(), self.game5_color_btn.height()))
        self.game5_color_btn.clicked.connect(self.browseColor5)

        self.game6_color_label = QtWidgets.QLabel(MainWindow)
        self.game6_color_label.setGeometry(QtCore.QRect(460, 395+v_interval*2+v_extra_height, 160, 30))
        self.game6_color_label.setFont(font)
        self.game6_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game6_color_label.setText("Game 6 Colour:")
        self.game6_color = QtWidgets.QLabel(MainWindow)
        self.game6_color.setGeometry(QtCore.QRect(620, 402+v_interval*2+v_extra_height, 80, 20))
        self.game6_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game6_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game6_color_btn.setGeometry(QtCore.QRect(710, 397+v_interval*2+v_extra_height, 120, 30))
        self.game6_color_btn.setFont(font)
        self.game6_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game6_color_btn.setIcon(button_icon)
        self.game6_color_btn.setIconSize(QtCore.QSize(self.game6_color_btn.width(), self.game6_color_btn.height()))
        self.game6_color_btn.clicked.connect(self.browseColor6)

        self.game7_color_label = QtWidgets.QLabel(MainWindow)
        self.game7_color_label.setGeometry(QtCore.QRect(80, 395+v_interval*3+v_extra_height, 160, 30))
        self.game7_color_label.setFont(font)
        self.game7_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game7_color_label.setText("Game 7 Colour:")
        self.game7_color = QtWidgets.QLabel(MainWindow)
        self.game7_color.setGeometry(QtCore.QRect(220, 402+v_interval*3+v_extra_height, 80, 20))
        self.game7_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game7_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game7_color_btn.setGeometry(QtCore.QRect(310, 397+v_interval*3+v_extra_height, 120, 30))
        self.game7_color_btn.setFont(font)
        self.game7_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game7_color_btn.setIcon(button_icon)
        self.game7_color_btn.setIconSize(QtCore.QSize(self.game7_color_btn.width(), self.game7_color_btn.height()))
        self.game7_color_btn.clicked.connect(self.browseColor7)

        self.game8_color_label = QtWidgets.QLabel(MainWindow)
        self.game8_color_label.setGeometry(QtCore.QRect(460, 395+v_interval*3+v_extra_height, 160, 30))
        self.game8_color_label.setFont(font)
        self.game8_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game8_color_label.setText("Game 8 Colour:")
        self.game8_color = QtWidgets.QLabel(MainWindow)
        self.game8_color.setGeometry(QtCore.QRect(620, 402+v_interval*3+v_extra_height, 80, 20))
        self.game8_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game8_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game8_color_btn.setGeometry(QtCore.QRect(710, 397+v_interval*3+v_extra_height, 120, 30))
        self.game8_color_btn.setFont(font)
        self.game8_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game8_color_btn.setIcon(button_icon)
        self.game8_color_btn.setIconSize(QtCore.QSize(self.game8_color_btn.width(), self.game8_color_btn.height()))
        self.game8_color_btn.clicked.connect(self.browseColor8)

        self.game9_color_label = QtWidgets.QLabel(MainWindow)
        self.game9_color_label.setGeometry(QtCore.QRect(80, 395+v_interval*4+v_extra_height, 160, 30))
        self.game9_color_label.setFont(font)
        self.game9_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game9_color_label.setText("Game 9 Colour:")
        self.game9_color = QtWidgets.QLabel(MainWindow)
        self.game9_color.setGeometry(QtCore.QRect(220, 402+v_interval*4+v_extra_height, 80, 20))
        self.game9_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game9_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game9_color_btn.setGeometry(QtCore.QRect(310, 397+v_interval*4+v_extra_height, 120, 30))
        self.game9_color_btn.setFont(font)
        self.game9_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game9_color_btn.setIcon(button_icon)
        self.game9_color_btn.setIconSize(QtCore.QSize(self.game9_color_btn.width(), self.game9_color_btn.height()))
        self.game9_color_btn.clicked.connect(self.browseColor9)

        self.game10_color_label = QtWidgets.QLabel(MainWindow)
        self.game10_color_label.setGeometry(QtCore.QRect(460, 395+v_interval*4+v_extra_height, 160, 30))
        self.game10_color_label.setFont(font)
        self.game10_color_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.game10_color_label.setText("Game 10 Colour:")
        self.game10_color = QtWidgets.QLabel(MainWindow)
        self.game10_color.setGeometry(QtCore.QRect(620, 402+v_interval*4+v_extra_height, 80, 20))
        self.game10_color.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.game10_color_btn = QtWidgets.QPushButton(MainWindow)
        self.game10_color_btn.setGeometry(QtCore.QRect(710, 397+v_interval*4+v_extra_height, 120, 30))
        self.game10_color_btn.setFont(font)
        self.game10_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game10_color_btn.setIcon(button_icon)
        self.game10_color_btn.setIconSize(QtCore.QSize(self.game10_color_btn.width(), self.game10_color_btn.height()))
        self.game10_color_btn.clicked.connect(self.browseColor10)

        self.color1 = None
        self.color2 = None
        self.color3 = None
        self.color4 = None
        self.color5 = None
        self.color6 = None
        self.color7 = None
        self.color8 = None
        self.color9 = None
        self.color10 = None

    def writeSeventhLine(self, MainWindow):
        v_interval = 40
        v_extra_height = 120
        self.time_string_label = QtWidgets.QLabel(MainWindow)
        self.time_string_label.setGeometry(QtCore.QRect(80, 397+v_interval*4+60+v_extra_height, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.time_string_label.setFont(font)
        self.time_string_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.time_string_label.setText("Choose game playing period:")

        self.time_from = QtWidgets.QDateTimeEdit(MainWindow)
        self.time_from.setGeometry(QtCore.QRect(400, 397+v_interval*4+60+v_extra_height, 150, 30))
        self.time_from.setStyleSheet("background-color: rgb(255, 255, 255);")
        curr_date = datetime.date.today()
        self.time_from.setDate(curr_date)

        self.time_tire_label = QtWidgets.QLabel(MainWindow)
        self.time_tire_label.setGeometry(QtCore.QRect(560, 397+v_interval*4+60+v_extra_height, 15, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.time_tire_label.setFont(font)
        self.time_tire_label.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.time_tire_label.setText("-")


        self.time_to = QtWidgets.QDateTimeEdit(MainWindow)
        self.time_to.setGeometry(QtCore.QRect(580, 397+v_interval*4+60+v_extra_height, 150, 30))
        self.time_to.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_to.setDate(curr_date)

    def writeEighthLine(self, MainWindow):
        v_interval = 40
        self.note_label1 = QtWidgets.QLabel(MainWindow)
        self.note_label1.setGeometry(QtCore.QRect(150, 397+v_interval*4+60+60, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.note_label1.setFont(font)
        self.note_label1.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.note_label1.setText("Bingo Books are produced")
        
        self.note_label2 = QtWidgets.QLabel(MainWindow)
        self.note_label2.setGeometry(QtCore.QRect(180, 397+v_interval*4+60+60+40, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(50)
        self.note_label2.setFont(font)
        self.note_label2.setStyleSheet("color: rgb(0, 0, 0);border: none;")
        self.note_label2.setText("with 3 pages per sheet")
        
        self.printDouble = False
        self.double_checkbox = QtWidgets.QCheckBox("double", MainWindow)
        self.double_checkbox.setGeometry(QtCore.QRect(520, 397+v_interval*4+60+60, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(False)
        self.double_checkbox.setFont(font)
        self.double_checkbox.stateChanged.connect(self.setDoubleCheckBox)

    def setDoubleCheckBox(self, state):
        if state==QtCore.Qt.Checked:
            self.printDouble = True
        else:
            self.printDouble = False
            
    def changePermFrom(self):
        perm_range_from = self.permFromEdit.text()
        if perm_range_from.isnumeric()==False:
            self.show_message("Warning", "Please type right number format.")
            return
        table_id = int(perm_range_from)%6
        if table_id==1:
            return
        if table_id==0:
            perm_from = int(perm_range_from)+1
        else:
            perm_from = int(perm_range_from)-table_id+1
        self.permFromEdit.setText("{:d}".format(perm_from))


    def browseLogoImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Choose File", "","image Files (*.jpg *.png *.bmp)", options=options)
        self.chooseLogoEdit.setText(fileName)

    def setDefaultColors(self):
        self.single_sheet_game_color.setStyleSheet("background-color: gold;")
        self.single_sheet_color = "gold"
        self.game1_color.setStyleSheet("background-color: gold;")
        self.color1 = "gold"
        self.game2_color.setStyleSheet("background-color: purple;")
        self.color2 = "purple"
        self.game3_color.setStyleSheet("background-color: yellow;")
        self.color3 = "yellow"
        self.game4_color.setStyleSheet("background-color: pink;")
        self.color4 = "pink"
        self.game5_color.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.color5 = "green"
        self.game6_color.setStyleSheet("background-color: orange;")
        self.color6 = "orange"
        self.game7_color.setStyleSheet("background-color: blue;")
        self.color7 = "blue"
        self.game8_color.setStyleSheet("background-color: red;")
        self.color8 = "red"
        self.game9_color.setStyleSheet("background-color: grey;")
        self.color9 = "grey"
        self.game10_color.setStyleSheet("background-color: brown;")
        self.color10 = "brown"
        
    def browseSingleSheetColor(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        if ret==1:
            self.single_sheet_game_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.single_sheet_color = ui.color_name
        

    def browseColor1(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color1 = None
        if ret==1:
            self.game1_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color1 = ui.color_name


    def browseColor2(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color2 = None
        if ret==1:
            self.game2_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color2 = ui.color_name

    def browseColor3(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color3 = None
        if ret==1:
            self.game3_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color3 = ui.color_name

    def browseColor4(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color4 = None
        if ret==1:
            self.game4_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color4 = ui.color_name

    def browseColor5(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color5 = None
        if ret==1:
            self.game5_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color5 = ui.color_name

    def browseColor6(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color6 = None
        if ret==1:
            self.game6_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color6 = ui.color_name

    def browseColor7(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color7 = None
        if ret==1:
            self.game7_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color7 = ui.color_name

    def browseColor8(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color8 = None
        if ret==1:
            self.game8_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color8 = ui.color_name

    def browseColor9(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color9 = None
        if ret==1:
            self.game9_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color9 = ui.color_name

    def browseColor10(self):
        Dialog = QtWidgets.QDialog()
        ui = colorDlg.Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec_()
        # self.color10 = None
        if ret==1:
            self.game10_color.setStyleSheet("background-color:" + ui.curr_color + ";")
            self.color10 = ui.color_name

    def print(self):
        bingo_pages_per_book = self.panelPerPageEdit.text()
        bingo_books_to_print = self.booksCountEdit.text()
        bingo_double_books_to_print = self.booksDoubleCountEdit.text()
        bingo_single_sheets_to_print = self.sheetsCountEdit.text()
        perm_range_from = self.permFromEdit.text()
        perm_range_to = self.permToEdit.text()
        colors = []
        colors.append(self.color1)
        colors.append(self.color2)
        colors.append(self.color3)
        colors.append(self.color4)
        colors.append(self.color5)
        colors.append(self.color6)
        colors.append(self.color7)
        colors.append(self.color8)
        colors.append(self.color9)
        colors.append(self.color10)
        if bingo_pages_per_book!="" and bingo_pages_per_book.isnumeric()==False:
            self.show_message("Warning", "Please type right number format.")
            return
        elif bingo_pages_per_book=="":
            self.show_message("Warning", "Please enter pages per book.")
            return
        if bingo_books_to_print!="" and bingo_books_to_print.isnumeric()==False:
            self.show_message("Warning", "Please type right number format.")
            return
        if self.book_kind==0 and bingo_books_to_print=="":
            self.show_message("Warning", "Please enter single bingo books to be printed")
            return
        if bingo_double_books_to_print != "" and bingo_double_books_to_print.isnumeric()==False:
            self.show_message("Warning", "Please type right number format.")
            return
        if self.book_kind==1 and bingo_double_books_to_print=="":
            self.show_message("Warning", "Please enter double bingo books to be printed")
            return
        if bingo_single_sheets_to_print != "" and bingo_single_sheets_to_print.isnumeric()==False:
            self.show_message("Warning", "Please type right number format.")
            return
        if self.book_kind==0 and bingo_books_to_print=="":
            self.show_message("Warning", "Please enter single sheets to be printed")
            return
        if perm_range_from != "" and perm_range_from.isnumeric()==False:
            self.show_message("Warning", "Please type right number format.")
            return
        elif perm_range_from == "":
            self.show_message("Warning", "Please enter 'From' of range.")
            return
        if perm_range_to != "" and perm_range_to.isnumeric()==False:
            self.show_message("Warning", "Please type right number format.")
            return
        page_title = self.pageTitleEdit.text()
        logo_path = self.chooseLogoEdit.text()
        # date_from = self.time_from.dateTime()
        # date_to = self.time_to.dateTime()
        # if date_from > date_to:
        #     self.show_message('Warning', 'Choose right time period')
        #     return
        perm_int_range_from = 0
        perm_int_range_to = 0
        bingo_int_pages_per_book = 0
        bingo_int_books_to_print = 0
        bingo_int_double_books_to_print = 0
        bingo_int_single_sheets_to_print = 0
        if perm_range_from != "":
            perm_int_range_from = int(perm_range_from)
        if perm_range_to != "":
            perm_int_range_to = int(perm_range_to)
        if bingo_pages_per_book != "":
            bingo_int_pages_per_book = int(bingo_pages_per_book)
        if bingo_books_to_print != "":
            bingo_int_books_to_print = int(bingo_books_to_print)
        if bingo_double_books_to_print != "":
            bingo_int_double_books_to_print = int(bingo_double_books_to_print)
        if bingo_single_sheets_to_print != "":
            bingo_int_single_sheets_to_print = int(bingo_single_sheets_to_print)
        session_name = self.session_combobox.currentText()
        pdfWriter.makePdf(self.session_id, session_name, self.book_kind, bingo_int_pages_per_book, bingo_int_books_to_print, bingo_int_double_books_to_print, bingo_int_single_sheets_to_print, perm_int_range_from, perm_int_range_to, page_title, logo_path, colors, self.single_sheet_color)

    def show_message(self, title, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()