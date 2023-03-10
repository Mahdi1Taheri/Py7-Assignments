# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 552)
        MainWindow.setStyleSheet(u"background-color: rgb(132, 132, 198);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 421, 61))
        font = QFont()
        font.setFamilies([u"Lola Sans"])
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.move1 = QPushButton(self.centralwidget)
        self.move1.setObjectName(u"move1")
        self.move1.setGeometry(QRect(120, 330, 151, 141))
        font1 = QFont()
        font1.setPointSize(50)
        self.move1.setFont(font1)
        self.move1.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(0, 220, 220);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color: rgb(0, 0, 0) ;\n"
"	padding-top: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(0, 131, 197);\n"
"}\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(0, 214, 103);\n"
"}")
        self.move2 = QPushButton(self.centralwidget)
        self.move2.setObjectName(u"move2")
        self.move2.setGeometry(QRect(300, 330, 151, 141))
        self.move2.setFont(font1)
        self.move2.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(0, 220, 220);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color: rgb(0, 0, 0) ;\n"
"	padding-top: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(0, 131, 197);\n"
"}\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(0, 214, 103);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 280, 121, 41))
        font2 = QFont()
        font2.setFamilies([u"Lola Sans"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.p1 = QPushButton(self.centralwidget)
        self.p1.setObjectName(u"p1")
        self.p1.setGeometry(QRect(10, 120, 151, 141))
        self.p1.setFont(font1)
        self.p1.setStyleSheet(u"\n"
"QPushButton {\n"
"	background-color: rgb(170, 170, 255);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color: rgb(0, 0, 0) ;\n"
"	padding-top: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(0, 131, 197);\n"
"}\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(0, 214, 103);\n"
"}")
        self.p2 = QPushButton(self.centralwidget)
        self.p2.setObjectName(u"p2")
        self.p2.setGeometry(QRect(410, 120, 151, 141))
        self.p2.setFont(font1)
        self.p2.setStyleSheet(u"\n"
"QPushButton {\n"
"	background-color: rgb(170, 170, 255);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color: rgb(0, 0, 0) ;\n"
"	padding-top: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(0, 131, 197);\n"
"}\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(0, 214, 103);\n"
"}")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(220, 60, 151, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(100, 270, 371, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 70, 121, 41))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 70, 121, 41))
        self.label_4.setFont(font2)
        self.new_game = QPushButton(self.centralwidget)
        self.new_game.setObjectName(u"new_game")
        self.new_game.setGeometry(QRect(200, 480, 171, 41))
        font3 = QFont()
        font3.setFamilies([u"Lola Sans"])
        font3.setPointSize(15)
        self.new_game.setFont(font3)
        self.new_game.setStyleSheet(u"\n"
"QPushButton {\n"
"	background-color: rgb(170, 170, 255);\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color: rgb(0, 0, 0) ;\n"
"	padding-top: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(0, 131, 197);\n"
"}\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(0, 214, 103);\n"
"}")
        self.lable_win = QLabel(self.centralwidget)
        self.lable_win.setObjectName(u"lable_win")
        self.lable_win.setGeometry(QRect(170, 150, 231, 41))
        self.lable_win.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Palam Pulum Pilish Game", None))
        self.move1.setText(QCoreApplication.translate("MainWindow", u"\u270b", None))
        self.move2.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udd1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"your move", None))
        self.p1.setText("")
        self.p2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Player 2", None))
        self.new_game.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.lable_win.setText("")
    # retranslateUi

