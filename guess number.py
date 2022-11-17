# Guess Number Game.
import random


# making a random number
computer_num = random.randint(1,21)
print("if you wanna exit from the game, write 'exit'.")

# Variable to count the number of user guesses
number_of_guess = 0

while number_of_guess < 6:
    # input section
    user_num = input("Enter your guess: ")
    # close game section
    if user_num == "exit":
        break

    user_num = int(user_num)
    # Comparing the user's guess with the computer's number
    if user_num == computer_num:
        number_of_guess += 1
        print("YAY! you win!!🎉🎉")
        print("Number of times you guessed: ", number_of_guess)
        break
    elif user_num < computer_num:
        number_of_guess += 1
        print("Guess a bigger number")
    elif user_num > computer_num:
        number_of_guess += 1
        print("Guess a smaller number5")
if number_of_guess >= 5:
    print("you didn't guessed the number, the number was", computer_num)
        



