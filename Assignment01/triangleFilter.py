# triangle filter
#----------------
# A program that
# receives the size of three sides of a triangle 
# and determines whether it is possible to draw such a triangle or not

# receiving the size of three sides.
side1 = float(input("Enter the size of the side 1: "))
side2 = float(input("Enter the size of the side 2: "))
side3 = float(input("Enter the size of the side 3: "))

if side1 > (side2 + side3):
    print("*it is NOT possible to draw this triangle*")
elif side2 > (side1 + side3):
    print("*it is NOT possible to draw this triangle*")
elif side3 > (side1 + side2):
    print("*it is NOT possible to draw this triangle*")
else:
    print("it is possible to draw this triangle")


