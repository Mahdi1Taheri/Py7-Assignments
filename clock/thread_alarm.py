import time
from PySide6.QtCore import *
from mytime import MyTime
from win10toast import ToastNotifier
from database import Database

class AlarmThread(QThread):
    def __init__(self):
        super().__init__()
        self.time_alarms = []
        self.current_time = MyTime(int(time.strftime('%H')),int(time.strftime('%M')),int(time.strftime('%S')))
        self.toast = ToastNotifier()
        self.db = Database()

    def run(self):
        while True:
            self.current_time.plus()
            time.sleep(1)
            for i in self.time_alarms:
                if self.current_time == self.db.get_time_alarm:
                    self.toast.show_toast(
                    "Alarm",
                    f"Alarm Time",
                    duration = 20,
                    icon_path = "time.ico",
                    threaded = True,
                    )