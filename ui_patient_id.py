# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_patient_idBKiYIY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.532338 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title_bar_2 = QFrame(self.drop_shadow_frame)
        self.title_bar_2.setObjectName(u"title_bar_2")
        self.title_bar_2.setMaximumSize(QSize(16777215, 40))
        self.title_bar_2.setStyleSheet(u"background-color: none;")
        self.title_bar_2.setFrameShape(QFrame.StyledPanel)
        self.title_bar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(11, 0, 11, 0)
        self.frame_3 = QFrame(self.title_bar_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 87 14pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color:#FFF;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")

        self.horizontalLayout_7.addWidget(self.label)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.window_btns = QFrame(self.title_bar_2)
        self.window_btns.setObjectName(u"window_btns")
        self.window_btns.setMaximumSize(QSize(80, 16777215))
        self.window_btns.setFrameShape(QFrame.StyledPanel)
        self.window_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.window_btns)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.minimize_btn = QPushButton(self.window_btns)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	border:0px solid;\n"
"	background-color: rgb(85, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(68, 204, 0);\n"
"}")

        self.horizontalLayout_6.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.window_btns)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setStyleSheet(u"QPushButton{\n"
"	border:0px solid;\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(214, 214, 0);\n"
"}")

        self.horizontalLayout_6.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.window_btns)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"	border:0px solid;\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(199, 0, 0);\n"
"}")

        self.horizontalLayout_6.addWidget(self.close_btn)


        self.horizontalLayout_5.addWidget(self.window_btns)


        self.verticalLayout_6.addWidget(self.title_bar_2)

        self.content_bar_2 = QFrame(self.drop_shadow_frame)
        self.content_bar_2.setObjectName(u"content_bar_2")
        self.content_bar_2.setFrameShape(QFrame.StyledPanel)
        self.content_bar_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.content_bar_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.stackedWidget = QStackedWidget(self.content_bar_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.patient_id_page = QWidget()
        self.patient_id_page.setObjectName(u"patient_id_page")
        self.horizontalLayout = QHBoxLayout(self.patient_id_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.patient_id_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: none;\n"
"border: 2px solid  rgb(173, 125, 255);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 100))
        self.frame_16.setMaximumSize(QSize(16777215, 100))
        self.frame_16.setStyleSheet(u"border: 0px solid;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 100))
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setStyleSheet(u"border: 0px solid;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 10))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(100, 0))
        self.frame_19.setMaximumSize(QSize(100, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_21)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_3.setLabelAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.formLayout_3.setFormAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(150, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_22)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 16777215))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	font: 87 10pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: #FFF;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_4)


        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.frame_22)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 50))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.patientIdLineEdit_2 = QLineEdit(self.frame_24)
        self.patientIdLineEdit_2.setObjectName(u"patientIdLineEdit_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patientIdLineEdit_2.sizePolicy().hasHeightForWidth())
        self.patientIdLineEdit_2.setSizePolicy(sizePolicy)
        self.patientIdLineEdit_2.setMinimumSize(QSize(1, 35))
        self.patientIdLineEdit_2.setMaximumSize(QSize(281, 35))
        self.patientIdLineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	border: 2px solid rgb(98, 103, 255);\n"
"	border-radius: 10px;\n"
"	color: #2a2b2d;\n"
"	background-color: #FFF;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgba(0,212,255,1);\n"
"	background-color: rgb(157, 159, 162);\n"
"}")
        self.patientIdLineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.patientIdLineEdit_2)


        self.horizontalLayout_15.addWidget(self.frame_24)


        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.frame_23)


        self.verticalLayout_2.addWidget(self.frame_21)

        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_25)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setLabelAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_4.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.viewDetailsPushButton_2 = QPushButton(self.frame_25)
        self.viewDetailsPushButton_2.setObjectName(u"viewDetailsPushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewDetailsPushButton_2.sizePolicy().hasHeightForWidth())
        self.viewDetailsPushButton_2.setSizePolicy(sizePolicy1)
        self.viewDetailsPushButton_2.setMinimumSize(QSize(125, 30))
        self.viewDetailsPushButton_2.setMaximumSize(QSize(125, 30))
        self.viewDetailsPushButton_2.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	border: 2px solid rgb(131, 133, 135);\n"
"	border-radius: 15px;\n"
"	color: #2a2b2d;\n"
"	background-color: rgb(131, 133, 135);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: #FFF;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,114,160,1), stop:1 rgba(0,212,255,1));\n"
"}\n"
"")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.viewDetailsPushButton_2)


        self.verticalLayout_2.addWidget(self.frame_25)


        self.horizontalLayout_13.addWidget(self.frame_20)

        self.frame_26 = QFrame(self.frame_18)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(100, 0))
        self.frame_26.setMaximumSize(QSize(100, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_26)


        self.horizontalLayout_12.addWidget(self.frame_18)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_27 = QFrame(self.frame_2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 100))
        self.frame_27.setMaximumSize(QSize(16777215, 100))
        self.frame_27.setStyleSheet(u"border:0px solid;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_27)


        self.horizontalLayout_17.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.patient_id_page)
        self.patient_details_page = QWidget()
        self.patient_details_page.setObjectName(u"patient_details_page")
        self.horizontalLayout_18 = QHBoxLayout(self.patient_details_page)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.patient_details_page)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(self.frame_28)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: none;\n"
"border: 2px solid  rgb(173, 125, 255);\n"
"border-radius: 10px;")
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.main)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.patient_details = QFrame(self.main)
        self.patient_details.setObjectName(u"patient_details")
        self.patient_details.setMinimumSize(QSize(0, 100))
        self.patient_details.setMaximumSize(QSize(16777215, 100))
        self.patient_details.setStyleSheet(u"border: 0px solid;")
        self.patient_details.setFrameShape(QFrame.StyledPanel)
        self.patient_details.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.patient_details)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.left_side = QFrame(self.patient_details)
        self.left_side.setObjectName(u"left_side")
        self.left_side.setFrameShape(QFrame.StyledPanel)
        self.left_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.patient_name = QFrame(self.left_side)
        self.patient_name.setObjectName(u"patient_name")
        self.patient_name.setFrameShape(QFrame.StyledPanel)
        self.patient_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.patient_name)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.patient_name)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(150, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.patientLabel = QLabel(self.frame_29)
        self.patientLabel.setObjectName(u"patientLabel")
        self.patientLabel.setMaximumSize(QSize(150, 16777215))
        self.patientLabel.setStyleSheet(u"QLabel{\n"
"	font: 87 10pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: #FFF;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.patientLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.patientLabel)


        self.horizontalLayout_20.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.patient_name)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 50))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.patientLineEdit = QLineEdit(self.frame_31)
        self.patientLineEdit.setObjectName(u"patientLineEdit")
        sizePolicy.setHeightForWidth(self.patientLineEdit.sizePolicy().hasHeightForWidth())
        self.patientLineEdit.setSizePolicy(sizePolicy)
        self.patientLineEdit.setMinimumSize(QSize(1, 35))
        self.patientLineEdit.setMaximumSize(QSize(281, 35))
        self.patientLineEdit.setStyleSheet(u"QLineEdit{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	border: 2px solid rgb(98, 103, 255);\n"
"	border-radius: 10px;\n"
"	color: #2a2b2d;\n"
"	background-color: #FFF;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"")
        self.patientLineEdit.setAlignment(Qt.AlignCenter)
        self.patientLineEdit.setDragEnabled(True)
        self.patientLineEdit.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.patientLineEdit)


        self.horizontalLayout_22.addWidget(self.frame_31)


        self.horizontalLayout_20.addWidget(self.frame_30)


        self.verticalLayout_3.addWidget(self.patient_name)

        self.gender = QFrame(self.left_side)
        self.gender.setObjectName(u"gender")
        self.gender.setFrameShape(QFrame.StyledPanel)
        self.gender.setFrameShadow(QFrame.Raised)
        self.gender_line_edit = QFrame(self.gender)
        self.gender_line_edit.setObjectName(u"gender_line_edit")
        self.gender_line_edit.setGeometry(QRect(157, 0, 246, 47))
        self.gender_line_edit.setFrameShape(QFrame.StyledPanel)
        self.gender_line_edit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.gender_line_edit)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gender_line_edit_2 = QFrame(self.gender_line_edit)
        self.gender_line_edit_2.setObjectName(u"gender_line_edit_2")
        self.gender_line_edit_2.setMaximumSize(QSize(16777215, 50))
        self.gender_line_edit_2.setFrameShape(QFrame.StyledPanel)
        self.gender_line_edit_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.gender_line_edit_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.genderLineEdit = QLineEdit(self.gender_line_edit_2)
        self.genderLineEdit.setObjectName(u"genderLineEdit")
        sizePolicy.setHeightForWidth(self.genderLineEdit.sizePolicy().hasHeightForWidth())
        self.genderLineEdit.setSizePolicy(sizePolicy)
        self.genderLineEdit.setMinimumSize(QSize(1, 35))
        self.genderLineEdit.setMaximumSize(QSize(281, 35))
        self.genderLineEdit.setLayoutDirection(Qt.LeftToRight)
        self.genderLineEdit.setStyleSheet(u"QLineEdit{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	border: 2px solid rgb(98, 103, 255);\n"
"	border-radius: 10px;\n"
"	color: #2a2b2d;\n"
"	background-color: #FFF;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"")
        self.genderLineEdit.setAlignment(Qt.AlignCenter)
        self.genderLineEdit.setDragEnabled(True)
        self.genderLineEdit.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.genderLineEdit)


        self.horizontalLayout_24.addWidget(self.gender_line_edit_2)

        self.gender_label = QFrame(self.gender)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setGeometry(QRect(0, 0, 150, 47))
        self.gender_label.setMaximumSize(QSize(150, 16777215))
        self.gender_label.setFrameShape(QFrame.StyledPanel)
        self.gender_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.gender_label)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.genderLabel = QLabel(self.gender_label)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setMaximumSize(QSize(150, 16777215))
        self.genderLabel.setStyleSheet(u"QLabel{\n"
"	font: 87 10pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: #FFF;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.genderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.genderLabel)


        self.verticalLayout_3.addWidget(self.gender)


        self.horizontalLayout_19.addWidget(self.left_side)

        self.right_side = QFrame(self.patient_details)
        self.right_side.setObjectName(u"right_side")
        self.right_side.setFrameShape(QFrame.StyledPanel)
        self.right_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_side)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.right_side)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(157, 0, 246, 47))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 50))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.patientIdLineEdit_3 = QLineEdit(self.frame_34)
        self.patientIdLineEdit_3.setObjectName(u"patientIdLineEdit_3")
        sizePolicy.setHeightForWidth(self.patientIdLineEdit_3.sizePolicy().hasHeightForWidth())
        self.patientIdLineEdit_3.setSizePolicy(sizePolicy)
        self.patientIdLineEdit_3.setMinimumSize(QSize(1, 35))
        self.patientIdLineEdit_3.setMaximumSize(QSize(281, 35))
        self.patientIdLineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	border: 2px solid rgb(98, 103, 255);\n"
"	border-radius: 10px;\n"
"	color: #2a2b2d;\n"
"	background-color: #FFF;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"")
        self.patientIdLineEdit_3.setAlignment(Qt.AlignCenter)
        self.patientIdLineEdit_3.setDragEnabled(True)
        self.patientIdLineEdit_3.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.patientIdLineEdit_3)


        self.horizontalLayout_27.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(0, 0, 150, 47))
        self.frame_35.setMaximumSize(QSize(150, 16777215))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_35)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(150, 16777215))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	font: 87 10pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: #FFF;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.frame_32)

        self.frame_36 = QFrame(self.right_side)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(157, 0, 246, 47))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 50))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.DobLineEdit = QLineEdit(self.frame_38)
        self.DobLineEdit.setObjectName(u"DobLineEdit")
        sizePolicy.setHeightForWidth(self.DobLineEdit.sizePolicy().hasHeightForWidth())
        self.DobLineEdit.setSizePolicy(sizePolicy)
        self.DobLineEdit.setMinimumSize(QSize(1, 35))
        self.DobLineEdit.setMaximumSize(QSize(281, 35))
        self.DobLineEdit.setStyleSheet(u"QLineEdit{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	border: 2px solid rgb(98, 103, 255);\n"
"	border-radius: 10px;\n"
"	color: #2a2b2d;\n"
"	background-color: #FFF;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"")
        self.DobLineEdit.setAlignment(Qt.AlignCenter)
        self.DobLineEdit.setDragEnabled(True)
        self.DobLineEdit.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.DobLineEdit)


        self.horizontalLayout_30.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(0, 0, 150, 47))
        self.frame_39.setMaximumSize(QSize(150, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_39)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(150, 16777215))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	font: 87 10pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: #FFF;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.frame_36)


        self.horizontalLayout_19.addWidget(self.right_side)


        self.verticalLayout_10.addWidget(self.patient_details)

        self.patient_data = QFrame(self.main)
        self.patient_data.setObjectName(u"patient_data")
        self.patient_data.setMaximumSize(QSize(16777215, 16777215))
        self.patient_data.setStyleSheet(u"border:0px solid;\n"
"background-color: rgb(215, 212, 255);")
        self.patient_data.setFrameShape(QFrame.NoFrame)
        self.patient_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.patient_data)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.tableWidget = QTableWidget(self.patient_data)
        if (self.tableWidget.columnCount() < 15):
            self.tableWidget.setColumnCount(15)
        print('table')
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.soap_note = QLabel(self.patient_data)
        self.soap_note.setObjectName(u"soap_note")
        self.soap_note.setMinimumSize(QSize(0, 30))
        self.soap_note.setMaximumSize(QSize(16777215, 37))
        self.soap_note.setAutoFillBackground(False)
        self.soap_note.setStyleSheet(u"border-radius: 0px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.soap_note)

        self.soapLineEdit = QLineEdit(self.patient_data)
        self.soapLineEdit.setObjectName(u"soapLineEdit")
        self.soapLineEdit.setMinimumSize(QSize(0, 70))
        self.soapLineEdit.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.soapLineEdit.setFont(font)
        self.soapLineEdit.setLayoutDirection(Qt.LeftToRight)
        self.soapLineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255);")
        self.soapLineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.soapLineEdit.setDragEnabled(True)
        self.soapLineEdit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.soapLineEdit)

        self.back_frame = QFrame(self.patient_data)
        self.back_frame.setObjectName(u"back_frame")
        self.back_frame.setMinimumSize(QSize(0, 30))
        self.back_frame.setMaximumSize(QSize(16777215, 30))
        self.back_frame.setLayoutDirection(Qt.RightToLeft)
        self.back_frame.setFrameShape(QFrame.StyledPanel)
        self.back_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.back_frame)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.back_btn = QPushButton(self.back_frame)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy1.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy1)
        self.back_btn.setMinimumSize(QSize(125, 30))
        self.back_btn.setMaximumSize(QSize(125, 30))
        self.back_btn.setLayoutDirection(Qt.RightToLeft)
        self.back_btn.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	border: 2px solid rgb(131, 133, 135);\n"
"	border-radius: 15px;\n"
"	color: #2a2b2d;\n"
"	background-color: rgb(131, 133, 135);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: #FFF;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,114,160,1), stop:1 rgba(0,212,255,1));\n"
"}\n"
"")

        self.horizontalLayout_33.addWidget(self.back_btn)


        self.verticalLayout_5.addWidget(self.back_frame)


        self.verticalLayout_10.addWidget(self.patient_data)


        self.horizontalLayout_34.addWidget(self.main)


        self.horizontalLayout_18.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.patient_details_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.content_bar_2)

        self.credits_bar_2 = QFrame(self.drop_shadow_frame)
        self.credits_bar_2.setObjectName(u"credits_bar_2")
        self.credits_bar_2.setMaximumSize(QSize(16777215, 40))
        self.credits_bar_2.setStyleSheet(u"background-color: none;")
        self.credits_bar_2.setFrameShape(QFrame.StyledPanel)
        self.credits_bar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.credits_bar_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.credits_bar_2)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_41)

        self.label_2 = QLabel(self.credits_bar_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font: 87 8pt \"Montserrat Black\";\n"
"	text-align: center;\n"
"	color: rgb(255, 85, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.frame_grip = QFrame(self.credits_bar_2)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_grip)


        self.verticalLayout_6.addWidget(self.credits_bar_2)


        self.horizontalLayout_10.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Patient Details", None))
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Patient ID: ", None))
        self.patientIdLineEdit_2.setText("")
        self.patientIdLineEdit_2.setPlaceholderText("")
        self.viewDetailsPushButton_2.setText(QCoreApplication.translate("MainWindow", u"View Details", None))
        self.patientLabel.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.patientLineEdit.setText("")
        self.patientLineEdit.setPlaceholderText("")
        self.genderLineEdit.setText("")
        self.genderLineEdit.setPlaceholderText("")
        self.genderLabel.setText(QCoreApplication.translate("MainWindow", u"Gender & Age", None))
        self.patientIdLineEdit_3.setText("")
        self.patientIdLineEdit_3.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Patient ID", None))
        self.DobLineEdit.setText("")
        self.DobLineEdit.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Encounter ID", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date and Time", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Chief Complaint", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Lab Orders Count", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Lab Results Count", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Medication Orders Count", None))
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Medication Fulfillment Count", None))
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Vital Sign Count", None))
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Therapy Orders Count", None))
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Therapy Actions Count", None))
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Immunization Count", None))
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Has Appt", None))
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Payment_status", None))
        self.soap_note.setText(QCoreApplication.translate("MainWindow", u"  SOAP Note", None))
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Created By Jagannath", None))
    # retranslateUi

