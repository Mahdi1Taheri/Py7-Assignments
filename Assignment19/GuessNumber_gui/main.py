import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.setFixedSize(454,274)
        self.u_guess = self.ui.btn_guess.clicked.connect(self.guess)
        self.number_of_guess = 0
        self.random_num = random.randint(0,100)
    
    def guess(self):
        self.user_guess = int(self.ui.line_edit.text())
        # while self.number_of_guess < 8:
            # Comparing the user's guess with the computer's number
        if self.user_guess == self.random_num:
            msg = QMessageBox()
            msg.setText(f"You guessed the right number! you won!\nyou guessed {self.number_of_guess} times!")
            msg.exec()
            self.random_num = random.randint(0,100)
                
        elif self.user_guess < self.random_num:
            self.number_of_guess += 1
            msg1 = QMessageBox()
            msg1.setText("Go Up⬆")
            msg1.exec()
        elif self.user_guess > self.random_num:
            self.number_of_guess += 1
            msg2 = QMessageBox()
            msg2.setText("Go Down⬇")
            msg2.exec()
        elif self.number_of_guess >= 8:
            msg3 = QMessageBox()
            msg3.setText("you loose")
            msg3.exec()        
app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()