from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtPrintSupport
from PyQt5.QtWidgets import *
from DbAccess.controller import ExpenseDataIntoDb
import calendar

global month_name
month_name = list()
for name in calendar.month_name:
    month_name.append(name)


class PaySalaryPage(QWidget):
    def __init__(self, parent= None):
        super(PaySalaryPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Pay Salary",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.staffid = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.staffid.setFont(font)
        self.staffid.setObjectName("label")
        self.horizontalLayout.addWidget(self.staffid)
        self.enterstaffid = QtWidgets.QLineEdit(self.widget)
        self.enterstaffid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterstaffid.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enterstaffid)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DOP = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOP.setFont(font)
        self.DOP.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.DOP)
        self.enterdate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterdate.setCalendarPopup(True)
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.enterdate)
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.submitButton.setGeometry(QtCore.QRect(260, 120, 131, 31))
        self.submitButton.setObjectName("pushButton")

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.DOP.setText(_translate("Form", "Date of Payment:"))
        self.submitButton.setText(_translate("Form", "Submit"))
        self.staffid.setText(_translate("Form", "Staff ID:"))
        self.enterstaffid.setText("")
        self.enterdate.setDate(QtCore.QDate.currentDate())

    def paysalaryintodb(self):
        staffid = self.enterstaffid.text()
        try:
            if int(staffid) >= 0:
                pass
        except ValueError:
            return False
        getdata = ExpenseDataIntoDb()
        salary = getdata.getSalary(staffid)
        if salary < 0:
            return False
        name = getdata.getName('staff','staffid',staffid)
        description = "Paid salary to " + name
        date_format = self.enterdate.text().split('-',2)
        DOE = date_format[2] + '-' + date_format[1] + '-' + date_format[0]
        month_no = int(self.enterdate.text().split('-',2)[1])
        month = month_name[month_no]
        year = self.enterdate.text().split('-',2)[2]
        category = "Salary"
        insertintodb = ExpenseDataIntoDb()
        if insertintodb.insertIntoDb(description,salary,DOE,month,year,category):
            return True
        else:
            return False


class AddExpensePage(QWidget):
    def __init__(self, parent= None):
        super(AddExpensePage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Add Expense",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.description = QtWidgets.QLabel("Expense Description:",self)
        self.description.move(80,145)
        self.enterdescription = QtWidgets.QLineEdit(self)
        self.enterdescription.move(240,145)
        self.enterdescription.setStyleSheet("background-color: rgb(255, 255, 255);border-color: qlineargradient(spread:pad, "\
                                       "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"\
                                       "border-color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.description.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.amount = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.amount.setFont(font)
        self.amount.setObjectName("label")
        self.horizontalLayout.addWidget(self.amount)
        self.enteramount = QtWidgets.QLineEdit(self.widget)
        self.enteramount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enteramount.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enteramount)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DOP = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOP.setFont(font)
        self.DOP.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.DOP)
        self.enterdate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterdate.setCalendarPopup(True)
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.enterdate)
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.submitButton.setGeometry(QtCore.QRect(260, 130, 131, 31))
        self.submitButton.setObjectName("pushButton")


        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.DOP.setText(_translate("Form", "Date of Payment:"))
        self.submitButton.setText(_translate("Form", "Add"))
        self.amount.setText(_translate("Form", "Amount:"))
        self.enteramount.setText("")
        self.enterdescription.setText("")
        self.enterdate.setDate(QtCore.QDate.currentDate())

    def insertintodb(self):
        description = self.enterdescription.text()
        amount = self.enteramount.text()
        try:
            if int(amount) >=0:
                pass
        except ValueError:
            return False
        date_format = self.enterdate.text().split('-',2)
        DOE = date_format[2] + '-' + date_format[1] + "-" + date_format[0]
        month_no = int(self.enterdate.text().split('-',2)[1])
        month = month_name[month_no]
        year = self.enterdate.text().split('-',2)[2]
        category = "Other"
        if "" in (description,amount):
            return False
        insertintodb = ExpenseDataIntoDb()
        if insertintodb.insertIntoDb(description,amount,DOE,month,year,category):
            return True
        else:
            return False


class feesPaidPage(QWidget):
    def __init__(self, parent=None):
        super(feesPaidPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Enter Details", self)
        self.heading.move(80, 90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.rollno = QtWidgets.QLabel("Roll No:", self)
        self.rollno.move(80, 145)
        self.enterrollno = QtWidgets.QLineEdit(self)
        self.enterrollno.move(145, 145)
        self.enterrollno.setStyleSheet(
            "background-color: rgb(255, 255, 255);border-color: qlineargradient(spread:pad, " \
            "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));" \
            "border-color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.rollno.setFont(font)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.feespaid = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.feespaid.setFont(font)
        self.feespaid.setObjectName("label")
        self.horizontalLayout.addWidget(self.feespaid)
        self.enterfees = QtWidgets.QLineEdit(self.widget)
        self.enterfees.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterfees.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enterfees)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DOP = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOP.setFont(font)
        self.DOP.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.DOP)
        self.enterdate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterdate.setCalendarPopup(True)
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.enterdate)
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                        "background-color: qconicalgradient(cx:0, cy:0,"
                                        " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                        " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                        " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                        " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                        "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                        " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.submitButton.setGeometry(QtCore.QRect(260, 120, 131, 31))
        self.submitButton.setObjectName("pushButton")
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.DOP.setText(_translate("Form", "Date of Payment:"))
        self.submitButton.setText(_translate("Form", "Submit"))
        self.feespaid.setText(_translate("Form", "Amount:"))
        self.enterrollno.setText("")
        self.enterfees.setText("")
        self.enterdate.setDate(QtCore.QDate.currentDate())

    def studentFeesIntoDb(self):
        insertintodb = ExpenseDataIntoDb()
        name = insertintodb.getName('student', 'rollno', self.enterrollno.text())
        if name == 0:
            return False
        description = 'Fees deposited by ' + name
        print(description)
        amount = self.enterfees.text()
        try:
            if int(amount) >=0:
                pass
        except ValueError:
            return False
        date_format = self.enterdate.text().split('-', 2)
        DOE = date_format[2] + '-' + date_format[1] + "-" + date_format[0]
        month_no = int(self.enterdate.text().split('-', 2)[1])
        month = month_name[month_no]
        year = self.enterdate.text().split('-', 2)[2]
        category = "Fees"
        if insertintodb.insertIntoDb(description, amount, DOE, month, year, category):
            insertintodb.feesDetailIntoDb(self.enterrollno.text(),amount)
            return True
        else:
            return False

class ViewExpensePage(QWidget):
    def __init__(self, parent= None):
        super(ViewExpensePage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("View Expense",self)
        self.heading.move(80,100)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)

        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 20, 200, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.category = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.category.setFont(font)
        self.category.setObjectName("label")
        self.horizontalLayout.addWidget(self.category)
        self.entercategory = QtWidgets.QComboBox(self.widget)
        self.entercategory.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entercategory.setObjectName("combobox")
        self.entercategory.addItem("")
        self.entercategory.addItem("")
        self.entercategory.addItem("")
        self.entercategory.addItem("")
        self.entercategory.addItem("")
        self.horizontalLayout.addWidget(self.entercategory)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 70, 200, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DOS = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOS.setFont(font)
        self.DOS.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.DOS)
        self.enterstartdate = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.enterstartdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterstartdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterstartdate.setCalendarPopup(True)
        self.enterstartdate.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.enterstartdate)


        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(350, 70, 200, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DOE = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOE.setFont(font)
        self.DOE.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.DOE)
        self.enterenddate = QtWidgets.QDateEdit(self.layoutWidget_4)
        self.enterenddate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterenddate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterenddate.setCalendarPopup(True)
        self.enterenddate.setObjectName("dateEdit_2")
        self.horizontalLayout_4.addWidget(self.enterenddate)
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.submitButton.setGeometry(QtCore.QRect(260, 120, 131, 31))
        self.submitButton.setObjectName("pushButton")
        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.DOS.setText(_translate("Form", "Start Date:"))
        self.DOE.setText(_translate("Form", "End Date:"))
        self.submitButton.setText(_translate("Form", "Submit"))
        self.category.setText(_translate("Form", "Category:"))
        self.entercategory.setItemText(0, _translate("Form", "All"))
        self.entercategory.setItemText(1, _translate("Form", "Salary"))
        self.entercategory.setItemText(2, _translate("Form", "Fees"))
        self.entercategory.setItemText(3, _translate("Form", "All Debited"))
        self.entercategory.setItemText(4, _translate("Form", "Other"))
        self.enterstartdate.setDate(QtCore.QDate.currentDate())
        self.enterenddate.setDate(QtCore.QDate.currentDate())

    def getdatafromdb(self):
        category = self.entercategory.currentText()
        DOS = self.enterstartdate.text()
        DOE = self.enterenddate.text()
        getdata = ExpenseDataIntoDb()
        data = getdata.showdataintotable(category,DOS,DOE)
        return data


class ShowExpensePage(QWidget):
    def __init__(self, parent= None):
        super(ShowExpensePage, self).__init__(parent)
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
        self.layoutWidget_2 = QtWidgets.QWidget(self)
        self.layoutWidget_2.setGeometry(QtCore.QRect(180, 90, 170, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DOS = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOS.setFont(font)
        self.DOS.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.DOS)
        self.enterstartdate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enterstartdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterstartdate.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.enterstartdate)
        self.enterstartdate.setEnabled(False)

        self.layoutWidget_4 = QtWidgets.QWidget(self)
        self.layoutWidget_4.setGeometry(QtCore.QRect(360, 90, 170, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DOE = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOE.setFont(font)
        self.DOE.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.DOE)
        self.enterenddate = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.enterenddate.setEnabled(False)
        self.enterenddate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterenddate.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.enterenddate)
        self.printButton = QtWidgets.QPushButton(self)
        self.printButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.printButton.setGeometry(QtCore.QRect(540, 85, 131, 31))
        self.printButton.setObjectName("pushButton")
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.backButton.setGeometry(QtCore.QRect(280, 470, 131, 31))
        self.backButton.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 90, 150, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.category = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.category.setFont(font)
        self.category.setObjectName("label")
        self.horizontalLayout.addWidget(self.category)
        self.entercategory = QtWidgets.QComboBox(self.widget)
        self.entercategory.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entercategory.setObjectName("combobox")
        self.entercategory.addItem("")
        self.entercategory.addItem("")
        self.entercategory.addItem("")
        self.entercategory.addItem("")
        self.entercategory.setEnabled(False)
        self.horizontalLayout.addWidget(self.entercategory)

        self.table = QtWidgets.QTableWidget(self.frame_2)
        self.table.setGeometry(10,50,600,390)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0,250)
        self.table.setColumnWidth(1,150)
        self.table.setColumnWidth(2,175)
        self.table.setHorizontalHeaderLabels(("Description","Amount","Date of Expense"))
        #self.table.setRowCount(300)
        self.table.setStyleSheet("background-color: rgb(255,255,255);")
        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.DOS.setText(_translate("Form", "Start Date:"))
        self.DOE.setText(_translate("Form", "End Date:"))
        self.backButton.setText(_translate("Form", "Back"))
        self.printButton.setText(_translate("Form", "Print"))
        self.category.setText(_translate("Form", "Category:"))
        self.entercategory.setItemText(0, _translate("Form", "All"))
        self.entercategory.setItemText(1, _translate("Form", "Salary"))
        self.entercategory.setItemText(2, _translate("Form", "Fees"))
        self.entercategory.setItemText(3, _translate("Form", "All Debited"))
        self.entercategory.setItemText(4, _translate("Form", "Others"))
        self.enterstartdate.setText("")
        self.enterenddate.setText("")

    def showData(self,data):
        self.enterstartdate.setText(str(data[2]))
        self.enterenddate.setText(str(data[3]))
        count = data[0]
        for number in count:
            noofrecords = int(number[0])
            print(noofrecords)
        self.table.setRowCount(noofrecords+8)
        for i in range(0,noofrecords+6):
            for j in range(0,3):
                self.table.setItem(i,j,QTableWidgetItem(""))
        exp_data = data[1]
        i =0
        for each_data in exp_data:
            x = each_data[2].split('-',2)
            y = x[2] + '-' + x[1] + '-' + x[0]
            if i<noofrecords:
                self.table.setItem(i, 0, QTableWidgetItem(str(each_data[0])))
                self.table.setItem(i, 1, QTableWidgetItem(str(each_data[1])))
                self.table.setItem(i, 2, QTableWidgetItem(str(y)))
            i = i+1


    def printpreviewdialog(self):
        printer = QtPrintSupport.QPrinter()
        printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
        printer.setPageSize(QtPrintSupport.QPrinter.A4)
        printer.setPaperSize(QtPrintSupport.QPrinter.A4)
        printer.setPageMargins(25,15,25,25,QtPrintSupport.QPrinter.Millimeter)
        previewdialog = QtPrintSupport.QPrintPreviewDialog(printer, self)
        previewdialog.paintRequested.connect(self.printpreview)
        previewdialog.exec_()

    def printpreview(self, printer):
        self.table.render(printer)