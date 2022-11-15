# Calculator
# by Mahdi Taheri
import mpmath
import math


# welcome message
print("Welcome to Mahdi Calculator!")

# mathematical operations funcs
def Add(Fnum, Lnum):
  return Fnum + Lnum

def Subtract(Fnum, Lnum):
  return Fnum - Lnum

def Divide(Fnum, Lnum):
  return Fnum / Lnum

def Multiply(Fnum, Lnum):
  return Fnum * Lnum 

def Sqrt(x):
  return math.sqrt(x)

def Sin(x):
  return math.sin(math.radians(x))

def Cos(x):
  return math.cos(math.radians(x))

def Tan(x):
  return math.tan(math.radians(x))

def Cot(x):
  return 1 / Tan(x)

def Factorial(x):
  return math.factorial(x)

# Mathematical operator selection section
print("1.Add")
print("2.Subtract")
print("3.Division")
print("4.Multiply")
print("5.Sqrt")
print("6.Sin")
print("7.Cos")
print("8.Tan")
print("9.Cot")
print("10.Factorial")
choice = input("Enter your choose(1/.../10): ")


# input section
if choice == "5" or "6" or "7" or "8" or "9" or "10":
  num = float(input("enter your number: "))
else:
  num1 = float(input("enter the first number: "))
  num2 = float(input("enter the second number: "))

# output section  
if choice == "1":
  print(num1, "+", num2, "=", Add(num1, num2))
elif choice == "2":
  print(num1, "-", num2, "=", Subtract(num1, num2))
elif choice == "3":
  print(num1, "/", num2, "=", Divide(num1, num2))
elif choice == "4":
  print(num1, "*", num2, "=", Multiply(num1, num2))
elif choice == "5":
  print("Square of", num, "is", Sqrt(num))
elif choice == "6":
  print("the sine value of", num ,"degrees is", round(Sin(num), 4))
elif choice == "7":
  print("The value of cosine of", num, "is", round(Cos(num), 4))
elif choice == "8":
  print("The value of tangent of", num, "is", round(Tan(num), 4))
elif choice == "9":
  print("The value of cotangent of", num, "is", round(Cot(num), 4))
elif choice == "10":
  print("The value of Factorial of", num, "is", Factorial(int(num)))
