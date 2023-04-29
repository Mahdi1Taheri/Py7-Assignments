import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("todo_list.db")
        self.cursor = self.con.cursor()

    # def priority(self,priority1):
    #     self.cursor.execute(f"INSERT INTO tasks(priority) VALUES('{priority1}')")
    #     self.con.commit()

    def get_tasks(self):
        result = self.cursor.execute("SELECT * FROM tasks")
        tasks = result.fetchall()
        return tasks

    def add_new_task(self, new_title, new_description, priority):
        query = f"INSERT INTO tasks(title, description,priority) VALUES('{new_title}', '{new_description}','{priority}')"
        self.cursor.execute(query)
        self.con.commit()

    def remove_task(self,id):
        query = f"DELETE FROM tasks WHERE id == '{id}'"
        self.cursor.execute(query)
        self.con.commit()

    def done_task(self,id): 
        num = 1
        num0 = 0
        self.cursor.execute(f"UPDATE tasks SET is_done = '{num}' WHERE id is '{id}'")
        # result2 = self.cursor.execute(f"SELECT order FROM tasks WHERE (order - {num}) <= 0")
        self.con.commit()
