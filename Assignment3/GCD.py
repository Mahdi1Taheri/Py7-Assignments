# GCD

firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter te second number: "))

while firstNum != secondNum:
	if firstNum > secondNum:
		firstNum -= secondNum
	else:
		secondNum -= firstNum

print ("\nThe GCD number is: ", firstNum)