import time
from PySide6.QtCore import *
from mytime import *

class TimerThread(QThread):
    new_signal = Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.time = MyTime(0,0,0) 
        
    def run(self):
        while True:
            self.time.sub()
            self.new_signal.emit(self.time)
            time.sleep(1)

    def set_time(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s