from termcolor import colored
import qrcode

PRODUCTS = []
cart = []

def read_db():
    global f
    f = open("database.txt","r")

    for line in f:
        result = line.rstrip("\n").split(',')
        my_dict = {"code": result[0], "name": result[1], "price": result[2],"count": result[3]}
        PRODUCTS.append(my_dict)
    
    f.close() 

def write_db():
    f = open("database.txt",'w')
    for product in PRODUCTS:
        f.write(product['code']+',')
        f.write(product['name']+',')
        f.write(product['price']+',')
        f.write(product['count']+ "\n")
    f.close()


def show_menu():
    print(colored("Choose:","yellow"))
    print(colored("1.Add","yellow"))
    print(colored("2.Edit","yellow"))
    print(colored("3.Remove","yellow"))
    print(colored("4.Search","yellow"))
    print(colored("5.Show List","yellow"))
    print(colored("6.Buy","yellow"))
    print(colored("7.Product's QR code","yellow"))
    print(colored("8.Exit","yellow"))

def add():
    code = input(colored("enter product's code: "))
    name = input(colored("enter product's name: "))
    price = input(colored("enter product's price: "))
    count = input(colored("enter product's count: "))
  
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    print(colored("done succsesfuly","green"))
    PRODUCTS.append(new_product)
 
def edit():
    pr_code = input(colored("Enter Product's code: ","yellow"))
    for product in PRODUCTS:
        if pr_code == product["code"]:
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            print(product["code"],"\t\t", product["name"],"\t\t", product["price"],"\t\t", product["count"])
            print(colored("1.Name","yellow"))
            print(colored("2.Price","yellow"))
            print(colored("3.Count","yellow"))
            edit_choice = input(colored("Which item do you want to edit?: ","yellow"))
            if edit_choice == "1":
                product["name"] = input("Enter new product's name: ")
                print(colored("Product's name changed!","green"))
                print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
                print(product["code"],"\t\t", colored(product["name"],"green"),"\t\t", product["price"],"\t\t", product["count"])
                break
            elif edit_choice == "2":
                product["price"] = input("Enter new product's price: ")
                print(colored("Product's price changed!","green"))
                print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
                print(product["code"],"\t\t", product["name"],"\t\t", colored(product["price"],"green"),"\t\t", product["count"])
                break
            elif edit_choice == "3":
                product["count"] = input("Enter new product's count: ")
                print(colored("Product's count changed!","green"))
                print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
                print(product["code"],"\t\t", product["name"],"\t\t", product["price"],"\t\t", colored(product["count"],"green"))
                break            
    else:
        print(colored("The Product's code is wrong.","red"))
 
    

def remove():
    pr_code = input("enter product's code: ")
    for product in PRODUCTS:
        if pr_code == product["code"]:
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            print(product["code"],"\t\t", product["name"],"\t\t", product["price"],"\t\t", product["count"])
            break
        else:
            print(colored("Product's code is wrong!","red"))
            break

    sure = input(colored("Are you sure to remove this product?(y/n): ","yellow"))

    if sure == "y":
        for product in PRODUCTS:
            if pr_code == product["code"]:
                PRODUCTS.remove(product)
                show_list()
                break
    else:
        exit()
  

def search():
    user_input = input("Type to search: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            break
    else:
        print("NOT FOUND")

def show_list():
    print("Code\tName\tPrice")
    for product in PRODUCTS:
        print(product["code"], "\t", product["name"], "\t", product["price"])

def buy():
    global cart
    while True:
        print(colored("*NOTICE: if you wanna exit, write exit.","yellow"))
        code = input("Enter the Product's code: ").upper()
        for product in PRODUCTS:
            if product["code"] == code:
                many = int(input("how many products do you want? "))
                count = int(product["count"])
                if many <= count:
                    result = count =- many
                    product["count"] = result
                    cart += ["code: " + product["code"],"| name: " + product["name"], "| price: " + product["price"], f"| count: {many}","\n"]
                    print(colored("Product added to your cart.","green"))
                    print("your Cart=> ",*cart)
                    break
                else:
                    print(colored("Insufficient inventory","red"))
                    exit()
            elif code == "EXIT":
                exit()
        else:
            print(colored("NOT FOUND","red"))
        


def qrc():
    pr_code = input("enter product's code: ")
    for product in PRODUCTS:
        if pr_code == product["code"]:
            print("Code\tName\tPrice")
            print(product["code"], "\t", product["name"], "\t", product["price"])
            data = product["code"],product["name"], product["price"],product["count"]
            img = qrcode.make(data)
            img.save(product["code"]+"P.png")
            print(colored("done successfully!","green"))

print("Welcome to Mahdi Store.")
print("Loading...")
read_db()
print("Data loaded.")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        qrc()
    elif choice == 8:
        write_db()
        exit(0)
    else:
        print(colored("*NOTICE: your choosen number should be between 1 and 7.","red"))

