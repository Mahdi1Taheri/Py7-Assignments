import gtts
from termcolor import colored
import re

def read_from_file():
    global word_bank

    f = open("Assignment8/words.txt",'r')
    temp = f.read().split("\n")
    word_bank = []

    for i in range(0, len(temp), 2):
        my_dict = {'en': temp[i], 'fa': temp[i + 1]}
        word_bank.append(my_dict)
    f.close()

read_from_file()
def translate_en_per():
    userE_text = input("enter your english text: ").lower()
    user_words = userE_text.split(" ")

    output = ""
    for user_word in user_words :
        for word in word_bank :
            if user_word == word["en"] :
                output = output + colored(word["fa"],"green") + " "
                break
        else :
            output = output + colored(user_word,"yellow") + " "

    print(colored(output + ".","green"))


def translate_per_en():
    userE_text = input("Enter your Persian text: ").lower()
    user_words = userE_text.split(" ")

    output = ""
    for user_word in user_words :
        for word in word_bank :
            if user_word == word["fa"]:
                output = output + word["en"] + " "
                break
        else :
            output = output + user_word + " "

    print(colored(output + ".","green"))
    
    sound2 = gtts.gTTS(output , lang = "en" , slow = False )
    sound2.save("Assignment8/EN_Voice.mp3")

def add_word():
    en = input('Enter new English word: ')
    fa = input(f'what does {en} mean? ')
    for word in word_bank:
        if en in word["en"]:
            print(colored("this word is available in dictionary.","red"))
            break
    else:
        my_dict = {'en': en, 'fa': fa}
        word_bank.append(my_dict)
        print(colored("your new word successfully added.","green"))

def write_to_db():
    open('Assignment8/words.txt', 'w').close()
    f = open('Assignment8/words.txt', 'a')
    for word in word_bank:
        f.write(word['en'] + "\n" + word['fa'] + "\n")
    f.close()

while True:
    print("1. Persian to English")
    print("2. English to Persian")
    print("3. Add new word")
    print(colored("*NOTICE: if you wanna exit from the program, write 'exit'.","yellow"))
    choice = input("Enter Translate mode(1/2/exit): ").lower()
    if choice == "1":
        translate_per_en()
        print()
    elif choice == "2":
        translate_en_per()
        print()
    elif choice == "3":
        add_word()
        print()
    elif choice == "exit":
        write_to_db()
        break
    else:
        print(colored("*NOTICE: your choice should be between 1 to 3.","red"))