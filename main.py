import csv
import sys
import platform
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QTableWidgetItem

from PyGUI.RBAC import RBACClass

# GUI FILE
from PyGUI.ui_login import Ui_Form
from PyGUI.ui_patient_id import Ui_MainWindow

GLOBAL_STATE = 0


# IMPORT FUNCTIONS
# from PyGUI.ui_functions import *


class MainWindow(QtWidgets.QMainWindow):
    role_value = None
    DATA_PATH = 'D:\\SASTRA\Code\\Dean Mam Project\\assignment\\Data\\Medical_Records.csv'

    def __init__(self):
        print('Main init')
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        for i in RBACClass.permission_dict['Administrator']:
            self.ui.tableWidget.setColumnHidden(i, True)

        ## ==> MAXIMIZE RESTORE FUNCTION
        def maximize_restore():
            global GLOBAL_STATE
            status = GLOBAL_STATE

            # IF NOT MAXIMIZED
            if status == 0:
                self.showMaximized()

                # SET GLOBAL TO 1
                GLOBAL_STATE = 1

                # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
                self.ui.drop_shadow_frame.setContentsMargins(0, 0, 0, 0)
                self.ui.drop_shadow_frame.setStyleSheet(
                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
                self.ui.maximize_btn.setToolTip("Restore")
            else:
                GLOBAL_STATE = 0
                self.showNormal()
                self.resize(self.width() + 1, self.height() + 1)
                self.ui.drop_shadow_frame.setContentsMargins(10, 10, 10, 10)
                self.ui.drop_shadow_frame.setStyleSheet(
                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
                self.ui.maximize_btn.setToolTip("Maximize")

        ## ==> UI DEFINITIONS
        def uiDefinitions():

            # REMOVE TITLE BAR
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # SET DROPSHADOW WINDOW
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 100))

            # APPLY DROPSHADOW TO FRAME
            self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

            # MAXIMIZE / RESTORE
            self.ui.maximize_btn.clicked.connect(lambda: maximize_restore())

            # MINIMIZE
            self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())

            # CLOSE
            self.ui.close_btn.clicked.connect(lambda: self.close())

            ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
            self.sizegrip = QSizeGrip(self.ui.frame_grip)
            self.sizegrip.setStyleSheet(
                "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
            self.sizegrip.setToolTip("Resize Window")

        def rolePermission(role):
            for i in role:
                self.ui.tableWidget.setColumnHidden(i, False)

        # MOVE WINDOW
        def moveWindowMain(event):
            # RESTORE BEFORE MOVE
            if self.returnStatus() == 1:
                self.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        def view_details():
            patient_id = self.ui.patientIdLineEdit_2.text()
            print(patient_id)
            self.ui.stackedWidget.setCurrentIndex(1)
            with open(MainWindow.DATA_PATH, 'r') as datafile:
                print('inside file')
                readData = csv.reader(datafile)
                rowValue = 0
                for row in readData:
                    print('inside row')
                    if row[1] == patient_id:
                        self.ui.tableWidget.insertRow(rowValue)
                        print(row[1], type(row[1]))
                        for i in MainWindow.role_value:
                            print('set')
                            self.ui.tableWidget.setItem(rowValue, i, QTableWidgetItem(row[i]))
                        rowValue = rowValue+1
        def go_back():
            self.ui.stackedWidget.setCurrentIndex(0)

        ## ==> SET UI DEFINITIONS
        uiDefinitions()

        print(MainWindow.role_value, "rolePerm")
        rolePermission(MainWindow.role_value)

        self.ui.viewDetailsPushButton_2.clicked.connect(view_details)
        self.ui.back_btn.clicked.connect(go_back)

        # SET TITLE BAR
        self.ui.title_bar_2.mouseMoveEvent = moveWindowMain

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus(self):
        return GLOBAL_STATE

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        def uiDefinition():
            # REMOVE TITLE BAR
            self.shadow = QGraphicsDropShadowEffect(self)
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # SET DROPSHADOW WINDOW
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 100))

            # APPLY DROPSHADOW TO FRAME
            self.ui.login_frame.setGraphicsEffect(self.shadow)

            # CLOSE
            self.ui.closePushButton.clicked.connect(lambda: self.close())

        # MOVE WINDOW
        def moveWindowLogin(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton():
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        def show_new_window():
            print(self.ui.userNameLineEdit.text(), self.ui.passwordLineEdit.text())
            r = RBACClass()
            MainWindow.role_value = r.logon(UserName=self.ui.userNameLineEdit.text(),
                                            Password=self.ui.passwordLineEdit.text())
            print(MainWindow.role_value, "show")
            if MainWindow.role_value != None:
                print('here')
                self.close()
                w = MainWindow()
                w.show()
            else:
                print('no')
                self.ui.userNameLineEdit.setPlaceholderText('Try Again')
                self.ui.passwordLineEdit.setPlaceholderText('Try Again')

        # SET TITLE BAR
        self.ui.login_frame.mouseMoveEvent = moveWindowLogin
        self.ui.loginPushButton.clicked.connect(show_new_window)

        ## ==> SET UI DEFINITIONS
        uiDefinition()

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
