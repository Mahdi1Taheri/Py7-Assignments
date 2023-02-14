import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

draw = 0
p1 = 0
p2 = 0

def new_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("\
        QPushButton { background-color: rgb(170, 170, 255);\
            border-style: outset;border-width: 1px;border-color: rgb(0, 0, 0) ;\
	        padding-top: 5px;\
	        color: rgb(0, 0, 0);\
	        border-radius: 5px;\
}\
        QPushButton:hover {\
	        background-color: rgb(0, 131, 197);\
}\
        QPushButton:pressed {\
            background-color: rgb(0, 214, 103);\
}           font: GhostLike Demo; ")

def about():
    msg = QMessageBox(windowTitle = "About", text= "Tic-Toc-Toe is a two-player game that you can play in two modes: player vs. player and player vs. cpu.\nThe beads are also marked with blue and red colors.\nHow to play is very easy,\njust place your three pieces on the board to form a line.\nThis line can be slanted or straight.\nAttention! don't forget to choose the game mode.")
    msg.exec()
def check():
    global p1
    global p2
    if (buttons[0][0].text() == "X" and buttons[0][1].text() == "X" and buttons[0][2].text() == "X") or (buttons[1][0].text() == "X" and buttons[1][1].text() == "X" and buttons[1][2].text() == "X") or \
       (buttons[2][0].text() == "X" and buttons[2][1].text() == "X" and buttons[2][2].text() == "X") or (buttons[0][0].text() == "X" and buttons[1][0].text() == "X" and buttons[2][0].text() == "X") or \
       (buttons[0][1].text() == "X" and buttons[1][1].text() == "X" and buttons[2][1].text() == "X") or (buttons[0][2].text() == "X" and buttons[1][2].text() == "X" and buttons[2][2].text() == "X") or \
       (buttons[0][0].text() == "X" and buttons[1][1].text() == "X" and buttons[2][2].text() == "X") or (buttons[0][2].text() == "X" and buttons[1][1].text() == "X" and buttons[2][0].text() == "X"):
        msg_box = QMessageBox(text = "Player 1 WON!(X)")
        p1 += 1
        main_win.x_score.setText("X\n" + str(p1))
        msg_box.exec()
        new_game()

    elif (buttons[0][0].text() == "O" and buttons[0][1].text() == "O" and buttons[0][2].text() == "O") or (buttons[1][0].text() == "O" and buttons[1][1].text() == "O" and buttons[1][2].text() == "O") or \
       (buttons[2][0].text() == "O" and buttons[2][1].text() == "O" and buttons[2][2].text() == "O") or (buttons[0][0].text() == "O" and buttons[1][0].text() == "O" and buttons[2][0].text() == "O") or \
       (buttons[0][1].text() == "O" and buttons[1][1].text() == "O" and buttons[2][1].text() == "O") or (buttons[0][2].text() == "O" and buttons[1][2].text() == "O" and buttons[2][2].text() == "O") or \
       (buttons[0][0].text() == "O" and buttons[1][1].text() == "O" and buttons[2][2].text() == "O") or (buttons[0][2].text() == "O" and buttons[1][1].text() == "O" and buttons[2][0].text() == "O"):
        msg_box = QMessageBox(text = "Player 2 WON!(O)")
        p2 += 1
        main_win.o_score.setText("O\n" + str(p2))
        msg_box.exec()
        new_game()

    elif buttons[0][0].text()!="" and buttons[0][1].text()!="" and buttons[0][2].text()!="" and buttons[1][0].text()!="" and buttons[1][1].text()!="" and buttons[1][2].text()!="" and buttons[2][0].text()!="" and buttons[2][1].text()!="" and buttons[2][2].text()!="":
        msg_box = QMessageBox(text = "That's a Tie...")
        msg_box.exec()
        new_game()

def game_mode(mode):
    global pmode
    pmode = mode
    print(pmode)



def play(row,col):
    global player
    global draw
    global pmode

    r = random.randint(0,2)
    c = random.randint(0,2)
    if buttons[row][col].text() == "":
        if player == 1:
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("\
            QPushButton { \
                background-color: blue;\
                border-style: outset;\
                border-width: 1px;\
                border-color: rgb(0, 0, 0) ;\
                padding-top: 5px;\
                color: rgb(0, 0, 0);\
                border-radius: 5px;\
    }\
            QPushButton:hover {\
                background-color: rgb(0, 131, 197);\
    }\
            QPushButton:pressed {\
                background-color: rgb(0, 214, 103);\
                } font: GhostLike Demo; ")
            
            draw += 1
            if pmode == "pvc":
                while True:
                    r = random.randint(0,2)
                    c = random.randint(0,2)
                    if buttons[r][c].text() == "":
                        buttons[r][c].setText("O")
                        buttons[r][c].setStyleSheet("\
            QPushButton { \
                background-color: red;\
                border-style: outset;\
                border-width: 1px;\
                border-color: rgb(0, 0, 0) ;\
                padding-top: 5px;color: rgb(0, 0, 0);\
                border-radius: 5px;\
    }\
            QPushButton:hover {\
                background-color: red;\
    }\
            QPushButton:pressed {\
                background-color: rgb(0, 214, 103);\
                } font: GhostLike Demo; ")
                        break
            else:
                player = 2

        
        elif player == 2:
            if pmode == 'pvp':
                buttons[row][col].setText("O")
                buttons[row][col].setStyleSheet("\
            QPushButton { \
                background-color: red;\
                border-style: outset;\
                border-width: 1px;\
                border-color: rgb(0, 0, 0) ;\
                padding-top: 5px;\
                color: rgb(0, 0, 0);\
                border-radius: 5px;\
    }\
            QPushButton:hover {\
                background-color: rgb(0, 131, 197);\
    }\
            QPushButton:pressed {\
                background-color: rgb(0, 214, 103);\
                } font: GhostLike Demo; ")
            player = 1
            draw += 1
        check()



app = QApplication(sys.argv)

player = 1
loader = QUiLoader()
main_win = loader.load("Assignment18/mainwin.ui")
main_win.show()

buttons = [[main_win.btn_1, main_win.btn_2, main_win.btn_3],
           [main_win.btn_4, main_win.btn_5, main_win.btn_6],
           [main_win.btn_7, main_win.btn_8, main_win.btn_9]]


for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play,i,j))

main_win.btn_new.clicked.connect(new_game)
main_win.btn_pvp.clicked.connect(partial(game_mode,"pvp"))
main_win.btn_pvc.clicked.connect(partial(game_mode,"pvc"))
main_win.btn_about.clicked.connect(about)



app.exec()
