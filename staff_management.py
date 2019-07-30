from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from DbAccess.controller import *


class AddStaffPage(QWidget):
    def __init__(self, parent= None):
        super(AddStaffPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Add Staff Details",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.staffid = QtWidgets.QLabel("Staff ID:",self)
        self.staffid.move(80,145)
        self.enterstaffid = QtWidgets.QLineEdit(self)
        self.enterstaffid.setStyleSheet("background-color: rgb(255,255,255);")
        self.enterstaffid.setEnabled(False)
        self.enterstaffid.move(150,145)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.staffid.setFont(font)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.name.setFont(font)
        self.name.setObjectName("label")
        self.horizontalLayout.addWidget(self.name)
        self.entername = QtWidgets.QLineEdit(self.widget)
        self.entername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entername.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.entername)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.phnno = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.phnno.setFont(font)
        self.phnno.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.phnno)
        self.enterphnno = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enterphnno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterphnno.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enterphnno)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.address = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.address.setFont(font)
        self.address.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.address)
        self.enteraddress = QtWidgets.QLineEdit(self.layoutWidget)
        self.enteraddress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enteraddress.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enteraddress)
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

        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(380, 100, 241, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gender = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gender.setFont(font)
        self.gender.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.gender)
        self.maleButton = QtWidgets.QRadioButton(self.widget1)
        self.maleButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.maleButton)
        self.femaleButton = QtWidgets.QRadioButton(self.widget1)
        self.femaleButton.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.femaleButton)
        self.widget2 = QtWidgets.QWidget(self.frame_2)
        self.widget2.setGeometry(QtCore.QRect(10, 150, 271, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DOJ = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOJ.setFont(font)
        self.DOJ.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.DOJ)
        self.enterdate = QtWidgets.QDateEdit(self.widget2)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterdate.setCalendarPopup(True)
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.enterdate)
        self.widget3 = QtWidgets.QWidget(self.frame_2)
        self.widget3.setGeometry(QtCore.QRect(380, 150, 241, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.salary = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.salary.setFont(font)
        self.salary.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.salary)
        self.entersalary = QtWidgets.QLineEdit(self.widget3)
        self.entersalary.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entersalary.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.entersalary)
        self.maleButton.setChecked(True)
        self.insertintodb = StaffDataIntoDb()

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.address.setText(_translate("Form", "Address:"))
        self.phnno.setText(_translate("Form", "Phone No:"))
        self.submitButton.setText(_translate("Form", "Submit"))
        self.name.setText(_translate("Form", "Name:"))
        self.gender.setText(_translate("Form", "Gender:"))
        self.maleButton.setText(_translate("Form", "Male"))
        self.femaleButton.setText(_translate("Form", "Female"))
        self.DOJ.setText(_translate("Form", "Date of Joining:"))
        self.salary.setText(_translate("Form", "Salary:"))
        self.entername.setText("")
        self.enterphnno.setText("")
        self.enteraddress.setText("")
        self.enterdate.setDate(QtCore.QDate.currentDate())
        self.entersalary.setText("")

    def insert(self):
        print("in")
        name = self.entername.text()
        phn = self.enterphnno.text()
        phn_nos = phn.split(",", phn.count(','))
        for i in range(phn.count(',') + 1):
            try:
                if int(phn_nos[i]) > 999999999 and int(phn_nos[i]) < 10000000000:
                    pass
                else:
                    return False
            except ValueError:
                return False
        address = self.enteraddress.text()
        DOJ = self.enterdate.text()
        salary = self.entersalary.text()
        try:
            if int(salary) >= 0:
                pass
        except ValueError:
            return False
        if "" in (name,phn,address,DOJ,salary):
            return False
        else:
            if self.maleButton.isChecked():
                gender = 'M'
                if self.insertintodb.insertIntoDb(name, phn, address, gender, DOJ, salary):
                    return True
                else:
                    return False
            elif self.femaleButton.isChecked():
                gender = 'F'
                if self.insertintodb.insertIntoDb(name, phn, address, gender, DOJ, salary):
                    return True
                else:
                    return False
            else:
                return False

    def show_sid(self):
        sid = self.insertintodb.showstaffid()
        self.enterstaffid.setText(str(sid))


class SearchforDeleteStaffPage(QWidget):
    def __init__(self, parent= None):
        super(SearchforDeleteStaffPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Delete Staff Member",self)
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
        self.searchButton.setGeometry(QtCore.QRect(60, 100, 131, 31))
        self.searchButton.setObjectName("pushButton")
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

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.staffid.setText(_translate("Form", "Staff ID:"))
        self.searchButton.setText(_translate("Form", "Search"))


    def searchstaffid(self,deletepage):
        staffid = self.enterstaffid.text()
        try:
            if int(staffid) >=0:
                self.viewdata = ViewStaffData(staffid,"Single")
                data = self.viewdata.returndata()
                deletepage.viewdatatodelete(data)
                return True
        except ValueError:
            return False

class deleteStaffPage(QWidget):
    def __init__(self, parent= None):
        super(deleteStaffPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Delete Staff Member",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.staffid = QtWidgets.QLabel("Staff ID:",self)
        self.staffid.move(80,145)
        self.enterstaffid = QtWidgets.QLineEdit(self)
        self.enterstaffid.move(150,145)
        self.enterstaffid.setEnabled(False)
        self.enterstaffid.setStyleSheet("background-color: rgb(255,255,255);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.staffid.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.address = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.address.setFont(font)
        self.address.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.address)
        self.enteraddress = QtWidgets.QLineEdit(self.layoutWidget)
        self.enteraddress.setEnabled(False)
        self.enteraddress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enteraddress.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enteraddress)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.phnno = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.phnno.setFont(font)
        self.phnno.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.phnno)
        self.enterphnno = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enterphnno.setEnabled(False)
        self.enterphnno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterphnno.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enterphnno)
        self.deleteButton = QtWidgets.QPushButton(self.frame_2)
        self.deleteButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                      "background-color: qconicalgradient(cx:0, cy:0,"
                                      " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                      " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                      " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                      " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                      "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                      " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.deleteButton.setGeometry(QtCore.QRect(200, 250, 131, 31))
        self.deleteButton.setObjectName("pushButton")

        self.backButton = QtWidgets.QPushButton(self.frame_2)
        self.backButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.backButton.setGeometry(QtCore.QRect(350, 250, 131, 31))
        self.backButton.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.name.setFont(font)
        self.name.setObjectName("label")
        self.horizontalLayout.addWidget(self.name)
        self.entername = QtWidgets.QLineEdit(self.widget)
        self.entername.setEnabled(False)
        self.entername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entername.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.entername)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(380, 100, 241, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gender = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gender.setFont(font)
        self.gender.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.gender)
        self.maleButton = QtWidgets.QRadioButton(self.widget1)
        self.maleButton.setObjectName("radioButton")
        self.maleButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.maleButton)
        self.femaleButton = QtWidgets.QRadioButton(self.widget1)
        self.femaleButton.setObjectName("radioButton_2")
        self.femaleButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.femaleButton)
        self.widget2 = QtWidgets.QWidget(self.frame_2)
        self.widget2.setGeometry(QtCore.QRect(10, 150, 271, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DOJ = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOJ.setFont(font)
        self.DOJ.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.DOJ)
        self.enterdate = QtWidgets.QLineEdit(self.widget2)
        self.enterdate.setEnabled(False)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.enterdate)
        self.widget3 = QtWidgets.QWidget(self.frame_2)
        self.widget3.setGeometry(QtCore.QRect(380, 150, 241, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.salary = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.salary.setFont(font)
        self.salary.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.salary)
        self.entersalary = QtWidgets.QLineEdit(self.widget3)
        self.entersalary.setEnabled(False)
        self.entersalary.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout_6.addWidget(self.entersalary)

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.address.setText(_translate("Form", "Address:"))
        self.phnno.setText(_translate("Form", "Phone No:"))
        self.deleteButton.setText(_translate("Form", "Delete"))
        self.backButton.setText(_translate("Form", "Back"))
        self.name.setText(_translate("Form", "Name:"))
        self.gender.setText(_translate("Form", "Gender:"))
        self.maleButton.setText(_translate("Form", "Male"))
        self.femaleButton.setText(_translate("Form", "Female"))
        self.DOJ.setText(_translate("Form", "Date of Joining:"))
        self.salary.setText(_translate("Form", "Salary:"))


    def viewdatatodelete(self,data):
        for eachdata in data:
            self.enterstaffid.setText(str(eachdata[0]))
            self.entername.setText(eachdata[1])
            self.enterphnno.setText(eachdata[2])
            self.enteraddress.setText(eachdata[3])
            if eachdata[4] == 'F':
                self.femaleButton.setChecked(True)
            else:
                self.maleButton.setChecked(True)
            self.enterdate.setText(str(eachdata[5]))
            self.entersalary.setText(str(eachdata[6]))

    def DeleteStaffData(self):
        delete = StaffDataIntoDb()
        if delete.deleteStaffFromDb(self.enterstaffid.text()):
            return True
        else:
            return False

class SearchforUpdateStaffPage(QWidget):
    def __init__(self, parent= None):
        super(SearchforUpdateStaffPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Update Staff Details",self)
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
        self.searchButton.setGeometry(QtCore.QRect(60, 100, 131, 31))
        self.searchButton.setObjectName("pushButton")
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

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.staffid.setText(_translate("Form", "Staff ID:"))
        self.searchButton.setText(_translate("Form", "Search"))

    def searchstaffid(self,updatepage):
        staffid = self.enterstaffid.text()
        try:
            if int(staffid)>=0:
                self.viewdata = ViewStaffData(staffid,"Single")
                data = self.viewdata.returndata()
                updatepage.viewdatatoupdate(data)
                return True
        except ValueError:
            return False


class updateStaffPage(QWidget):
    def __init__(self, parent= None):
        super(updateStaffPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Update Staff Details",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.staffid = QtWidgets.QLabel("Staff ID:",self)
        self.staffid.move(80,145)
        self.enterstaffid = QtWidgets.QLineEdit(self)
        self.enterstaffid.move(150,145)
        self.enterstaffid.setEnabled(False)
        self.enterstaffid.setStyleSheet("background-color: rgb(255,255,255);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.staffid.setFont(font)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.name.setFont(font)
        self.name.setObjectName("label")
        self.horizontalLayout.addWidget(self.name)
        self.entername = QtWidgets.QLineEdit(self.widget)
        self.entername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entername.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.entername)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.phnno = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.phnno.setFont(font)
        self.phnno.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.phnno)
        self.enterphnno = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enterphnno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterphnno.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enterphnno)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.address = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.address.setFont(font)
        self.address.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.address)
        self.enteraddress = QtWidgets.QLineEdit(self.layoutWidget)
        self.enteraddress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enteraddress.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enteraddress)
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.submitButton.setGeometry(QtCore.QRect(200, 250, 131, 31))
        self.submitButton.setObjectName("pushButton")
        self.cancelButton = QtWidgets.QPushButton(self.frame_2)
        self.cancelButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.cancelButton.setGeometry(QtCore.QRect(350, 250, 131, 31))
        self.cancelButton.setObjectName("pushButton_2")

        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(380, 100, 241, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gender = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gender.setFont(font)
        self.gender.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.gender)
        self.maleButton = QtWidgets.QRadioButton(self.widget1)
        self.maleButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.maleButton)
        self.femaleButton = QtWidgets.QRadioButton(self.widget1)
        self.femaleButton.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.femaleButton)
        self.widget2 = QtWidgets.QWidget(self.frame_2)
        self.widget2.setGeometry(QtCore.QRect(10, 150, 271, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DOJ = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOJ.setFont(font)
        self.DOJ.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.DOJ)
        self.enterdate = QtWidgets.QDateEdit(self.widget2)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enterdate.setCalendarPopup(True)
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.enterdate)
        self.widget3 = QtWidgets.QWidget(self.frame_2)
        self.widget3.setGeometry(QtCore.QRect(380, 150, 241, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.salary = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.salary.setFont(font)
        self.salary.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.salary)
        self.entersalary = QtWidgets.QLineEdit(self.widget3)
        self.entersalary.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entersalary.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.entersalary)

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.address.setText(_translate("Form", "Address:"))
        self.phnno.setText(_translate("Form", "Phone No:"))
        self.submitButton.setText(_translate("Form", "Update"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
        self.name.setText(_translate("Form", "Name:"))
        self.gender.setText(_translate("Form", "Gender:"))
        self.maleButton.setText(_translate("Form", "Male"))
        self.femaleButton.setText(_translate("Form", "Female"))
        self.DOJ.setText(_translate("Form", "Date of Joining:"))
        self.salary.setText(_translate("Form", "Salary:"))


    def viewdatatoupdate(self,data):
        for eachdata in data:
            self.enterstaffid.setText(str(eachdata[0]))
            self.entername.setText(eachdata[1])
            self.enterphnno.setText(eachdata[2])
            self.enteraddress.setText(eachdata[3])
            if eachdata[4] == 'F':
                self.femaleButton.setChecked(True)
            else:
                self.maleButton.setChecked(True)
            print("dateinupdate" + str(eachdata[5]))
            dates = str(eachdata[5]).split('-',2)
            print(dates)
            self.enterdate.setDateTime(QtCore.QDateTime(QtCore.QDate(int(dates[2]),int(dates[1]),int(dates[0])), QtCore.QTime(0, 0, 0)))
            self.entersalary.setText(str(eachdata[6]))


    def updateStaffDataIntoDb(self):
        print("in")
        staffid = self.enterstaffid.text()
        name = self.entername.text()
        phn = self.enterphnno.text()
        address = self.enteraddress.text()
        DOJ = self.enterdate.text()
        salary = self.entersalary.text()
        updateintodb = StaffDataIntoDb()
        if self.maleButton.isChecked():
            gender = 'M'
            if updateintodb.updateIntoDb(staffid,name, phn, address, gender, DOJ,salary):
                return True
            else:
                return False
        elif self.femaleButton.isChecked():
            gender = 'F'
            if updateintodb.updateIntoDb(staffid,name, phn, address, gender, DOJ, salary):
                return True
            else:
                return False
        else:
            return False

class SearchStaffPage(QWidget):
    def __init__(self, parent= None):
        super(SearchStaffPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Search Staff Member",self)
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
        self.layoutWidget.setGeometry(QtCore.QRect(10, 45, 271, 22))
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
        self.searchButton.setGeometry(QtCore.QRect(60, 100, 131, 31))
        self.searchButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(280, 55, 271, 22))
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
        self.widget.hide()
        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 55, 200, 22))
        self.widget_2.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.noofrec = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.noofrec.setFont(font)
        self.noofrec.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.noofrec)
        self.enternoofrec = QtWidgets.QComboBox(self.widget_2)
        self.enternoofrec.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enternoofrec.setObjectName("combobox")
        self.horizontalLayout_2.addWidget(self.enternoofrec)
        self.enternoofrec.addItem("All")
        self.enternoofrec.addItem("Single")
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.staffid.setText(_translate("Form", "Staff ID:"))
        self.noofrec.setText(_translate("Form", "Show:"))
        self.searchButton.setText(_translate("Form", "Search"))

    def searchstaffid(self,searchedpage):
        staffid = self.enterstaffid.text()
        num = self.enternoofrec.currentText()
        self.viewdata = ViewStaffData(staffid,num)
        data = self.viewdata.returndata()
        if data == 0:
            return False
        else:
            if self.enternoofrec.currentText() == 'Single':
                try:
                    if int(staffid) >= 0:
                        searchedpage.viewdatatosearch(data)
                        return True
                except ValueError:
                    return False
            else:
                searchedpage.viewintable(data)
                return True

    def showstaffid(self):
        if self.enternoofrec.currentText() == 'Single':
            self.widget.show()
        else:
            self.widget.hide()
            self.enterstaffid.setText("")

class StaffSearchedPage(QWidget):
    def __init__(self, parent= None):
        super(StaffSearchedPage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Search Staff Member",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.staffid = QtWidgets.QLabel("Staff ID:",self)
        self.staffid.move(80,145)
        self.enterstaffid = QtWidgets.QLineEdit(self)
        self.enterstaffid.move(150,145)
        self.enterstaffid.setEnabled(False)
        self.enterstaffid.setStyleSheet("background-color: rgb(255,255,255);")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.staffid.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.address = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.address.setFont(font)
        self.address.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.address)
        self.enteraddress = QtWidgets.QLineEdit(self.layoutWidget)
        self.enteraddress.setEnabled(False)
        self.enteraddress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enteraddress.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enteraddress)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 70, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.phnno = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.phnno.setFont(font)
        self.phnno.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.phnno)
        self.enterphnno = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enterphnno.setEnabled(False)
        self.enterphnno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterphnno.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enterphnno)
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.backButton.setGeometry(QtCore.QRect(310, 450, 131, 31))
        self.backButton.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 70, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.name.setFont(font)
        self.name.setObjectName("label")
        self.horizontalLayout.addWidget(self.name)
        self.entername = QtWidgets.QLineEdit(self.widget)
        self.entername.setEnabled(False)
        self.entername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entername.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.entername)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(380, 120, 241, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gender = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gender.setFont(font)
        self.gender.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.gender)
        self.maleButton = QtWidgets.QRadioButton(self.widget1)
        self.maleButton.setObjectName("radioButton")
        self.maleButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.maleButton)
        self.femaleButton = QtWidgets.QRadioButton(self.widget1)
        self.femaleButton.setObjectName("radioButton_2")
        self.femaleButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.femaleButton)
        self.widget2 = QtWidgets.QWidget(self.frame_2)
        self.widget2.setGeometry(QtCore.QRect(10, 170, 271, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DOJ = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DOJ.setFont(font)
        self.DOJ.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.DOJ)
        self.enterdate = QtWidgets.QLineEdit(self.widget2)
        self.enterdate.setEnabled(False)
        self.enterdate.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.enterdate.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.enterdate)
        self.widget3 = QtWidgets.QWidget(self.frame_2)
        self.widget3.setGeometry(QtCore.QRect(380, 170, 241, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.salary = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.salary.setFont(font)
        self.salary.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.salary)
        self.entersalary = QtWidgets.QLineEdit(self.widget3)
        self.entersalary.setEnabled(False)
        self.entersalary.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout_6.addWidget(self.entersalary)
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(('Staff ID','Name','Phone No','Address','Gender','Date Of Joining','Salary'))
        self.table.setGeometry(30,135,700,300)
        self.table.verticalHeader().hide()
        self.table.setColumnWidth(0,80)
        self.table.setColumnWidth(1,130)
        self.table.setColumnWidth(3,160)
        self.table.setColumnWidth(4,50)
        self.table.setColumnWidth(6,80)
        self.table.setStyleSheet("background-color: rgb(255,255,255);")
        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.address.setText(_translate("Form", "Address:"))
        self.phnno.setText(_translate("Form", "Phone No:"))
        self.backButton.setText(_translate("Form", "Back"))
        self.name.setText(_translate("Form", "Name:"))
        self.gender.setText(_translate("Form", "Gender:"))
        self.maleButton.setText(_translate("Form", "Male"))
        self.femaleButton.setText(_translate("Form", "Female"))
        self.DOJ.setText(_translate("Form", "Date of Joining:"))
        self.salary.setText(_translate("Form", "Salary:"))


    def viewdatatosearch(self,data):
        self.hiddingWidgets()
        self.staffid.show()
        self.enterstaffid.show()
        self.widget.show()
        self.widget1.show()
        self.widget2.show()
        self.widget3.show()
        self.layoutWidget.show()
        self.layoutWidget_2.show()
        for eachdata in data:
            self.enterstaffid.setText(str(eachdata[0]))
            self.entername.setText(eachdata[1])
            self.enterphnno.setText(eachdata[2])
            self.enteraddress.setText(eachdata[3])
            if eachdata[4] == 'F':
                self.femaleButton.setChecked(True)
            else:
                self.maleButton.setChecked(True)
            self.enterdate.setText(str(eachdata[5]))
            self.entersalary.setText(str(eachdata[6]))

    def viewintable(self,data):
        self.hiddingWidgets()
        self.table.show()
        count = data[0]
        for number in count:
            no = int(number[0])
        self.table.setRowCount(no+8)
        for i in range(0,no+8):
            for j in range(0,7):
                self.table.setItem(i,j,QTableWidgetItem(""))
        i =0
        details = data[1]
        for each_detail in details:
            if i <= no:
                self.table.setItem(i,0,QTableWidgetItem(str(each_detail[0])))
                self.table.setItem(i,1,QTableWidgetItem(str(each_detail[1])))
                self.table.setItem(i,2,QTableWidgetItem(str(each_detail[2])))
                self.table.setItem(i,3,QTableWidgetItem(str(each_detail[3])))
                self.table.setItem(i,4,QTableWidgetItem(str(each_detail[4])))
                self.table.setItem(i,5,QTableWidgetItem(str(each_detail[5])))
                self.table.setItem(i,6,QTableWidgetItem(str(each_detail[6])))
            i = i+1

    def hiddingWidgets(self):
        self.table.hide()
        self.staffid.hide()
        self.enterstaffid.hide()
        self.widget.hide()
        self.widget1.hide()
        self.widget2.hide()
        self.widget3.hide()
        self.layoutWidget.hide()
        self.layoutWidget_2.hide()