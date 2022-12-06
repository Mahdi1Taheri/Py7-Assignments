side = int(input("Enter the side of diamond: "))

for i in range(side):
    print((side - i) * " ",(2 * i + 1) * "*")
for i in range(side - 2, -1, -1):
    print((side - i) * " ",(2 * i + 1) * "*")
