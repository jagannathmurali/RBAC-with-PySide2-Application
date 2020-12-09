# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loginxDyLgG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(524, 634)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(524, 634))
        Form.setMaximumSize(QSize(524, 634))
        Form.setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(Form)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(35, 37, 38, 1), stop:1 rgba(65, 67, 69, 1));\n"
"")
        self.login_frame.setFrameShape(QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.login_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 80, 211, 61))
        font = QFont()
        font.setFamily(u"Montserrat Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 87 16pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,114,160,1), stop:1 rgba(0,212,255,1));\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.login_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 120, 321, 61))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font: 87 16pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,114,160,1), stop:1 rgba(0,212,255,1));\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.userNameLineEdit = QLineEdit(self.login_frame)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")
        self.userNameLineEdit.setGeometry(QRect(120, 240, 281, 41))
        self.userNameLineEdit.setMinimumSize(QSize(281, 41))
        self.userNameLineEdit.setMaximumSize(QSize(281, 41))
        self.userNameLineEdit.setStyleSheet(u"QLineEdit{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	border: 2px solid rgb(131, 133, 135);\n"
"	border-radius: 20px;\n"
"	color: #2a2b2d;\n"
"	background-color: rgb(131, 133, 135);\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgba(0,212,255,1);\n"
"	background-color: rgb(157, 159, 162);\n"
"}")
        self.userNameLineEdit.setAlignment(Qt.AlignCenter)
        self.passwordLineEdit = QLineEdit(self.login_frame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(120, 310, 281, 41))
        self.passwordLineEdit.setMinimumSize(QSize(281, 41))
        self.passwordLineEdit.setMaximumSize(QSize(281, 41))
        self.passwordLineEdit.setStyleSheet(u"QLineEdit{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	border: 2px solid rgb(131, 133, 135);\n"
"	border-radius: 20px;\n"
"	color: #2a2b2d;\n"
"	background-color: rgb(131, 133, 135);\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgba(0,212,255,1);\n"
"}")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setAlignment(Qt.AlignCenter)
        self.loginPushButton = QPushButton(self.login_frame)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(120, 380, 120, 41))
        self.loginPushButton.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	border: 2px solid rgb(131, 133, 135);\n"
"	border-radius: 20px;\n"
"	color: #2a2b2d;\n"
"	background-color: rgb(131, 133, 135);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: #FFF;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,114,160,1), stop:1 rgba(0,212,255,1));\n"
"}\n"
"")
        self.label_3 = QLabel(self.login_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 520, 161, 61))
        font1 = QFont()
        font1.setFamily(u"Montserrat Black")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(10)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: rgb(131, 133, 135);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.closePushButton = QPushButton(self.login_frame)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setGeometry(QRect(280, 380, 120, 41))
        self.closePushButton.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	border: 2px solid rgb(131, 133, 135);\n"
"	border-radius: 20px;\n"
"	color: #2a2b2d;\n"
"	background-color: rgb(131, 133, 135);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: #FFF;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,114,160,1), stop:1 rgba(0,212,255,1));\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.login_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"WELCOME TO", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"MEDICAL DATABASE", None))
        self.userNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.loginPushButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Created By Jagannath", None))
        self.closePushButton.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

