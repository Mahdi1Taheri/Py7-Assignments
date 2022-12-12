# Tic Tac Toe Game.
from termcolor import colored
import pyfiglet

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
        if board[i] == [x,x,x]:
            print("Player 1[X] wins!")
        elif board[i] == [o,o,o]:
            print("Player 2[O] wins!")
            return True
    
    if board[0][0] == board [1][0] == board[2][0] == x:
        print("Player 1[X] win!")
        return True

    elif board[0][1] and board[1][1] and board[2][1] == x:
        print("Player 1[X] win!")
        return True

    elif board[0][2] and board[1][2] and board[2][2] == x:
        print("Player 1[X] win!")
        return True

    elif board[0][0] and board [1][0] and board[2][0] == o:
        print("Player 2[O] win!")
        return True

    elif board[0][1] and board[1][1] and board[2][1] == o:
        print("Player 2[O] win!")
        return True

    elif board[0][2] and board[1][2] and board[2][2] == o:
        print("Player 2[O] win!")
        return True

    elif board[0][0] and board[1][1] and board[2][2] == x:
        print("Player 1[X] win!")
        return True
        
    elif board[0][0] and board[1][1] and board[2][2] == o:
        print("Player 2[O] win!")
        return True
    
    else:
        if draw == 9:
            print("draw...")
            return True
        
# printing the GameBoard.

show_board()
while True:
    print("Player 1")

    while True:
        row = int(input("please enter row : "))
        col =  int(input("please enter col : "))
        draw += 1
        if 0 <= row <= 2 and 0 <= col <= 2 :
            if board[row][col] == "_":
                board[row][col] = colored("X","red")
                break
            else:
                print( "This house has already been selected, please try again . . .")
        else:
                print(" The selected number must be between 0 and 2 \n Please try again . . .")          
    show_board()
    if check_game() == True:
        break

    print("Player 2")
    
    while True:
        row = int(input("please enter row : "))
        col = int(input("please enter col : "))
        draw += 1
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == "_":
                    board[row][col] = colored("O","blue")
                    break
            else:
                 print("this place is full, try another place.")
        else:
                 print("please enter the number between 0 to 2.")     
    show_board()
    check_game()