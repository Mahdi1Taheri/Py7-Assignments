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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(622, 556)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.description = QTextEdit(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(20, 380, 311, 101))
        font = QFont()
        font.setFamilies([u"Titillium Lt"])
        font.setPointSize(11)
        self.description.setFont(font)
        self.description.setStyleSheet(u"QTextEdit{\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding: 0 20px 0 20px;\n"
"	background-color: rgb(34,36,44)\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"	border: 2px solid rgb(48,50,62);\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	border: 2px solid rgb(24, 200, 121);\n"
"	background-color: rgb(84, 84, 84);\n"
"	\n"
"}")
        self.btn_newtask = QPushButton(self.centralwidget)
        self.btn_newtask.setObjectName(u"btn_newtask")
        self.btn_newtask.setGeometry(QRect(350, 440, 241, 41))
        self.btn_newtask.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(67, 133, 200);\n"
"}\n"
"")
        self.btn_newtask.setCheckable(False)
        self.task_title = QLineEdit(self.centralwidget)
        self.task_title.setObjectName(u"task_title")
        self.task_title.setGeometry(QRect(340, 380, 261, 51))
        font1 = QFont()
        font1.setFamilies([u"Titillium Lt"])
        font1.setPointSize(12)
        self.task_title.setFont(font1)
        self.task_title.setStyleSheet(u"QLineEdit{\n"
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
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 601, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(110, 350, 431, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 490, 191, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 490, 71, 31))
        font2 = QFont()
        font2.setPointSize(15)
        self.label.setFont(font2)
        self.date_time_edit = QDateTimeEdit(self.centralwidget)
        self.date_time_edit.setObjectName(u"date_time_edit")
        self.date_time_edit.setGeometry(QRect(360, 490, 221, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Description...", None))
        self.btn_newtask.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.task_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Title...", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"High", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Middle", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Low", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Priority: ", None))
    # retranslateUi

