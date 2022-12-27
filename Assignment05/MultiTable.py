# This program receives two parameters n and m from the user and prints a multiplication table with dimensions n and m.

n = int(input("Enter the height of the table: "))
m = int(input("Enter the width of the table: "))

def multi(n,m):

    print("  ",end='')
    for t in range(1,n + 1):
        print("    ", end="")
        print("%1d" % t, end='')
    print()
    for num in range(1,m + 1):
        print("%2d| " % num, end="")
        for num1 in range(1, n + 1):
            print("%3d  " % (num*num1), end="")
        print()

multi(n,m)
