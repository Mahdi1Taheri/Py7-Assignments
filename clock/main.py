import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
from mytime import MyTime
from thread_stopwatch import StopwatchThread 
from thread_timer import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # stopwatch section
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)

        # Timer section
        self.ui.btn_timer_start.clicked.connect(self.start_timer)
        self.ui.btn_timer_stop.clicked.connect(self.stop_timer)
        self.ui.btn_timer_reset.clicked.connect(self.reset_timer)
    
        self.thread_stopwatch = StopwatchThread()
        self.thread_timer = TimerThread()
        self.thread_stopwatch.new_signal.connect(self.show_num)
        self.thread_timer.new_signal.connect(self.show_time_timer)
    

    # Stopwatch methods
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
    
    # Timer methods
    def start_timer(self):
        if (int(self.ui.le_hour.text()) or int(self.ui.le_minute.text()) or int(self.ui.le_second.text())) >= 0:
            self.thread_timer.set_time(int(self.ui.le_hour.text()),int(self.ui.le_minute.text()),int(self.ui.le_second.text()))
            self.thread_timer.start()


    def stop_timer(self):
        self.thread_timer.terminate()

    def reset_timer(self):
        self.thread_timer.time.hour = 0 
        self.thread_timer.time.minute = 0
        self.thread_timer.time.second = 0
        time.sleep(0.5)
        self.stop_timer()

    def show_num(self,s):
        self.ui.lb_time.setText(f"{self.thread_stopwatch.time.hour}:{self.thread_stopwatch.time.minute}:{self.thread_stopwatch.time.second}")

    def show_time_timer(self):
        self.ui.le_hour.setText(str(self.thread_timer.time.hour))
        self.ui.le_minute.setText(str(self.thread_timer.time.minute))
        self.ui.le_second.setText(str(self.thread_timer.time.second))
        if self.thread_timer.time.second + self.thread_timer.time.minute + self.thread_timer.time.hour <= 0:
            self.thread_timer.terminate()

    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
