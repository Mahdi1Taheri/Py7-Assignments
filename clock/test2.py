from datetime import datetime
import time
from PySide6.QtCore import *
from mytime import MyTime
from win10toast import ToastNotifier
from database import Database

db = Database()
toast = ToastNotifier()
alarms = db.get_alarms()

e = datetime.now()
print(e.hour,e.minute)

# for i in range(len(alarms)):
#         k = str(alarms[i][2]).split(":")
#         alarm = MyTime(int(k[i][0]), int(k[i][1]), 0)
#         print(alarm)