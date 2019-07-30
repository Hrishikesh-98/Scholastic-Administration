from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from DbAccess.controller import *

class AvailableBookPage(QWidget):
    def __init__(self, parent= None):
        super(AvailableBookPage, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                           "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                           "border-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 100, 641, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 721, 301))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                                   "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                                   "border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.heading = QtWidgets.QLabel("Available Books",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 70, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.noofbook = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.noofbook.setFont(font)
        self.noofbook.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.noofbook)
        self.enternoofbook = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enternoofbook.setEnabled(False)
        self.enternoofbook.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enternoofbook.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enternoofbook)
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.backButton.setGeometry(QtCore.QRect(280, 450, 131, 31))
        self.backButton.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 70, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.bookname.setFont(font)
        self.bookname.setObjectName("label")
        self.horizontalLayout.addWidget(self.bookname)
        self.enterbookname = QtWidgets.QLineEdit(self.widget)
        self.enterbookname.setEnabled(False)
        self.enterbookname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterbookname.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enterbookname)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(('Book ID','Name','Author','Publication','Edition','Issued'))
        self.table.setGeometry(80,130,630,300)
        self.table.verticalHeader().hide()
        self.table.setColumnWidth(0,80)
        self.table.setColumnWidth(1,130)
        self.table.setColumnWidth(2,130)
        self.table.setColumnWidth(3,130)
        self.table.setColumnWidth(4,80)
        self.table.setColumnWidth(5,80)
        self.table.setStyleSheet("background-color: rgb(255,255,255);")
        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.noofbook.setText(_translate("Form", "Copies Available:"))
        self.backButton.setText(_translate("Form", "Back"))
        self.bookname.setText(_translate("Form", "Book Name:"))
        self.enterbookname.setText("")
        self.enternoofbook.setText("")

    def showavailability(self,bookname,count,num):
        if num == 'Single':
            self.hidingWidgets()
            self.widget.show()
            self.layoutWidget.show()
            self.layoutWidget_2.show()
            self.enterbookname.setText(bookname)
            self.enternoofbook.setText(str(count))
        else:
            self.hidingWidgets()
            self.table.show()
            nos = count[0]
            for no in nos:
                number = int(no[0])
            self.table.setRowCount(number+6)
            for i in range(0,number+6):
                for j in range(0,6):
                    self.table.setItem(i,j,QTableWidgetItem(""))
            i = 0
            data = count[1]
            for each_data in data:
                if i<number:
                    self.table.setItem(i,0,QTableWidgetItem(str(each_data[0])))
                    self.table.setItem(i,1,QTableWidgetItem(str(each_data[1])))
                    self.table.setItem(i,2,QTableWidgetItem(str(each_data[2])))
                    self.table.setItem(i,3,QTableWidgetItem(str(each_data[3])))
                    self.table.setItem(i,4,QTableWidgetItem(str(each_data[4])))
                    self.table.setItem(i,5,QTableWidgetItem(str(each_data[5])))
                i = i+1

    def hidingWidgets(self):
        self.table.hide()
        self.widget.hide()
        self.layoutWidget_2.hide()
        self.layoutWidget.hide()

class SearchforAvailabilityPage(QWidget):
    def __init__(self, parent= None):
        super(SearchforAvailabilityPage, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                           "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                           "border-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 100, 641, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 721, 301))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                                   "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                                   "border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.heading = QtWidgets.QLabel("Check Book Availability",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.searchButton = QtWidgets.QPushButton(self.frame_2)
        self.searchButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                        "background-color: qconicalgradient(cx:0, cy:0,"
                                        " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                        " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                        " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                        " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                        "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                        " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.searchButton.setGeometry(QtCore.QRect(60, 120, 131, 31))
        self.searchButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(250, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.bookname.setFont(font)
        self.bookname.setObjectName("label")
        self.horizontalLayout.addWidget(self.bookname)
        self.enterbookname = QtWidgets.QLineEdit(self.widget)
        self.enterbookname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterbookname.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enterbookname)
        self.widget.hide()

        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 50, 200, 22))
        self.widget_2.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout")
        self.showbook = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.showbook.setFont(font)
        self.showbook.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.showbook)
        self.entershowbook = QtWidgets.QComboBox(self.widget_2)
        self.entershowbook.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entershowbook.setObjectName("combobox")
        self.horizontalLayout_2.addWidget(self.entershowbook)
        self.entershowbook.addItem("All")
        self.entershowbook.addItem("Issued")
        self.entershowbook.addItem("Single")
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.bookname.setText(_translate("Form", "Book Name:"))
        self.searchButton.setText(_translate("Form", "Search"))
        self.enterbookname.setText("")
        self.showbook.setText(_translate("Form", "Show"))
        self.entershowbook.setCurrentIndex(0)

    def chechavailability(self):
        bookname = self.enterbookname.text()
        checkbook = LibraryDataIntoDB()
        count = checkbook.checkavailablebooks(bookname,self.entershowbook.currentText())
        return count

    def showWidget(self):
        if self.entershowbook.currentText() == 'Single':
            self.enterbookname.setText("")
            self.widget.show()
        else:
            self.widget.hide()

class issueBookPage(QWidget):
    def __init__(self, parent= None):
        super(issueBookPage, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                           "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                           "border-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 100, 641, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 721, 301))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                                   "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                                   "border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.heading = QtWidgets.QLabel("Issue Book",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.rollno = QtWidgets.QLabel("Roll No:",self)
        self.rollno.move(80,145)
        self.enterrollno = QtWidgets.QLineEdit(self)
        self.enterrollno.move(145,145)
        self.enterrollno.setStyleSheet("background-color: rgb(255, 255, 255);border-color: qlineargradient(spread:pad, "\
                                       "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                                       "border-color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.rollno.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookid = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.bookid.setFont(font)
        self.bookid.setObjectName("label")
        self.horizontalLayout.addWidget(self.bookid)
        self.enterbookid = QtWidgets.QLineEdit(self.widget)
        self.enterbookid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterbookid.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enterbookid)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DOI = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOI.setFont(font)
        self.DOI.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.DOI)
        self.enterdate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterdate.setCalendarPopup(True)
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.enterdate)
        self.issueButton = QtWidgets.QPushButton(self.frame_2)
        self.issueButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.issueButton.setGeometry(QtCore.QRect(260, 100, 131, 31))
        self.issueButton.setObjectName("pushButton")

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.DOI.setText(_translate("Form", "Date of Issue:"))
        self.issueButton.setText(_translate("Form", "Issue"))
        self.bookid.setText(_translate("Form", "Book ID:"))
        self.enterrollno.setText("")
        self.enterbookid.setText("")
        self.enterdate.setDate(QtCore.QDate.currentDate())

    def issuebookintodb(self):
        issue = LibraryDataIntoDB()
        rollno = self.enterrollno.text()
        bookid = self.enterbookid.text()
        DOI = self.enterdate.text()
        date = DOI.split('-', 2)
        d = QtCore.QDate(int(date[2]), int(date[1]), int(date[0]))
        DOR = d.addDays(7).toString(QtCore.Qt.DefaultLocaleShortDate)
        if '' in (rollno,bookid,DOI):
            return 2
        else:
            if issue.issuebookintodb(rollno,bookid,DOI,DOR) == 1:
                return 1
            elif issue.issuebookintodb(rollno,bookid,DOI,DOR) == 2:
                return 3
            else:
                return 2

class returnBookPage(QWidget):
    def __init__(self, parent= None):
        super(returnBookPage, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                           "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                           "border-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 100, 641, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 721, 301))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, "\
                                   "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                                   "border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.heading = QtWidgets.QLabel("Return Book",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.rollno = QtWidgets.QLabel("Roll No:",self)
        self.rollno.move(80,145)
        self.enterrollno = QtWidgets.QLineEdit(self)
        self.enterrollno.move(145,145)
        self.enterrollno.setStyleSheet("background-color: rgb(255, 255, 255);border-color: qlineargradient(spread:pad, "\
                                       "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                                       "border-color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.rollno.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookid = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.bookid.setFont(font)
        self.bookid.setObjectName("label")
        self.horizontalLayout.addWidget(self.bookid)
        self.enterbookid = QtWidgets.QLineEdit(self.widget)
        self.enterbookid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterbookid.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enterbookid)

        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DOR = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOR.setFont(font)
        self.DOR.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.DOR)
        self.enterdate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterdate.setCalendarPopup(True)
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.enterdate)
        self.returnButton = QtWidgets.QPushButton(self.frame_2)
        self.returnButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                        "background-color: qconicalgradient(cx:0, cy:0,"
                                        " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                        " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                        " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                        " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                        "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                        " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.returnButton.setGeometry(QtCore.QRect(260, 110, 131, 31))
        self.returnButton.setObjectName("pushButton")


        self.widget_3 = QtWidgets.QWidget(self.frame_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 90, 271, 22))
        self.widget_3.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fine = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.fine.setFont(font)
        self.fine.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.fine)
        self.enterfine = QtWidgets.QLineEdit(self.widget_3)
        self.enterfine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterfine.setObjectName("lineEdit_3")
        self.enterfine.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.enterfine)
        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.DOR.setText(_translate("Form", "Date of Return:"))
        self.returnButton.setText(_translate("Form", "Return"))
        self.bookid.setText(_translate("Form", "Book ID:"))
        self.fine.setText(_translate("Form", "Fine:"))
        self.enterrollno.setText("")
        self.enterdate.setDate(QtCore.QDate.currentDate())
        self.enterbookid.setText("")
        self.enterfine.setText("")

    def returnbooktodb(self):
        returnintodb = LibraryDataIntoDB()
        rollno = self.enterrollno.text()
        bookid = self.enterbookid.text()
        DOR = self.enterdate.text()
        fine = returnintodb.calculatefine(rollno,DOR)
        if fine == 'None':
            return 0
        else:
            self.enterfine.setText(str(fine))
            if returnintodb.returnbookintodb(rollno,bookid):
                return 1
            else:
                return 2


class AddBookPage(QWidget):
    def __init__(self, parent=None):
        super(AddBookPage, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, " \
                           "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));" \
                           "border-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 100, 641, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 721, 301))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 178);border-color: qlineargradient(spread:pad, " \
                                   "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));" \
                                   "border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.heading = QtWidgets.QLabel("Add Book", self)
        self.heading.move(80, 90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.bookid = QtWidgets.QLabel("Book ID:", self)
        self.bookid.move(105, 145)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.bookid.setFont(font)
        self.enterbookid = QLineEdit(self)
        self.enterbookid.setStyleSheet("background-color: rgb(255,255,255)")
        self.enterbookid.move(175,145)
        self.enterbookid.setFixedWidth(175)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.bookname.setFont(font)
        self.bookname.setObjectName("label")
        self.horizontalLayout.addWidget(self.bookname)
        self.enterbookname = QtWidgets.QLineEdit(self.widget)
        self.enterbookname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterbookname.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enterbookname)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.author = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.author.setFont(font)
        self.author.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.author)
        self.enterauthor = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enterauthor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterauthor.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enterauthor)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.publication = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.publication.setFont(font)
        self.publication.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.publication)
        self.enterpublication = QtWidgets.QLineEdit(self.layoutWidget)
        self.enterpublication.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterpublication.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enterpublication)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(380, 100, 241, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edition = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.edition.setFont(font)
        self.edition.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.edition)
        self.enteredition = QtWidgets.QLineEdit(self.widget1)
        self.enteredition.setStyleSheet("background-color: rgb(255,255,255)")
        self.enteredition.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.enteredition)
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                        "background-color: qconicalgradient(cx:0, cy:0,"
                                        " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                        " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                        " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                        " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                        "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                        " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.submitButton.setGeometry(QtCore.QRect(260, 220, 131, 31))
        self.submitButton.setObjectName("pushButton")



        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.publication.setText(_translate("Form", "Publication:"))
        self.author.setText(_translate("Form", "Author:"))
        self.submitButton.setText(_translate("Form", "Add"))
        self.bookname.setText(_translate("Form", "Book Name:"))
        self.edition.setText(_translate("Form", "Edition:"))
        self.enterbookid.setText("")
        self.enterbookname.setText("")
        self.enterauthor.setText("")
        self.enterpublication.setText("")
        self.enteredition.setText("")


    def addbookintodb(self):
        bookid = self.enterbookid.text()
        name = self.enterbookname.text()
        author = self.enterauthor.text()
        publication = self.enterpublication.text()
        edition = self.enteredition.text()
        addbookintodb = LibraryDataIntoDB()
        if "" in (bookid,name,author,publication,edition):
            return False
        else:
            if addbookintodb.addbookintodb(bookid,name,author,publication,edition):
                return True
            else:
                return False


