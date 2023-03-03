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
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 453)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 206, 8);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_edit1 = QLineEdit(self.centralwidget)
        self.line_edit1.setObjectName(u"line_edit1")
        self.line_edit1.setGeometry(QRect(200, 90, 331, 41))
        font = QFont()
        font.setFamilies([u"Gearus"])
        font.setPointSize(11)
        font.setBold(False)
        self.line_edit1.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 541, 41))
        font1 = QFont()
        font1.setFamilies([u"Gearus"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.label.setFont(font1)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(160, 60, 241, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.btn_download = QPushButton(self.centralwidget)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setGeometry(QRect(40, 90, 151, 41))
        font2 = QFont()
        font2.setFamilies([u"Gearus"])
        font2.setBold(True)
        self.btn_download.setFont(font2)
        self.btn_download.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 152, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(41, 124, 0);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 160, 221, 16))
        font3 = QFont()
        font3.setFamilies([u"Neuropol X Rg"])
        font3.setPointSize(15)
        self.label_2.setFont(font3)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 190, 491, 231))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.line_edit1.setText(QCoreApplication.translate("MainWindow", u"Enter URL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"YouTube Downloader", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Video Information", None))
    # retranslateUi

