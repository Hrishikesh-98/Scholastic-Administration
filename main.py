import sys
from PyQt5 import QtGui,QtCore,QtWidgets
from Student_Management.student_management import *
from Library_Management.library_management import *
from Staff_Management.staff_management import *
from Expense_Management.expense_management import *
from Course_Management.course_management import *
from DbAccess.controller import *


class MainPage(QWidget):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setup_Ui()

    def setup_Ui(self):
        self.setFixedSize(1200, 600)
        self.verticalFrame = QtWidgets.QFrame(self)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 1200, 600))
        self.verticalFrame.setStyleSheet("background-color: rgb(255, 253, 178);")
        self.line = QtWidgets.QFrame(self.verticalFrame)
        self.line.setStyleSheet("background-color: rgb(0,0,0);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameStyle(QFrame.Sunken)
        self.line.setGeometry(775,0,1,700)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.logout = QPushButton(self)
        self.logout.setStyleSheet("background-color: rgb(255, 255, 127);"
                                  "background-color: qconicalgradient(cx:0, cy:0,"
                                  " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                  " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                  " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                  " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                  "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                  " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.logout.move(1050,5)
        self.header = QtWidgets.QLabel(self.verticalFrame)
        self.header.setGeometry(QtCore.QRect(0, 0, 775, 80))
        self.header.setText("")
        self.header.setPixmap(QtGui.QPixmap(".\\header.png"))
        self.header.setScaledContents(True)
        self.header.setObjectName("label_1")
        self.background = QtWidgets.QLabel(self.verticalFrame)
        self.background.setGeometry(QtCore.QRect(30, 90, 700, 450))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(".\\welcome.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("label")
        self.toolBox = QtWidgets.QToolBox(self)
        self.toolBox.setGeometry(QtCore.QRect(800, 40, 361, 521))
        self.toolBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolBox.setStyleSheet("background-color: rgb(255, 253, 178);"
                                   "border-color: rgb(0, 0, 0);")
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox.setLineWidth(5)
        self.page = QtWidgets.QWidget(self)
        self.page.setGeometry(QtCore.QRect(0, 0, 361, 397))
        self.addStudentButton = QtWidgets.QPushButton(self.page)
        self.addStudentButton.setGeometry(QtCore.QRect(30, 10, 291, 31))
        self.addStudentButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.deleteStudentButton = QtWidgets.QPushButton(self.page)
        self.deleteStudentButton.setGeometry(QtCore.QRect(30, 60, 291, 31))
        self.deleteStudentButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                               "background-color: qconicalgradient(cx:0, cy:0,"
                                               " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                               " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                               " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                               " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                               "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                               " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.updateStudentButton = QtWidgets.QPushButton(self.page)
        self.updateStudentButton.setGeometry(QtCore.QRect(30, 110, 291, 31))
        self.updateStudentButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                               "background-color: qconicalgradient(cx:0, cy:0,"
                                               " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                               " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                               " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                               " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                               "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                               " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.searchStudentButton = QtWidgets.QPushButton(self.page)
        self.searchStudentButton.setGeometry(QtCore.QRect(30, 160, 291, 31))
        self.searchStudentButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                               "background-color: qconicalgradient(cx:0, cy:0,"
                                               " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                               " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                               " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                               " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                               "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), "
                                               "stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget(self)
        self.page_2.setGeometry(QtCore.QRect(0, 0, 361, 397))
        self.issueBookButton = QtWidgets.QPushButton(self.page_2)
        self.issueBookButton.setGeometry(QtCore.QRect(40, 10, 281, 31))
        self.issueBookButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                           "selection-background-color: rgb(255, 255, 0);"
                                           "background-color: qconicalgradient(cx:0, cy:0,"
                                           " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                           " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                           " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                           " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                           "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                           " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.returnBookButton = QtWidgets.QPushButton(self.page_2)
        self.returnBookButton.setGeometry(QtCore.QRect(40, 60, 281, 31))
        self.returnBookButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "selection-background-color: rgb(255, 255, 0);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.checkBookAvailabilityButton = QtWidgets.QPushButton(self.page_2)
        self.checkBookAvailabilityButton.setGeometry(QtCore.QRect(40, 110, 281, 31))
        self.checkBookAvailabilityButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                                       "selection-background-color: rgb(255, 255, 0);"
                                                       "background-color: qconicalgradient(cx:0, cy:0,"
                                                       " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                                       " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                                       " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                                       " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                                       "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                                       " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.addBookButton = QtWidgets.QPushButton(self.page_2)
        self.addBookButton.setGeometry(QtCore.QRect(40, 160, 281, 31))
        self.addBookButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                         "selection-background-color: rgb(255, 255, 0);"
                                         "background-color: qconicalgradient(cx:0, cy:0,"
                                         " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                         " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                         " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                         " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                         "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                         " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget(self)
        self.page_3.setGeometry(QtCore.QRect(0, 0, 361, 397))
        self.page_3.setObjectName("page_3")
        self.addStaffMemberButton = QtWidgets.QPushButton(self.page_3)
        self.addStaffMemberButton.setGeometry(QtCore.QRect(30, 10, 291, 31))
        self.addStaffMemberButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                                "selection-background-color: rgb(255, 255, 0);"
                                                "background-color: qconicalgradient(cx:0, cy:0,"
                                                " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                                " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                                " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                                " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                                "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                                " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.deleteStaffMemberButton = QtWidgets.QPushButton(self.page_3)
        self.deleteStaffMemberButton.setGeometry(QtCore.QRect(30, 60, 291, 31))
        self.deleteStaffMemberButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                                   "selection-background-color: rgb(255, 255, 0);"
                                                   "background-color: qconicalgradient(cx:0, cy:0,"
                                                   " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                                   " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                                   " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                                   " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                                   "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                                   " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.searchStaffMemberButton = QtWidgets.QPushButton(self.page_3)
        self.searchStaffMemberButton.setGeometry(QtCore.QRect(30, 110, 291, 31))
        self.searchStaffMemberButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                                   "selection-background-color: rgb(255, 255, 0);"
                                                   "background-color: qconicalgradient(cx:0, cy:0,"
                                                   " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                                   " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                                   " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                                   " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                                   "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                                   " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.updateStaffMemberButton = QtWidgets.QPushButton(self.page_3)
        self.updateStaffMemberButton.setGeometry(QtCore.QRect(30, 160, 291, 31))
        self.updateStaffMemberButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                                   "selection-background-color: rgb(255, 255, 0);"
                                                   "background-color: qconicalgradient(cx:0, cy:0,"
                                                   " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                                   " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                                   " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                                   " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                                   "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                                   " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.updateStaffMemberButton.setObjectName("updateStaffMemberButton")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget(self)
        self.page_4.setObjectName("page_4")
        self.addExpenseButton = QtWidgets.QPushButton(self.page_4)
        self.addExpenseButton.setGeometry(QtCore.QRect(30, 10, 291, 31))
        self.addExpenseButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "selection-background-color: rgb(255, 255, 0);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.paySalaryButton = QtWidgets.QPushButton(self.page_4)
        self.paySalaryButton.setGeometry(QtCore.QRect(30, 60, 291, 31))
        self.paySalaryButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                           "selection-background-color: rgb(255, 255, 0);"
                                           "background-color: qconicalgradient(cx:0, cy:0,"
                                           " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                           " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                           " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                           " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                           "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                           " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.feesPaidButton = QtWidgets.QPushButton(self.page_4)
        self.feesPaidButton.setGeometry(QtCore.QRect(30, 110, 291, 31))
        self.feesPaidButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                          "background-color: qconicalgradient(cx:0, cy:0,"
                                          " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                          " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                          " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                          " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                          "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), "
                                          "stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.printBillButton = QtWidgets.QPushButton(self.page_4)
        self.printBillButton.setGeometry(QtCore.QRect(30, 160, 291, 31))
        self.printBillButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                           "selection-background-color: rgb(255, 255, 0);"
                                           "background-color: qconicalgradient(cx:0, cy:0,"
                                           " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                           " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                           " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                           " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                           "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                           " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget(self)
        self.page_5.setObjectName("page_4")
        self.addCourseButton = QtWidgets.QPushButton(self.page_5)
        self.addCourseButton.setGeometry(QtCore.QRect(30, 10, 291, 31))
        self.addCourseButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                           "selection-background-color: rgb(255, 255, 0);"
                                           "background-color: qconicalgradient(cx:0, cy:0,"
                                           " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                           " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                           " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                           " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                           "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                           " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.viewCourseButton = QtWidgets.QPushButton(self.page_5)
        self.viewCourseButton.setGeometry(QtCore.QRect(30, 60, 291, 31))
        self.viewCourseButton.setStyleSheet("background-color: rgb(255, 255, 127);"
                                            "selection-background-color: rgb(255, 255, 0);"
                                            "background-color: qconicalgradient(cx:0, cy:0,"
                                            " angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375"
                                            " rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0,"
                                            " 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255,"
                                            " 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 "
                                            "rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625"
                                            " rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.toolBox.addItem(self.page_5, "")
        self.frame = QtWidgets.QFrame()
        self.frame.setGeometry(QtCore.QRect(10, 10, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.retranslateUi(self)
        # self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scholastic Administration"))
        self.addStudentButton.setText(_translate("MainWindow", "Add Student"))
        self.deleteStudentButton.setText(_translate("MainWindow", "Delete Student"))
        self.updateStudentButton.setText(_translate("MainWindow", "Update Details"))
        self.logout.setText(_translate("MainWindow", "logout"))
        self.searchStudentButton.setText(_translate("MainWindow", "Search Student"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Manage Student"))
        self.issueBookButton.setText(_translate("MainWindow", "Issue Book"))
        self.returnBookButton.setText(_translate("MainWindow", "Return Book"))
        self.checkBookAvailabilityButton.setText(_translate("MainWindow", "Check Availability"))
        self.addBookButton.setText(_translate("MainWindow", "Add Book"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Manage Library"))
        self.addStaffMemberButton.setText(_translate("MainWindow", "Add Staff Member"))
        self.deleteStaffMemberButton.setText(_translate("MainWindow", "Delete Staff Member"))
        self.searchStaffMemberButton.setText(_translate("MainWindow", "Search Member"))
        self.updateStaffMemberButton.setText(_translate("MainWindow", "Update Details"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Manage Staff"))
        self.addExpenseButton.setText(_translate("MainWindow", "Add Expense"))
        self.paySalaryButton.setText(_translate("MainWindow", "Pay Salary"))
        self.feesPaidButton.setText(_translate("MainWindow", "Deposite Fee"))
        self.printBillButton.setText(_translate("MainWindow", "View & Print Expenses"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Manage Accounts"))
        self.addCourseButton.setText(_translate("MainWindow", "Add Course"))
        self.viewCourseButton.setText(_translate("MainWindow", "View Courses"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("MainWindow", "Manage Courses"))

class LoginPage(QWidget):
    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(391, 459)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 391, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.background = QtWidgets.QLabel(self.frame)
        self.background.setGeometry(QtCore.QRect(-10, 0, 401, 461))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(".\\login.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("label")
        self.userid = QtWidgets.QLabel(self.frame)
        self.userid.setGeometry(QtCore.QRect(80, 150, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userid.setFont(font)
        self.userid.setStyleSheet("color: rgb(255, 255, 255);")
        self.userid.setObjectName("label_2")
        self.password = QtWidgets.QLabel(self.frame)
        self.password.setGeometry(QtCore.QRect(80, 220, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setStyleSheet("color: rgb(255, 255, 255);")
        self.password.setObjectName("label_3")
        self.enteruserid = QtWidgets.QLineEdit(self.frame)
        self.enteruserid.setGeometry(QtCore.QRect(80, 180, 211, 20))
        self.enteruserid.setObjectName("lineEdit")
        self.enterpass = QtWidgets.QLineEdit(self.frame)
        self.enterpass.setEchoMode(QLineEdit.Password)
        self.enterpass.setGeometry(QtCore.QRect(80, 250, 211, 20))
        self.enterpass.setObjectName("lineEdit_2")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(150, 300, 75, 23))
        self.loginButton.setObjectName("pushButton")
        self.login = QtWidgets.QLabel(self.frame)
        self.login.setGeometry(QtCore.QRect(160, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.login.setFont(font)
        self.login.setStyleSheet("color: rgb(255, 255, 255);")
        self.login.setObjectName("label_4")

        self.retranslateUi(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Scholastic Administration"))
        self.userid.setText(_translate("Form", "User ID:"))
        self.password.setText(_translate("Form", "Password:"))
        self.loginButton.setText(_translate("Form", "Log in"))
        self.login.setText(_translate("Form", "Login"))

    def loginto(self):
        matchlogin = Login(self.enteruserid.text(),self.enterpass.text())
        i = matchlogin.checklogindetails()
        return i

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scholastic Administration")
        self.setWindowIcon(QtGui.QIcon(".\\icon.png"))
        self.loginpage = LoginPage(self)
        self.loginpage.show()
        self.mainPage = MainPage(self)
        self.mainPage.hide()

        #Student Management

        self.searchforupdate = SearchforUpdatePage(self)
        self.searchforupdate.hide()
        self.updatestudent = updateStudentPage(self)
        self.updatestudent.hide()
        self.searchstudent = SearchStudentPage(self)
        self.searchstudent.hide()
        self.searchedstudent = StudentSearchedPage(self)
        self.searchedstudent.hide()
        self.searchfordelete = SearchforDeletePage(self)
        self.searchfordelete.hide()
        self.deletestudent = deleteStudentPage(self)
        self.deletestudent.hide()
        self.addstudent = AddStudentInfoPage(self)
        self.addstudent.hide()

        # Library Management

        self.issuebook = issueBookPage(self)
        self.issuebook.hide()
        self.returnbook = returnBookPage(self)
        self.returnbook.hide()
        self.checkavailability = SearchforAvailabilityPage(self)
        self.checkavailability.hide()
        self.availablebook = AvailableBookPage(self)
        self.availablebook.hide()
        self.addbook = AddBookPage(self)
        self.addbook.hide()

        # Staff Management
        self.addstaff = AddStaffPage(self)
        self.addstaff.hide()
        self.searchfordeletestaff = SearchforDeleteStaffPage(self)
        self.searchfordeletestaff.hide()
        self.deletestaff = deleteStaffPage(self)
        self.deletestaff.hide()
        self.searchforupdatestaff = SearchforUpdateStaffPage(self)
        self.searchforupdatestaff.hide()
        self.updatestaff = updateStaffPage(self)
        self.updatestaff.hide()
        self.searchstaff = SearchStaffPage(self)
        self.searchstaff.hide()
        self.searchedstaff = StaffSearchedPage(self)
        self.searchedstaff.hide()

        # Expense Management
        self.paysalary = PaySalaryPage(self)
        self.paysalary.hide()
        self.addexpense = AddExpensePage(self)
        self.addexpense.hide()
        self.viewexpense = ViewExpensePage(self)
        self.viewexpense.hide()
        self.feespaid = feesPaidPage(self)
        self.feespaid.hide()
        self.showexpense = ShowExpensePage(self)
        self.showexpense.hide()

        # Course Management
        self.addcourse = AddCoursePage(self)
        self.addcourse.hide()
        self.viewcourse = ViewCoursePage(self)
        self.viewcourse.hide()

        # login button signal and slots
        self.loginpage.loginButton.clicked.connect(self.login)
        self.loginpage.enterpass.returnPressed.connect(self.login)

        #main page signal and slots
        self.mainPage.logout.clicked.connect(self.logout)
        self.mainPage.addStudentButton.clicked.connect(self.addStudent)
        self.mainPage.updateStudentButton.clicked.connect(self.searchForUpdate)
        self.mainPage.searchStudentButton.clicked.connect(self.searchStudent)
        self.mainPage.deleteStudentButton.clicked.connect(self.searchForDelete)
        self.mainPage.issueBookButton.clicked.connect(self.issueBook)
        self.mainPage.returnBookButton.clicked.connect(self.returnBook)
        self.mainPage.checkBookAvailabilityButton.clicked.connect(self.checkAvailability)
        self.mainPage.addBookButton.clicked.connect(self.addBook)
        self.mainPage.addStaffMemberButton.clicked.connect(self.addStaff)
        self.mainPage.deleteStaffMemberButton.clicked.connect(self.searchForDeleteStaff)
        self.mainPage.updateStaffMemberButton.clicked.connect(self.searchForUpdateStaff)
        self.mainPage.searchStaffMemberButton.clicked.connect(self.searchStaff)
        self.mainPage.paySalaryButton.clicked.connect(self.paySalary)
        self.mainPage.addExpenseButton.clicked.connect(self.addExpense)
        self.mainPage.feesPaidButton.clicked.connect(self.feesPay)
        self.mainPage.printBillButton.clicked.connect(self.viewExpense)
        self.mainPage.addCourseButton.clicked.connect(self.addCourse)
        self.mainPage.viewCourseButton.clicked.connect(self.viewCourse)

        # Student Management signal and slots
        self.addstudent.submitButton.clicked.connect(self.insertStudentDataIntoDb)
        self.searchfordelete.searchButton.clicked.connect(self.deleteStudent)
        self.searchforupdate.searchButton.clicked.connect(self.updateStudent)
        self.searchstudent.searchButton.clicked.connect(self.searchedStudent)
        self.updatestudent.cancelButton.clicked.connect(self.searchForUpdate)
        self.updatestudent.submitButton.clicked.connect(self.updateStudentData)
        self.searchedstudent.backButton.clicked.connect(self.searchStudent)
        self.searchfordelete.searchButton.clicked.connect(self.deleteStudent)
        self.deletestudent.backButton.clicked.connect(self.searchForDelete)
        self.deletestudent.deleteButton.clicked.connect(self.deleteStudentData)
        self.searchstudent.enternoofrec.currentIndexChanged.connect(self.searchstudent.showrollno)

        # Library Management signal and slots
        self.checkavailability.searchButton.clicked.connect(self.availableBook)
        self.availablebook.backButton.clicked.connect(self.checkAvailability)
        self.addbook.submitButton.clicked.connect(self.addbookintodb)
        self.issuebook.issueButton.clicked.connect(self.issueindb)
        self.returnbook.returnButton.clicked.connect(self.returnintodb)
        self.checkavailability.searchButton.clicked.connect(self.checkavailableindb)
        self.checkavailability.entershowbook.currentIndexChanged.connect(self.checkavailability.showWidget)

        # Staff Management signal and slots
        self.searchfordeletestaff.searchButton.clicked.connect(self.deleteStaff)
        self.deletestaff.deleteButton.clicked.connect(self.deleteStaffData)
        self.updatestaff.submitButton.clicked.connect(self.updateStaffData)
        self.addstaff.submitButton.clicked.connect(self.insertStaffDataIntoDb)
        self.deletestaff.backButton.clicked.connect(self.searchForDeleteStaff)
        self.searchforupdatestaff.searchButton.clicked.connect(self.updateStaff)
        self.searchstaff.searchButton.clicked.connect(self.searchedStaff)
        self.updatestaff.cancelButton.clicked.connect(self.searchForUpdateStaff)
        self.searchedstaff.backButton.clicked.connect(self.searchStaff)
        self.searchstaff.enternoofrec.currentIndexChanged.connect(self.searchstaff.showstaffid)

        # Expense Management signal and slots
        self.addexpense.submitButton.clicked.connect(self.insertExpenseIntoDB)
        self.paysalary.submitButton.clicked.connect(self.insertSalaryIntoDB)
        self.feespaid.submitButton.clicked.connect(self.feesintodb)
        self.viewexpense.submitButton.clicked.connect(self.showExpense)
        self.showexpense.printButton.clicked.connect(self.showexpense.printpreviewdialog)
        self.showexpense.backButton.clicked.connect(self.viewExpense)

        # Course management signal and slots
        self.addcourse.submitButton.clicked.connect(self.addCourseIntoDb)


        self.show()


    def allHide(self):
        self.mainPage.background.hide()
        self.addstudent.hide()
        self.searchforupdate.hide()
        self.searchfordelete.hide()
        self.deletestudent.hide()
        self.updatestudent.hide()
        self.searchedstudent.hide()
        self.searchstudent.hide()
        self.feespaid.hide()
        self.loginpage.hide()
        self.issuebook.hide()
        self.returnbook.hide()
        self.checkavailability.hide()
        self.availablebook.hide()
        self.addbook.hide()
        self.addstaff.hide()
        self.searchfordeletestaff.hide()
        self.deletestaff.hide()
        self.searchforupdatestaff.hide()
        self.searchstaff.hide()
        self.searchedstaff.hide()
        self.updatestaff.hide()
        self.paysalary.hide()
        self.addexpense.hide()
        self.viewexpense.hide()
        self.showexpense.hide()
        self.addcourse.hide()
        self.viewcourse.hide()

    # Login Functions
    def login(self):
        if self.loginpage.loginto():
            self.setGeometry(100,100,1200, 600)
            self.mainPage.show()
            self.mainPage.background.show()
            self.setFixedSize(1200, 600)
        else:
            QMessageBox.about(self, "info", "Username/Password you entered is incorrect")

    def logout(self):
        self.setFixedSize(391,459)
        self.allHide()
        self.loginpage.enteruserid.setText("")
        self.loginpage.enterpass.setText("")
        self.mainPage.hide()
        self.loginpage.show()

    # Student Management Functions

    def addStudent(self):
        self.allHide()
        self.addstudent.show()
        self.addinto2 = insertStudentDsts()
        self.addstudent.updateCoursesInList()
        self.addinto2.show_rno(self.addstudent)

    def insertStudentDataIntoDb(self):
        self.addinto = insertStudentDsts()
        if self.addinto.insert(self.addstudent):
            QMessageBox.about(self,"Info","Student Data Added")
        else:
            QMessageBox.about(self,"Info","Could not add data")
        self.addstudent.retranslateUi()

    def searchForUpdate(self):
        self.allHide()
        self.searchforupdate.enterrollno.setText('')
        self.searchforupdate.show()
        self.updatestudent.retranslateUi()

    def searchForDelete(self):
        self.allHide()
        self.searchfordelete.enterrollno.setText('')
        self.searchfordelete.show()
        self.deletestudent.retranslateUi()

    def updateStudent(self):
        if self.searchforupdate.searchrollno(self.updatestudent):
            self.allHide()
            self.updatestudent.show()
        else:
            QMessageBox.about(self,'Info','Something went wrong')

    def updateStudentData(self):
        if self.updatestudent.updateStudentDataIntoDb():
            QMessageBox.about(self,"Info","Student Data Updated")
        else:
            QMessageBox.about(self,"Info","Could not update data")
        #self.addstudent.retranslateUi()

    def searchStudent(self):
        self.allHide()
        self.searchstudent.enterrollno.setText('')
        self.searchstudent.show()
        self.searchedstudent.retranslateUi()

    def searchedStudent(self):
        if self.searchstudent.searchrollno(self.searchedstudent):
            self.allHide()
            self.searchedstudent.show()
            pass
        else:
            QMessageBox.about(self,'Info','Something went wrong')
        self.searchstudent.retranslateUi()

    def deleteStudent(self):
        if self.searchfordelete.searchrollno(self.deletestudent):
            self.allHide()
            self.deletestudent.show()
        else:
            QMessageBox.about(self,"Info","Something went wrong")

    def deleteStudentData(self):
        if self.deletestudent.DeleteStudentData():
            QMessageBox.about(self,'Info','Student Data Deleted')
        else:
            QMessageBox.about(self,'Info','Could not delete data')
        self.deletestudent.retranslateUi()

    # Library Management funtions

    def issueBook(self):
        self.allHide()
        self.issuebook.show()

    def issueindb(self):
        if self.issuebook.issuebookintodb()== 1:
            QMessageBox.about(self,"Info","Book Issued")
        elif self.issuebook.issuebookintodb() == 3:
            QMessageBox.about(self,"Info","Student already has a book issued")
        else:
            QMessageBox.about(self, "Info", "Something went wrong in entering values")
        self.issuebook.retranslateUi()

    def returnBook(self):
        self.allHide()
        self.returnbook.show()

    def returnintodb(self):
        if self.returnbook.returnbooktodb() == 1:
            QMessageBox.about(self,"Info", "Book Returned")
        elif self.returnbook.returnbooktodb() == 2:
            QMessageBox.about(self,"Info","Book returned is not correct")
        else:
            QMessageBox.about(self, "Info", "Something went wrong in entering values")
        self.returnbook.retranslateUi()

    def checkAvailability(self):
        self.allHide()
        self.checkavailability.show()
        self.checkavailability.retranslateUi()

    def checkavailableindb(self):
        count = self.checkavailability.chechavailability()
        bookname = self.checkavailability.enterbookname.text()
        num = self.checkavailability.entershowbook.currentText()
        self.availablebook.showavailability(bookname,count,num)

    def availableBook(self):
        self.allHide()
        self.checkavailability.widget.hide()
        self.availablebook.show()

    def addBook(self):
        self.allHide()
        self.addbook.show()

    def addbookintodb(self):
        if self.addbook.addbookintodb():
            QMessageBox.about(self,"Info","Book Added")
        else:
            QMessageBox.about(self,"Info","Could not complete task")
        self.addbook.retranslateUi()

    # Staff Management Functions

    def addStaff(self):
        self.allHide()
        self.addstaff.show()
        self.addstaff.show_sid()

    def insertStaffDataIntoDb(self):
        if self.addstaff.insert():
            QMessageBox.about(self,"Info","Staff Data Added")
        else:
            QMessageBox.about(self,"Info","Could not add data")
        self.addstaff.retranslateUi()

    def searchForDeleteStaff(self):
        self.allHide()
        #self.searchfordeletestaff.enterstaffid.setText('')
        self.searchfordeletestaff.show()

    def deleteStaff(self):
        if self.searchfordeletestaff.searchstaffid(self.deletestaff):
            self.allHide()
            self.deletestaff.show()
        else:
            QMessageBox.about(self,'Info',"Something went wrong in entering values")

    def searchForUpdateStaff(self):
        self.searchforupdatestaff.enterstaffid.setText('')
        self.allHide()
        self.searchforupdatestaff.show()

    def updateStaff(self):
        if self.searchforupdatestaff.searchstaffid(self.updatestaff):
            self.allHide()
            self.updatestaff.show()
        else:
            QMessageBox.about(self,'Info',"Something went wrong in entering values")


    def searchStaff(self):
        self.allHide()
        self.searchstaff.enterstaffid.setText('')
        self.searchstaff.show()
        self.searchedstaff.retranslateUi()

    def searchedStaff(self):
        if self.searchstaff.searchstaffid(self.searchedstaff):
            self.allHide()
            self.searchstaff.widget.hide()
            self.searchedstaff.show()
        else:
            QMessageBox.about(self,'info','Something went wrong in entering values')

    def updateStaffData(self):
        if self.updatestaff.updateStaffDataIntoDb():
            QMessageBox.about(self,"Info","Staff Data Updated")
        else:
            QMessageBox.about(self,"Info","Could not update data")

    def deleteStaffData(self):
        if self.deletestaff.DeleteStaffData():
            QMessageBox.about(self,'Info','Staff Data Deleted')
        else:
            QMessageBox.about(self,'Info','Could not delete data')
        self.deletestaff.retranslateUi()

    # Expense Management Functions

    def paySalary(self):
        self.allHide()
        self.paysalary.show()

    def addExpense(self):
        self.allHide()
        self.addexpense.show()

    def insertExpenseIntoDB(self):
        if self.addexpense.insertintodb():
            QMessageBox.about(self,"Info","Expense Added")
        else:
            QMessageBox.about(self,"Info","Something went wrong in entering values")
        self.addexpense.retranslateUi()

    def insertSalaryIntoDB(self):
        if self.paysalary.paysalaryintodb():
            QMessageBox.about(self,"Info","Expense Added")
        else:
            QMessageBox.about(self,"Info","Something went wrong in entering values")
        self.paysalary.retranslateUi()

    def feesPay(self):
        self.allHide()
        self.feespaid.show()

    def feesintodb(self):
        if self.feespaid.studentFeesIntoDb():
            QMessageBox.about(self,"Info","Fees deposited")
        else:
            QMessageBox.about(self,"Info","Something went wrong in entering values")
        self.feespaid.retranslateUi()

    def viewExpense(self):
        self.allHide()
        self.viewexpense.show()
        self.showexpense.retranslateUi()

    def showExpense(self):
        self.allHide()
        self.showexpense.show()
        data = self.viewexpense.getdatafromdb()
        self.showexpense.showData(data)

    # Course management functions

    def addCourse(self):
        self.allHide()
        self.addcourse.showcourseid()
        self.addcourse.show()

    def addCourseIntoDb(self):
        if self.addcourse.addcourseintodb(self.addstudent,self.updatestudent):
            QMessageBox.about(self,"Info","Course Added")
        else:
            QMessageBox.about(self,"Info","Something went wrong in entering values")
        self.addcourse.retranslateUi()
        self.addcourse.showcourseid()

    def viewCourse(self):
        self.allHide()
        self.viewcourse.showavailablecourses()
        self.viewcourse.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())