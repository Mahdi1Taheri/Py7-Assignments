import qrcode

user_name =  input("Please enter your name with a space between first name and last name to create a QRcode: ")
user_number = int(input("Please enter your phone number: ")) 

data = []

data.append(user_name)

if type(user_number) == int:
    user_number = str(user_number)
    data.append(user_number)
else:
    print("please enter integer!")

lst = '\n'.join(''.join(l) for l in data)

img = qrcode.make(lst)
img.save('user_data.png')
