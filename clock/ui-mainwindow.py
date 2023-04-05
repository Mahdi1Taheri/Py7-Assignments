# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(612, 500)
        MainWindow.setStyleSheet(u"background-color: rgb(67, 67, 67);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 591, 471))
        font = QFont()
        font.setFamilies([u"Titillium"])
        font.setPointSize(11)
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid lightgray;\n"
"    background: #ff9717;\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #ff9717;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: #757575;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bot"
                        "tom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.btn_start_stopwatch = QPushButton(self.widget)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(40, 230, 171, 41))
        font1 = QFont()
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.btn_start_stopwatch.setFont(font1)
        self.btn_start_stopwatch.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 151, 23);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 10px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 20px;\n"
"  border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #c57412;\n"
"}")
        self.btn_stop_stopwatch = QPushButton(self.widget)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(220, 230, 161, 41))
        self.btn_stop_stopwatch.setFont(font1)
        self.btn_stop_stopwatch.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 151, 23);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 10px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 20px;\n"
"  border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #c57412;\n"
"}")
        self.lb_time = QLabel(self.widget)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setGeometry(QRect(250, 130, 211, 61))
        font2 = QFont()
        font2.setFamilies([u"Seven Segment"])
        font2.setPointSize(40)
        self.lb_time.setFont(font2)
        self.lb_time.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.btn_reset_stopwatch = QPushButton(self.widget)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(390, 230, 151, 41))
        self.btn_reset_stopwatch.setFont(font1)
        self.btn_reset_stopwatch.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 151, 23);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 10px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 20px;\n"
"  border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #c57412;\n"
"}")
        self.tabWidget.addTab(self.widget, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.le_hour = QLineEdit(self.tab_4)
        self.le_hour.setObjectName(u"le_hour")
        self.le_hour.setGeometry(QRect(130, 80, 91, 91))
        font3 = QFont()
        font3.setPointSize(50)
        self.le_hour.setFont(font3)
        self.le_hour.setStyleSheet(u"\n"
"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	alginment: center\n"
"}")
        self.le_minute = QLineEdit(self.tab_4)
        self.le_minute.setObjectName(u"le_minute")
        self.le_minute.setGeometry(QRect(250, 80, 91, 91))
        self.le_minute.setFont(font3)
        self.le_minute.setStyleSheet(u"\n"
"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	alginment: center\n"
"}")
        self.le_second = QLineEdit(self.tab_4)
        self.le_second.setObjectName(u"le_second")
        self.le_second.setGeometry(QRect(370, 80, 91, 91))
        self.le_second.setFont(font3)
        self.le_second.setStyleSheet(u"\n"
"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	alginment: center\n"
"}")
        self.btn_timer_start = QPushButton(self.tab_4)
        self.btn_timer_start.setObjectName(u"btn_timer_start")
        self.btn_timer_start.setGeometry(QRect(50, 250, 161, 41))
        self.btn_timer_start.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 151, 23);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 10px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 20px;\n"
"  border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #c57412;\n"
"}")
        self.btn_timer_stop = QPushButton(self.tab_4)
        self.btn_timer_stop.setObjectName(u"btn_timer_stop")
        self.btn_timer_stop.setGeometry(QRect(220, 250, 141, 41))
        self.btn_timer_stop.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 151, 23);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 10px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 20px;\n"
"  border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #c57412;\n"
"}")
        self.btn_timer_reset = QPushButton(self.tab_4)
        self.btn_timer_reset.setObjectName(u"btn_timer_reset")
        self.btn_timer_reset.setGeometry(QRect(370, 250, 161, 41))
        self.btn_timer_reset.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 151, 23);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 10px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 20px;\n"
"  border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #c57412;\n"
"}")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.btn_add = QPushButton(self.tab_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(230, 370, 161, 41))
        font4 = QFont()
        font4.setBold(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.btn_add.setFont(font4)
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 151, 23);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 10px 24px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 20px;\n"
"  border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #c57412;\n"
"}")
        self.alarm_name = QLineEdit(self.tab_2)
        self.alarm_name.setObjectName(u"alarm_name")
        self.alarm_name.setGeometry(QRect(10, 310, 341, 51))
        font5 = QFont()
        font5.setFamilies([u"Titillium"])
        font5.setPointSize(14)
        self.alarm_name.setFont(font5)
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
        self.alarm_time = QLineEdit(self.tab_2)
        self.alarm_time.setObjectName(u"alarm_time")
        self.alarm_time.setGeometry(QRect(360, 310, 221, 51))
        self.alarm_time.setFont(font5)
        self.alarm_time.setStyleSheet(u"QLineEdit{\n"
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
        self.verticalLayoutWidget = QWidget(self.tab_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 9, 571, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 40, 551, 81))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(117, 117, 117);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-radius: 5px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.teh_lb = QLabel(self.frame)
        self.teh_lb.setObjectName(u"teh_lb")
        self.teh_lb.setGeometry(QRect(10, 10, 441, 51))
        font6 = QFont()
        font6.setFamilies([u"Titillium"])
        font6.setPointSize(20)
        self.teh_lb.setFont(font6)
        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 150, 551, 81))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(117, 117, 117);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-radius: 5px\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.de_lb = QLabel(self.frame_2)
        self.de_lb.setObjectName(u"de_lb")
        self.de_lb.setGeometry(QRect(10, 10, 441, 51))
        self.de_lb.setFont(font6)
        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 260, 551, 81))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(117, 117, 117);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-radius: 5px\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.us_lb = QLabel(self.frame_3)
        self.us_lb.setObjectName(u"us_lb")
        self.us_lb.setGeometry(QRect(10, 10, 441, 51))
        self.us_lb.setFont(font6)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lb_time.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.le_hour.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.le_minute.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.le_second.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_timer_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_timer_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_timer_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.alarm_name.setText("")
        self.alarm_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter alarm name...", None))
        self.alarm_time.setText("")
        self.alarm_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Time...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.teh_lb.setText("")
        self.de_lb.setText("")
        self.us_lb.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"World clock", None))
    # retranslateUi

