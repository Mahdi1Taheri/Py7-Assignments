# Hangman Game.(or guess the word)
import random

word_bank = ["earth","moon", "woman", "life", "freedom", "love", "soul", "music", "anime"]
word = random.choice(word_bank)

list_true = ''
mistakes = 0


while True:
    for i in range(len(word)):
        if word[i] in list_true:
            print(word[i], end="")
        else:
            print("_", end= " ")

    user = input("\nEnter your guess(ONLY ONE LETTER): ").lower()
    if len(user) == 1:
        if user in word:
            list_true += user
            print("Correct!")
        else:
            print("wrong!")
            mistakes += 1
    else:
        print("NOTICE: just one letter!")

    if mistakes == 6:
        break
    elif list_true == word:
        print("you win!!")
        print("The word was ", word)
        break
    
    
        
    



    
    
    
    
