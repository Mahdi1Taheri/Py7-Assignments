import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('alarm.db')
        self.cursor = self.con.cursor()

    def get_time_alarm(self,id):
        result = self.cursor.execute(f'SELECT time FROM alarm WHERE id == {id}')
        alarm_time = result.fetchone()
        o = str(alarm_time[0])
        return o
    
    def get_alarms(self):
        result = self.cursor.execute('SELECT * FROM alarm')
        alarms = result.fetchall()
        return alarms
    
    def convertTuple(self,tup):
        str = ''.join(tup)
        return str
    
    def remove_alarm(self,id):
        self.cursor.execute(f'DELETE FROM alarm WHERE id = "{id}"')
        self.con.commit()

    def edit_alarm(self, ntime, id):
        self.cursor.execute(f'UPDATE alarm SET time="{ntime}" WHERE id = {id}')
        self.con.commit()