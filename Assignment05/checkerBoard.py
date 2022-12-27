# This program receives the n and m parameters and prints the checkerboard with n and m dimensions.
n = int(input("Enter the length: "))
m = int(input("Enter the width: "))

def gen(n,m):
    for num in range(n):
        if num % 2 == 0:
            print("#", end= "")
        else:
            print("*", end="")
    
    for row in range(m-1):
        print('\n', end= "")
        if row % 2 == 0:
            for num in range(n):
                if num % 2 == 0:
                    print("*", end= "")
                else:
                    print("#", end="")
        else:
            for num in range(n):
                if num % 2 == 0:
                    print("#", end= "")
                else:
                    print("*", end="")
    
gen(n,m)

