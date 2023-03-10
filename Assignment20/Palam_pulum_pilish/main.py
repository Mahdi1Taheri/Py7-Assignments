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
        self.setWindowTitle('Palam Poloosh Pelish')
        self.ui.move1.clicked.connect(self.play_game())
        self.ui.move2.clicked.connect(self.play_game())

    def play_game(self):
        
        # define choices for the game
        choices = ['✋', '🤚']
         
        # randomly choose for computer 1 and computer 2
        comp1_choice = random.choice(choices)
        comp2_choice = random.choice(choices)

        self.ui.p1.setText(comp1_choice)
        self.ui.p2.setText(comp2_choice)

        # determine the winner based on the rules of the game
        if comp1_choice == comp2_choice:
            result_str = 'Tie!'
        elif (comp1_choice == '✋' and comp2_choice == '🤚') or \
            (comp1_choice == '🤚' and comp2_choice == '✋'):
            result_str = 'Comp 1 wins!'
        else:
            result_str = 'Comp 2 wins!'
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_window = MainWindow()
    game_window.show()
    sys.exit(app.exec_())


    
