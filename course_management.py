from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from DbAccess.controller import *


class AddCoursePage(QWidget):
    def __init__(self, parent=None):
        super(AddCoursePage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Add Course", self)
        self.heading.move(80, 90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.courseid = QtWidgets.QLabel("Course ID:", self)
        self.courseid.move(90, 140)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.courseid.setFont(font)
        self.entercourseid = QLineEdit(self)
        self.entercourseid.setStyleSheet("background-color: rgb(255,255,255)")
        self.entercourseid.move(175,140)
        self.entercourseid.setEnabled(False)
        self.entercourseid.setFixedWidth(175)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.coursename = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.coursename.setFont(font)
        self.coursename.setObjectName("label")
        self.horizontalLayout.addWidget(self.coursename)
        self.entercoursename = QtWidgets.QLineEdit(self.widget)
        self.entercoursename.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entercoursename.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.entercoursename)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 50, 241, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fees = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.fees.setFont(font)
        self.fees.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.fees)
        self.enterfees = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enterfees.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterfees.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enterfees)
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.duration = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.duration.setFont(font)
        self.duration.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.duration)
        self.enterduration = QtWidgets.QLineEdit(self.layoutWidget)
        self.enterduration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterduration.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enterduration)
        self.submitButton = QtWidgets.QPushButton(self.frame_2)
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                        "background-color: qconicalgradient(cx:0, cy:0,"
                                        " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                        " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                        " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                        " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                        "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                        " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.submitButton.setGeometry(QtCore.QRect(260, 200, 131, 31))
        self.submitButton.setObjectName("pushButton")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.duration.setText(_translate("Form", "Duration:"))
        self.fees.setText(_translate("Form", "Fees:"))
        self.submitButton.setText(_translate("Form", "Add"))
        self.coursename.setText(_translate("Form", "Course Name:"))
        self.entercourseid.setText("")
        self.entercoursename.setText("")
        self.enterfees.setText("")
        self.enterduration.setText("")


    def addcourseintodb(self,addstudent,updatestudent):
        name = self.entercoursename.text()
        fees = self.enterfees.text()
        try:
            if int(fees)>=0:
                pass
        except ValueError:
            return False
        duration = self.enterduration.text()
        addcourseintodb = CourseDataIntoDB()
        if "" in (name,fees,duration):
            return False
        if addcourseintodb.addcourseintodb(name,fees,duration):
            updatestudent.updateCoursesInList()
            addstudent.updateCoursesInList()
            return True
        else:
            return False

    def showcourseid(self):
        showcourseid = CourseDataIntoDB()
        courseid = showcourseid.showcourseidfromdb()
        for ids in courseid:
            id = ids[0]
        self.entercourseid.setText(str(id))

class ViewCoursePage(QWidget):
    def __init__(self, parent= None):
        super(ViewCoursePage, self).__init__(parent)
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
        self.heading = QtWidgets.QLabel("Available Courses",self)
        self.heading.move(80,90)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.heading.setFont(font)
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Course ID','Name','Fees','Duration'))
        self.table.setGeometry(80,130,500,300)
        self.table.verticalHeader().hide()
        self.table.setColumnWidth(0,125)
        self.table.setColumnWidth(1,125)
        self.table.setColumnWidth(2,125)
        self.table.setColumnWidth(3,125)
        self.table.setStyleSheet("background-color: rgb(255,255,255);")


    def showavailablecourses(self):
        showcourses = CourseDataIntoDB()
        count = showcourses.showavailablecourses()
        nos = count[0]
        for no in nos:
            number = int(no[0])
        self.table.setRowCount(number + 6)
        for i in range(0, number + 6):
            for j in range(0, 6):
                self.table.setItem(i, j, QTableWidgetItem(""))
        i = 0
        data = count[1]
        for each_data in data:
            if i < number:
                self.table.setItem(i, 0, QTableWidgetItem(str(each_data[0])))
                self.table.setItem(i, 1, QTableWidgetItem(str(each_data[1])))
                self.table.setItem(i, 2, QTableWidgetItem(str(each_data[2])))
                self.table.setItem(i, 3, QTableWidgetItem(str(each_data[3])))
            i = i + 1