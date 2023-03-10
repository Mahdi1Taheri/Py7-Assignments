import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.setWindowTitle('Palam Pulum Pilish')
        self.ui.move1.clicked.connect(self.play_game)
        self.ui.move2.clicked.connect(self.play_game)

    def play_game(self):
        choices = ['✋', '🤚']
        comp1_choice = random.choice(choices)
        comp2_choice = random.choice(choices)
        self.ui.p1.setText(comp1_choice)
        self.ui.p2.setText(comp2_choice)
        
        if comp1_choice == comp2_choice:
            result_tie = 'Tie!'
            self.ui.lable_win.setText(result_tie)
        elif (comp1_choice == '✋' and comp2_choice == '🤚') or \
            (comp1_choice == '🤚' and comp2_choice == '✋'):
            result_win1 = 'Comp 1 wins!'
            self.ui.lable_win.setText(result_win1)
        else:
            result_win2 = 'Comp 2 wins!'
            self.ui.lable_win.setText(result_win2)
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_window = MainWindow()
    game_window.show()
    sys.exit(app.exec_())
