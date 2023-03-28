import time
from PySide6.QtCore import *
from mytime import MyTime


class StopwatchThread(QThread):
    new_signal = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0,00,00) 
        
    def run(self):
        while True:
            self.time.plus()
            self.new_signal.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.hour = 0
        self.time.minute = 00
        self.time.second = 00