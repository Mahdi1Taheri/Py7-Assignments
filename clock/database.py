import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('alarm_list.db')
        self.cursor = self.con.cursor()

    def get_time_alarm(self,id):
        result = self.cursor.execute(f'SELECT time FROM alarms WHERE id == {id}')
        alarm_time = result.fetchone()
        return alarm_time
    
    def get_alarms(self):
        result = self.cursor.execute('SELECT * FROM alarms')
        alarms = result.fetchall()
        return alarms
    
    def remove_alarm(self,id):
        self.cursor.execute(f'DELETE FROM alarms WHERE id = "{id}"')
        self.con.commit()

    def edit_alarm(self, ntime, id):
        self.cursor.execute(f'UPDATE alarms SET time="{ntime}" WHERE id = {id}')
        self.con.commit()