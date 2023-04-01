import time
from datetime import datetime
from PySide6.QtCore import *
from mytime import *
from win10toast import ToastNotifier



class TimerThread(QThread):
    new_signal = Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.time = MyTime(0,15,0) 
        
    def run(self):
        while True:
            self.time.sub_sec()
            self.new_signal.emit(self.time)
            time.sleep(1)
            
    def set_time(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
        self.time = MyTime(self.hour,self.minute,self.second)

    