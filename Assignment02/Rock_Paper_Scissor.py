# Rock Paper Scissor Game.
import random

print("*NOTICE: if you wanna close the game, write 'exit'.")

# user and computer score
user_score = 0
computer_score = 0

# number of times played
number_of_play = 0

while user_score <= 5 or computer_score <= 5:

    # computer choice
    words = ["rock", "paper", "scissor"]
    computer = random.choice(words)
    # user choice
    user = input("Enter your move: ").lower()
    print("computer: ",computer)
    number_of_play += 1

    if user == "exit":
        print("you played ", number_of_play," times.")
        break

    if user not in words:
        print("please enter the correct word(rock/paper/scissor)!")
        break
    
    # Compare the user's move and the computer's move and determine the winner
    if user == computer:
        print("Tied...")

    elif user == "rock":
        if computer == "scissor":
            print("user win!")
            user_score += 1
        else:
            print("computer win!")
            computer_score += 1
    
    elif user == "paper":
        if computer == "rock":
            print("user win!")
            user_score += 1
        else: 
            print("computer win!")
            computer_score += 1
    
    elif user == "scissor":
        if computer == "paper":
            print("user win!")
            user_score += 1
        else:
            print("computer win!")
            computer_score += 1 
    
    # showing the scores
    print("computer: ", computer_score, "| user: ", user_score)

    # end section
    if computer_score == 5:
        print("*you loose...*")
        break
    elif user_score == 5:
        print("*hooraa!! you win!!")
        break
