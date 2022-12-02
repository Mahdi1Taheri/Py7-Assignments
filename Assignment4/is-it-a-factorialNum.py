import math

num = int(input("enter your number to check: "))

lst = []
for number in range(100):
    fac = math.factorial(number)
    lst.append(fac)

if num in lst:
    print("yes")
else:
    print("no")