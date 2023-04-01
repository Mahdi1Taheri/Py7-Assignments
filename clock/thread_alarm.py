import time
from PySide6.QtCore import *
from mytime import MyTime
from win10toast import ToastNotifier
class AlarmThread(QThread):
    def __init__(self):
        super().__init__()
        self.Time_Alarms = []
        self.current_time = MyTime(int(time.strftime('%H')),int(time.strftime('%M')),int(time.strftime('%S')))
        self.toast = ToastNotifier()

    def run(self):
        while True:
            self.current_time.plus()
            time.sleep(1)
            for alarmtime in self.Time_Alarms:
                if self.current_time.equal(alarmtime):
                    self.toast.show_toast(
                    "Alarm",
                    f"Alarm Time",
                    duration = 20,
                    icon_path = "time.ico",
                    threaded = True,
                    )