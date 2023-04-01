import sys
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

        self.ui2 = Ui_OtherWindow()
        
        for i in range(100):
            self.time = datetime.now()
        # Notification obj
        self.toast = ToastNotifier()
        
        # stopwatch section
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)

        # Timer section
        self.ui.btn_timer_start.clicked.connect(self.start_timer)
        self.ui.btn_timer_stop.clicked.connect(self.stop_timer)
        self.ui.btn_timer_reset.clicked.connect(self.reset_timer)
        # ------------- #
        
        self.thread_stopwatch = StopwatchThread()
        self.thread_timer = TimerThread()
        self.db = Database()
        self.thread_alarm = AlarmThread()
        
        self.thread_stopwatch.new_signal.connect(self.show_num)
        self.thread_timer.new_signal.connect(self.show_time_timer)
        self.ui.btn_add.clicked.connect(self.alarm_window)
        self.ui2.btn_add_alarm.clicked.connect(self.db.add_alarm(str(self.ui2.alarm_name,self.ui2.time_edit.time())))
        self.thread_alarm.start()
        # WorldClock section
        self.thread_worldclock = WorldThread()
        self.thread_worldclock.new_signal.connect(self.show_worldclock)
        self.thread_worldclock.start()

        # center text in QLineEdit
        self.ui.le_hour.setAlignment(Qt.AlignmentFlag.AlignCenter)       
        self.ui.le_minute.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.ui.le_second.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        
    def alarm_window(self):
        self.window2 = QMainWindow()
        self.ui2 = Ui_OtherWindow()
        self.ui2.setupUi(self.window2)
        self.window2.show()


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
