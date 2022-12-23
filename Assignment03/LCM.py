firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter te second number: "))

multi = firstNum * secondNum

while firstNum != secondNum:
	if firstNum > secondNum:
		firstNum -= secondNum
	else:
		secondNum -= firstNum

print ("\nThe LCM number is: ", multi / firstNum)
