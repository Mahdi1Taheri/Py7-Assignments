import sys
import sqlite3
from functools import partial
from datetime import datetime
from win10toast import ToastNotifier
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
from alarm_window import Ui_OtherWindow
from mytime import MyTime
from thread_stopwatch import *
from thread_timer import *
from thread_worldclock import *
from database import Database
from thread_alarm import AlarmThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        self.con = sqlite3.connect('alarm.db')
        self.mcursor = self.con.cursor()
        self.window2 = QMainWindow()
        self.ui2 = Ui_OtherWindow()
        self.ui2.setupUi(self.window2)
        
        for i in range(100):
            self.time = datetime.now()
        # Notification obj
        self.toast = ToastNotifier()
        
        self.db = Database()
        # stopwatch section
        self.thread_stopwatch = StopwatchThread()
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)

        # Timer section
        self.thread_timer = TimerThread()
        self.ui.btn_timer_start.clicked.connect(self.start_timer)
        self.ui.btn_timer_stop.clicked.connect(self.stop_timer)
        self.ui.btn_timer_reset.clicked.connect(self.reset_timer)
        # ------------- #
        
        self.thread_stopwatch.new_signal.connect(self.show_num)
        self.thread_timer.new_signal.connect(self.show_time_timer)

        # Alarm section
        self.thread_alarm = AlarmThread()
        self.ui.btn_add.clicked.connect(self.add_alarm)
         
        self.thread_alarm.start()
        
        # WorldClock section
        self.thread_worldclock = WorldThread()
        self.thread_worldclock.new_signal.connect(self.show_worldclock)
        self.thread_worldclock.start()

        # center the text in QLineEdit
        self.ui.le_hour.setAlignment(Qt.AlignmentFlag.AlignCenter)       
        self.ui.le_minute.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.ui.le_second.setAlignment(Qt.AlignmentFlag.AlignCenter)  

    # add alarms to database
    def add_alarm(self):
        self.name = self.ui.alarm_name.text()
        self.hour = self.ui.alarm_hour.text()
        self.minute = self.ui.alarm_minute.text()
        self.mcursor.execute(f'INSERT INTO alarm(name,hour,minute) VALUES("{self.name}","{self.hour}","{self.minute}")')
        self.con.commit()
        self.show_alarm()
        self.ui.alarm_name.setText("")
        self.ui.alarm_hour.setText("")
        self.ui.alarm_minute.setText("")

    def show_alarm(self):
        alarms = self.db.get_alarms()
        for i in range(len(alarms)):
            lable = QLineEdit()
            lable.setStyleSheet("QLineEdit{ font-family: Titillium;font-size:15; border: 2px solid rgb(37,39,48);border-radius: 20px;color: #FFF;padding: 0 20px 0 20px;background-color: rgb(34,36,44)}\
                QLineEdit:hover{ border: 2px solid rgb(48,50,62);}\
                QLineEdit:focus{border: 2px solid rgb(24, 200, 121);background-color: rgb(84, 84, 84);}")
            # checkbox = QCheckBox()
            # checkbox.setStyleSheet("QCheckBox::indicator{ width: 25; height: 25;}")
            remove_btn = QPushButton()
            remove_btn.setStyleSheet("QPushButton { background-color: rgb(255, 151, 23);\
                                        border: none; color: white; padding: 5px 15px; text-align: center;\
                                        text-decoration: none; display: inline-block; font-size: 10px; border-radius: 7px;\
                                        }\
                                        QPushButton:hover{background-color: #c57412;}\
                                        QPushButton:pressed{background-color: rgb(67, 133, 200);}")
            lable.setText(f"{str(alarms[i][1])} | {str(alarms[i][2])}")
            lable.setReadOnly(True)
            # checkbox.setText("")
            # if alarms[i][4] == 0:
            #     new_checkbox.setChecked(True)
            remove_btn.setText("Del")
            self.ui.gridLayout.addWidget(lable, i,0)
            # self.ui.gridLayout.addWidget(checkbox, i,1)
            self.ui.gridLayout.addWidget(remove_btn, i,2)
            # checkbox.clicked.connect(partial(self.is_active, alarms[i][0], alarms[i][4]))
            remove_btn.clicked.connect(partial(self.db.remove_alarm, alarms[i][0]))
    
    
 
    # new window for add alarms
    # def alarm_window(self):
    #     self.window2 = QMainWindow()
    #     self.ui2 = Ui_OtherWindow()
    #     self.ui2.setupUi(self.window2)
    #     self.window2.show()

    def show_worldclock(self):
        self.thread_worldclock.de_time = self.thread_worldclock.teh_time.sub(MyTime(2,30,0))
        self.thread_worldclock.ny_time = self.thread_worldclock.teh_time.sub(MyTime(7,30,0))
        self.ui.teh_lb.setText(f"Iran, Tehran         | {self.thread_worldclock.teh_time.hour}:{self.thread_worldclock.teh_time.minute}")
        self.ui.de_lb.setText(f"Germany, Berlin | {self.thread_worldclock.de_time.hour}:{self.thread_worldclock.de_time.minute}")
        self.ui.us_lb.setText(f"USA, New York   | {self.thread_worldclock.ny_time.hour}:{self.thread_worldclock.ny_time.minute}")
        
    
    # Stopwatch methods
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def reset_stopwatch(self):
        self.thread_stopwatch.time.hour = 0
        self.thread_stopwatch.time.minute = 0
        self.thread_stopwatch.time.second = 0
        self.ui.lb_time.setText("0:0:0")
    
    # Timer methods
    def start_timer(self):
        if self.ui.le_hour.isModified() or self.ui.le_minute.isModified() or self.ui.le_second.isModified() == True:
            if (int(self.ui.le_hour.text()) or int(self.ui.le_minute.text()) or int(self.ui.le_second.text())) >= 0:
                self.thread_timer.set_time(int(self.ui.le_hour.text()),int(self.ui.le_minute.text()),int(self.ui.le_second.text()))
                self.thread_timer.start()

    def stop_timer(self):
        self.thread_timer.terminate()

    def reset_timer(self):
        self.thread_timer.time.hour = 0 
        self.ui.le_hour.setText("0")
        self.thread_timer.time.minute = 0
        self.ui.le_minute.setText("0")
        self.thread_timer.time.second = 0
        self.ui.le_second.setText("0")
        self.stop_timer()

    def show_num(self):
        self.ui.lb_time.setText(f"{self.thread_stopwatch.time.hour}:{self.thread_stopwatch.time.minute}:{self.thread_stopwatch.time.second}")

    def show_time_timer(self):
        self.ui.le_hour.setText(str(self.thread_timer.time.hour))
        self.ui.le_minute.setText(str(self.thread_timer.time.minute))
        self.ui.le_second.setText(str(self.thread_timer.time.second))
        if self.thread_timer.time.second + self.thread_timer.time.minute + self.thread_timer.time.hour <= 0:
            self.toast.show_toast(
                    "Timer Done!",
                    f"Timer ended at {self.time.hour}:{self.time.minute}:{self.time.second}",
                    duration = 20,
                    icon_path = "time.ico",
                    threaded = True,
                    )
            self.reset_timer()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
