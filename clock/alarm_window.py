# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alarm_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTimeEdit,
    QWidget)

class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        if not OtherWindow.objectName():
            OtherWindow.setObjectName(u"OtherWindow")
        OtherWindow.resize(454, 219)
        OtherWindow.setStyleSheet(u"background-color: rgb(67, 67, 67);")
        self.centralwidget = QWidget(OtherWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_add_alarm = QPushButton(self.centralwidget)
        self.btn_add_alarm.setObjectName(u"btn_add_alarm")
        self.btn_add_alarm.setGeometry(QRect(150, 130, 171, 41))
        font = QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_add_alarm.setFont(font)
        self.btn_add_alarm.setStyleSheet(u"QPushButton {\n"
" 	background-color: rgb(26, 200, 81);\n"
"	border: none;\n"
"	color: white;\n"
"    padding: 10px 24px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 20px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#159f3e;\n"
"}")
        self.alarm_name = QLineEdit(self.centralwidget)
        self.alarm_name.setObjectName(u"alarm_name")
        self.alarm_name.setGeometry(QRect(10, 80, 251, 41))
        font1 = QFont()
        font1.setFamilies([u"Titillium"])
        font1.setPointSize(14)
        self.alarm_name.setFont(font1)
        self.alarm_name.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding: 0 20px 0 20px;\n"
"	background-color: rgb(34,36,44)\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(24, 200, 121);\n"
"	background-color: rgb(84, 84, 84);\n"
"	\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 181, 31))
        font2 = QFont()
        font2.setFamilies([u"Titillium Bd"])
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:rgb(175, 175, 175)")
        self.time_edit = QTimeEdit(self.centralwidget)
        self.time_edit.setObjectName(u"time_edit")
        self.time_edit.setGeometry(QRect(270, 80, 171, 41))
        font3 = QFont()
        font3.setFamilies([u"Titillium"])
        font3.setPointSize(15)
        self.time_edit.setFont(font3)
        self.time_edit.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding: 0 20px 0 20px;\n"
"	background-color: rgb(34,36,44)\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(24, 200, 121);\n"
"	background-color: rgb(84, 84, 84);\n"
"	\n"
"}")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OtherWindow)
        self.statusbar.setObjectName(u"statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)

        QMetaObject.connectSlotsByName(OtherWindow)
    # setupUi

    def retranslateUi(self, OtherWindow):
        OtherWindow.setWindowTitle(QCoreApplication.translate("OtherWindow", u"MainWindow", None))
        self.btn_add_alarm.setText(QCoreApplication.translate("OtherWindow", u"Add", None))
        self.alarm_name.setText("")
        self.alarm_name.setPlaceholderText(QCoreApplication.translate("OtherWindow", u"Enter alarm name...", None))
        self.label.setText(QCoreApplication.translate("OtherWindow", u"Add Alarm", None))
    # retranslateUi

