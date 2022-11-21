# Project name: Educational status

# Project description: This program receives the student's first and last name 
# and after calculating the student's grade point average,
# prints the student's academic status in the output.

# receving Firstname, Lastname and grade of three lessons.

Fname = input("Enter your First name: ")
Lname = input("Enter your Last name: ")
grade1 = float( input("Enter your First grade: "))
grade2 = float(input("Enter your second grade: "))
grade3 = float(input("Enter your third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("_average > 17: status Great")
print("_ 12 < average => 17: status Normal")
print("_average < 17: status Fail")
print("------------------------")
print(Fname,"", Lname, end= "\n")
print(round(average, 2))
if average > 17:
    print("your grade status is Great!")
elif average > 12 and average <= 17:
    print("your grade status is Normal")
elif average < 12:
    print("your grade status is bulshit...")
