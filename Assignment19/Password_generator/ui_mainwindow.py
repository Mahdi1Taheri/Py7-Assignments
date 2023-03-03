# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'genpass_main.ui'
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
        MainWindow.resize(479, 409)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btngen1 = QPushButton(self.centralwidget)
        self.btngen1.setObjectName(u"btngen1")
        self.btngen1.setGeometry(QRect(60, 60, 91, 31))
        font = QFont()
        font.setFamilies([u"Microsoft Tai Le"])
        font.setPointSize(12)
        font.setBold(False)
        self.btngen1.setFont(font)
        self.btngen1.setStyleSheet(u"")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(60, 20, 371, 27))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(15)
        self.label_1.setFont(font1)
        self.line_edit1 = QLineEdit(self.centralwidget)
        self.line_edit1.setObjectName(u"line_edit1")
        self.line_edit1.setGeometry(QRect(160, 60, 241, 31))
        font2 = QFont()
        font2.setPointSize(15)
        self.line_edit1.setFont(font2)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(180, 110, 118, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(180, 280, 118, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.btngen2 = QPushButton(self.centralwidget)
        self.btngen2.setObjectName(u"btngen2")
        self.btngen2.setGeometry(QRect(60, 190, 91, 31))
        self.btngen2.setFont(font)
        self.btngen2.setStyleSheet(u"")
        self.line_edit2 = QLineEdit(self.centralwidget)
        self.line_edit2.setObjectName(u"line_edit2")
        self.line_edit2.setGeometry(QRect(160, 190, 241, 31))
        self.line_edit2.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 150, 242, 27))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 300, 291, 27))
        self.label_3.setFont(font1)
        self.line_edit3 = QLineEdit(self.centralwidget)
        self.line_edit3.setObjectName(u"line_edit3")
        self.line_edit3.setGeometry(QRect(160, 340, 241, 31))
        self.line_edit3.setFont(font2)
        self.btngen3 = QPushButton(self.centralwidget)
        self.btngen3.setObjectName(u"btngen3")
        self.btngen3.setGeometry(QRect(60, 340, 91, 31))
        self.btngen3.setFont(font)
        self.btngen3.setStyleSheet(u"")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(180, 400, 118, 3))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btngen1.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Generate Standard Strength Password", None))
        self.line_edit1.setText("")
        self.btngen2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.line_edit2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Generate Strong Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Generate extra Strong Password", None))
        self.line_edit3.setText("")
        self.btngen3.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

