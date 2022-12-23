# Snake with characters(pro version).
# By Mahdi1Taheri

pattern = input("Enter your snake pattern with a space between them(exp: * # ==> *#*#*#*#*): ").split(" ")

n = int(input("length of your snake: "))

if len(pattern) == 2:
    for num in range(n):
        if num % 2 == 0:
            print(str(pattern[0]), end="")
        else:
            print(str(pattern[1]), end="")
else:
    print("NOTICE: please only write 2 characters with a space between them!")
    
    
