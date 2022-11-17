# This program calculates at the moment and after entering any number, it displays the average up to that moment.

print("*NOTICE: if you wanna exit from this program, write 'exit'.")

# To count the number of numbers
how_many = 0

# to save all entered numbers
lst = []

while True:
    grade = input("Enter your grade: ")
    how_many += 1

    if grade == "exit":
        break

    grade = float(grade) 
    lst.append(grade)

    if how_many >= 2:
        print("Average scores so far: ", round(sum(lst) / how_many, 2))
    
    


