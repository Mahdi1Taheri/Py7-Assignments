# Tic Tac Toe Game.
from termcolor import colored
import pyfiglet
import random
import time

# جينگيل پينگيل بازي
title = pyfiglet.figlet_format("TicTacToe", font='slant')
print(colored(title, 'green'))
print(colored("*NOTICE: Any player who can capture a complete line is the winner!", 'yellow'))

o = colored('O', 'blue')
x = colored('X','red')
draw = 0

board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

def show_board():
    for row in board:
        print(*row)
    print()

def check_game():
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == x:
            print("Player 1[X] win!")
            return True
        elif board[0][i] == board[1][i] == board[2][i] == o:
            print("Player 2[O] win!")
            return True
    
    if board[0][0] == board [1][0] == board[2][0] == x:
        print("Player 1[X] win!")
        return True

    elif board[0][1] == board[1][1] == board[2][1] == x:
        print("Player 1[X] win!")
        return True

    elif board[0][2] == board[1][2] == board[2][2] == x:
        print("Player 1[X] win!")
        return True

    elif board[0][0] == board[1][0] == board[2][0] == o:
        print("Player 2[O] win!")
        return True

    elif board[0][1] == board[1][1] == board[2][1] == o:
        print("Player 2[O] win!")
        return True

    elif board[0][2] == board[1][2] == board[2][2] == o:
        print("Player 2[O] win!")
        return True

    elif board[0][0] == board[1][1] == board[2][2] == x:
        print("Player 1[X] win!")
        return True
        
    elif board[0][0] == board[1][1] == board[2][2] == o:
        print("Player 2[O] win!")
        return True
    
    else:
        if draw == 9:
            print("draw...")
            return True
        
user = int(input("Player VS Player or Player VS Computer?(1/2): "))
show_board()

if user == 1:
    start = time.time()
    while True:
        print("Player 1")
        if check_game() == True:
            break
        while True:
            row = int(input("please enter row : "))
            col =  int(input("please enter col : "))
            draw += 1
            if 0 <= row <= 2 and 0 <= col <= 2 :
                if board[row][col] == "_":
                    board[row][col] = x
                    break
                else:
                    print("this place is full, try another place.")
            else:
                    print("please enter a number between 0 to 2.")   
            if check_game() == True:
                break       
        show_board()
        if check_game() == True:
            end = time.time()
            print(f"Playing Time: {round(end - start , 2)}sec")
            break

        print("Player 2")
        
        while True:
            row = int(input("please enter row : "))
            col = int(input("please enter col : "))
            draw += 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == "_":
                        board[row][col] = o
                        break
                else:
                    print("this place is full, try another place.")
            else:
                    print("please enter the number between 0 to 2.")     
        show_board()
        if check_game() == True:
            end = time.time()
            print(f"Playing Time: {round(end - start , 2)}sec")
            break
        
elif user == 2:
    while True:
        start = time.time()
        print("Player 1")
        if check_game() == True:
            break
    
        while True:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if 0 <= row <= 2 and  0 <= col <= 2:
                if board[row][col] == "_":
                    board[row][col] = x
                    break
                else:
                    print("this place is full, try another place.")
            else:
                print("please enter a number between 0 to 2.")
        show_board()
        if check_game() == True:
            end = time.time()
            print(f"Playing Time: {round(end - start , 2)}sec")
            break

        print("Computer")
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if board[row][col] == "_":
                board[row][col] = o
                break
            else:
                print("select another row and col")
                continue
        show_board()
        if check_game() == True:
            end = time.time()
            print(f"Playing Time: {round(end - start , 2)}sec")
            break
