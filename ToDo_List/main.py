import sys
import sqlite3
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_mainwindow import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.db = Database()

        self.con = sqlite3.connect("todo_list.db")
        self.mcursor = self.con.cursor()
        

        # for i in range(len(tasks)):
        #     new_checkbox = QCheckBox()
        #     new_label = QLabel() 
        #     new_label.setText(tasks[i][1])

        #     new_label2 = QLabel()
        #     new_label2.setText(str(tasks[i][0]))

        #     self.ui.gl_tasks.addWidget(new_checkbox,i,0)
        # tasks = self.db.get_tasks()
    
        # for i in range(len(tasks)):
        #     self.ui.sb_high.clicked.connect(partial(self.db.priority,"high",tasks[i][0]))
        #     self.ui.sb_middle.clicked.connect(partial(self.db.priority,"middle",tasks[i][0]))
        #     self.ui.sb_low.clicked.connect(partial(self.db.priority, "low",tasks[i][0]))
        self.ui.btn_newtask.clicked.connect(self.new_task)

    
    def del_task(self,id):
        self.db.remove_task(id)

 
    def new_task(self):
        # getting title 
        new_title = self.ui.task_title.text()
        new_description = self.ui.description.toPlainText()
        # self.db.priority(self.ui.comboBox.currentText())

        # tasks = self.db.get_tasks()
           
        # for i in range(len(tasks)):
        #     if self.ui.sb_high.isChecked() == True:
        
        
        # Adding tasks to Database 
        self.db.add_new_task(new_title,new_description,self.ui.comboBox.currentText())
        self.add_widget()
        self.ui.task_title.setText("")
        self.ui.description.setText("")
        
        
        
    def add_widget(self):
            global id
            tasks = self.db.get_tasks()
            
            
            for i in range(len(tasks)):
                id = tasks[i][0]
                new_checkbox = QCheckBox()
                new_label = QLabel()  
                new_label.setText(tasks[i][1])
                new_label.setToolTip(f"{tasks[i][2]} | {self.ui.date_time_edit.text()}")
                del_btn = QPushButton()
                del_btn.setStyleSheet("QPushButton {\
                        background-color: rgb(26, 200, 81);font-family: Tillitum; border: none; color: white; padding: 5px 1px; text-align: center; text-decoration: none; display: inline-block; font-size: 10px; border-radius: 7px;}\
                    QPushButton:hover{background-color:#159f3e;}\
                    QPushButton:pressed{background-color: rgb(67, 133, 200);}")
                del_btn.setText("delete")

                color_widget = QLabel()
                color_widget.setAlignment(Qt.AlignCenter)
                color_widget.resize(5,10)
                if tasks[i][4] == 'High':
                    color_widget.setStyleSheet("background-color: #db1414; border-radius: 5px; font-family: Tilitium")
                    color_widget.setText("high")
                elif tasks[i][4] == 'Middle':
                    color_widget.setStyleSheet("background-color: #fac105; border-radius: 5px; font-family: Tilitium")
                    color_widget.setText("middle")
                elif tasks[i][4] == 'Low':
                    color_widget.setStyleSheet("background-color: #08cf79; border-radius: 5px; font-family: Tilitium")
                    color_widget.setText("low")


                
                
                self.ui.gridLayout.addWidget(new_checkbox,i,0)
                self.ui.gridLayout.addWidget(new_label, i, 1)
                self.ui.gridLayout.addWidget(del_btn, i, 2)
                self.ui.gridLayout.addWidget(color_widget,i,3 )
                del_btn.clicked.connect(partial(self.del_task,tasks[i][0]))  
                
                new_checkbox.clicked.connect(partial(self.db.done_task,tasks[i][0]))

                

                if tasks[i][3] == 1:
                    new_checkbox.setChecked(True)
                else:
                    new_checkbox.setChecked(False)

                if tasks[i][4] == "high":
                    new_checkbox.setStyleSheet("QCheckBox{ background-color: solid red}")
                elif tasks[i][4] == "middle":
                    new_checkbox.setStyleSheet("QCheckBox{ background-color: solid yellow}")
                elif tasks[i][4] == "low":
                    new_checkbox.setStyleSheet("QCheckBox{ background-color: solid blue}")
                else:
                    pass

                

                
                # new_checkbox.toggled.connect(self.db.done_task)




    # def msgButtonClick(self):
    #     self.close()
         




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    app.exec()
