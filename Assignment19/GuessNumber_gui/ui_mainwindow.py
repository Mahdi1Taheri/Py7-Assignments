# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(454, 274)
        MainWindow.setStyleSheet(u"background-color: rgb(107, 255, 53);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 351, 31))
        font = QFont()
        font.setFamilies([u"Gearus"])
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(150, 60, 151, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 321, 31))
        font1 = QFont()
        font1.setFamilies([u"Caviar Dreams"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setObjectName(u"line_edit")
        self.line_edit.setGeometry(QRect(115, 210, 131, 31))
        font2 = QFont()
        font2.setPointSize(15)
        self.line_edit.setFont(font2)
        self.line_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 150, 181, 61))
        font3 = QFont()
        font3.setFamilies([u"Caviar Dreams"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(150, 140, 151, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.btn_guess = QPushButton(self.centralwidget)
        self.btn_guess.setObjectName(u"btn_guess")
        self.btn_guess.setGeometry(QRect(250, 210, 75, 31))
        font4 = QFont()
        font4.setFamilies([u"Caviar Dreams"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.btn_guess.setFont(font4)
        self.btn_guess.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 255, 127);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color: rgb(0, 0, 0) ;\n"
"	padding-top: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 199, 199);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(1, 220, 121);\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 90, 41, 31))
        self.label_3.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Guess The Number", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"guess a number between  0 and", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Your Guess", None))
        self.btn_guess.setText(QCoreApplication.translate("MainWindow", u"guess", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"100", None))
    # retranslateUi

