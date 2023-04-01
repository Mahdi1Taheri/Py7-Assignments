from datetime import datetime
import time
import pytz
from PySide6.QtCore import *
from mytime import *


class WorldThread(QThread):
    new_signal = Signal(MyTime)
    def __init__(self):
        super().__init__()
        # self.main = MainWindow()
        # self.utc = pytz.utc
        # self.timeZ_Teh = pytz.timezone('Asia/Tehran') 
        # self.timeZ_Ny = pytz.timezone('America/New_York')
        # self.timeZ_De = pytz.timezone('Europe/Berlin')
        self.teh_time = MyTime(time.strftime("%H"),time.strftime("%M"),time.strftime("%S")) # Tehran Time
        self.de_time = self.teh_time.sub(MyTime(2,30,0)) # Berlin Time
        self.ny_time = self.teh_time.sub(MyTime(8,30,0)) # New York Time
 
    def run(self):
        while True:
            self.teh_time.plus()
            self.new_signal.emit(self.teh_time)
            time.sleep(1)
            # self.dt_Teh = datetime.now(self.timeZ_Teh)
            # self.dt_Ny = datetime.now(self.timeZ_Ny)
            # self.dt_De = datetime.now(self.timeZ_De)
            # self.new_signal.emit(self.timeZ_Teh,self.timeZ_De,self.timeZ_Ny)
            


            
  
