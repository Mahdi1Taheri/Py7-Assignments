from datetime import datetime
import time
from PySide6.QtCore import *
from mytime import MyTime
from win10toast import ToastNotifier
from database import Database

class AlarmThread(QThread):
    def __init__(self):
        super().__init__()
        self.e = datetime.now()
        self.current_time = MyTime(self.e.hour,self.e.minute,0)
        self.toast = ToastNotifier()
        self.db = Database()

        self.time_alarms = self.db.get_alarms()
        # for j in range(len(self.time_alarms)):
        #     k = str(self.time_alarms[j][2]).split(":")
        # self.alarm_time = MyTime(int(k[0]),int(k[1],0))

    def run(self):
        while True:
            # self.current_time.plus()
            # time.sleep(1)
            for i in self.time_alarms:
                hour = self.time_alarms[i][2]
                minute = self.time_alarms[i][3]
                self.alarm_time = MyTime(hour,minute,0)
                if self.current_time.hour and self.current_time.minute == self.alarm_time.hour and self.alarm_time.minute:
                    self.toast.show_toast(
                    "Alarm",
                    f"Alarm Time",
                    duration = 20,
                    icon_path = "time.ico",
                    threaded = True,
                    )

# class AlarmThread(QThread):
#     signal_show = Signal(str, int, int)

#     def __init__(self):
#         super().__init__()
#         self.db = Database()
#         self.toast = ToastNotifier()
#         self.alarms = self.db.get_alarms()

#     def run(self):
#         while True:
#             for i in range(len(self.alarms)):
#                 k = str(self.alarms[i][2]).split(":")
#                 alarm = MyTime(int(k[i][0]), int(k[i][1]), 0)
#                 print(alarm)
#                 fulltime = datetime.now()
#                 nowtime = fulltime.strftime("%H:%M")
#                 splittime = nowtime.split(":")
#                 self.time = MyTime(int(splittime[0]), int(splittime[1]), 0)
#                 if self.time == alarm:
#                     self.signal_show.emit(self.alarms[i][1], k[i][0], k[i][1])
#                     self.toast.show_toast(
#                     "Alarm",
#                     f"Alarm Time",
#                     duration = 20,
#                     icon_path = "time.ico",
#                     threaded = True,
#                     )

    
#     def update(self):
#         self.alarms = self.db.get_alarms()