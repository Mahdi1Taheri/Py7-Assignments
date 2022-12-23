import random

dice = random.randint(1,7)
print(dice)

while True:
    continu = input("Do you wanna roll the dice again?(yes/no): ")

    if continu == "yes":
        dice = random.randint(1,7)
        print(dice)
    else:
        break

    if dice == 6:
        dice = random.randint(1,7)
        print("your first gift: ",dice)
        dice = random.randint(1,7)
        print("your second gift: ",dice)
