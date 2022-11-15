# BMI prtoject
# BMI = weight / height ** 2

# receiving weight and height.

w = float(input("Enter your weight(kg): "))
h = float(input("Enter your height(meter): "))

BMI = round(w / (h/100)**2,3)

print("your BMI is ",BMI)

if BMI < 18.5:
    print("You are a thin person and you need to gain a little more weight to reach the normal level.")
elif BMI in range(18.5, 24.9):
    print("your weight is normal, Bravo!")
elif BMI in range(25, 29.9):
    print("You are a little overweight and it is better to lose your weight to reach the normal level.")
elif BMI in range(30, 34.9):
    print("You are a fat person and this obesity will be harmful to your body.\n With a little effort, you can reach the normal level and remove yourself from danger.")
elif BMI in range(35, 39.9):
    print("Your body is very fat and will face irreparable risks in the not too distant future.\n You have to work hard to keep your body healthy and lose weight!")