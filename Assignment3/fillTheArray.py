import random

n = int(input("How many number in a list? "))
range1 = int(input("Enter the range of numbers: "))

lst = []

for i in range(0,n):
    c = random.randint(0,range1)
    lst.append(c)

print(lst)