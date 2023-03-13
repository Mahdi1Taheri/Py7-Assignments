from termcolor import colored
import qrcode
import sqlite3

cart = []
def load_db():
    global connection
    global cursor
    connection= sqlite3.connect("store_db.db")
    cursor = connection.cursor()


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
    id = input(colored("enter product's code: "))
    name = input(colored("enter product's name: "))
    price = input(colored("enter product's price: "))
    count = input(colored("enter product's count: "))
    connection.commit()
    new_product = cursor.execute(f'INSERT INTO products(id,name,price,count) VALUES({id},{name},{price},{count})')
    print(colored("done succsesfuly","green"))
    
 
def edit():
    global all
    all = cursor.execute("SELECT id,name,price,count FROM products")
    pr_id = input(colored("Enter Product's code: ","yellow"))
    
    if pr_id == cursor.execute(f"SELECT id FROM products"):
        print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
        print(cursor.execute("SELECT id,name,price,count FROM products"))
        print(colored("1.Name","yellow"))
        print(colored("2.Price","yellow"))
        print(colored("3.Count","yellow"))

        edit_choice = input(colored("Which item do you want to edit?: ","yellow"))

        if edit_choice == "1":
            new_name = input("Enter new product's name: ")
            cursor.execute(f"INSERT INTO products(name) VALUES({new_name})")
            print(colored(f"Product's name changed to {new_name}","green"))
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            all.fetchall()
            connection.commit()
            
        elif edit_choice == "2":
            new_price = input("Enter new product's price: ")
            cursor.execute(f"INSERT INTO products(price) VALUES({new_price})")
            print(colored(f"Product's price changed to {new_price}","green"))
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            all.fetchall()
            connection.commit()
                
        elif edit_choice == "3":
            new_count = input("Enter new product's count: ")
            cursor.execute(f"INSERT INTO products(count) VALUES({new_count})")
            print(colored(f"Product's count changed to {new_count}","green"))
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            all.fetchall()
            connection.commit()
                          
    else:
        print(colored("The Product's code is wrong.","red"))
    
 
    

def remove():
    pr_id = input("enter product's code: ")
    for data in cursor.execute("SELECT * FROM products"):
        if pr_id == cursor.execute(f"SELECT id FROM products"):
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            all.fetchall()
            break
        else:
            print(colored("Product's code is wrong!","red"))
            break

    sure = input(colored("Are you sure to remove this product?(y/n): ","yellow"))

    if sure == "y":
        for data in cursor.execute("SELECT * FROM products"):
            cursor.execute(f"DELETE FROM products WHERE id = {pr_id}")
            connection.commit()
            show_list()
            break
    else:
        exit()
  

def search():
    user_input = input("Type to search: ")
    for data in cursor.execute(f"SELECT * FROM products WHERE id = {user_input} OR name = {user_input}"):
        print(data)
    else:
        print("NOT FOUND")

def show_list():
    print("Code\tName\tPrice")
    for data in cursor.execute("SELECT * FROM products"):
        print(data)

def buy():
    global cart
    while True:
        print(colored("*NOTICE: if you wanna exit, write exit.","yellow"))
        id = input("Enter the Product's code: ").upper()
        for data in cursor.execute("SELECT * FROM products"):
            if data == id:
                many = int(input("how many products do you want? "))
                count = cursor.execute(f"SELECT count FROM products WHERE id = {id}")
                int(count.fetchone())
                
                if many <= count:
                    result = count =- many
                    cursor.execute(f"UPDATE products SET count = {result} WHERE id = {id}")
                    
                    cart += ["id: " + data["id"],"| name: " + data["name"], "| price: " + data["price"], f"| count: {many}","\n"]
                    print(colored("Product added to your cart.","green"))
                    print("your Cart=> ",*cart)
                    break
                else:
                    print(colored("Insufficient inventory","red"))
                    exit()
            elif id == "EXIT":
                exit()
        else:
            print(colored("NOT FOUND","red"))
        


def qrc():
    pr_code = input("enter product's code: ")
    for data in cursor.execute("SELECT * FROM products"):
        if pr_code == cursor.execute("SELECT id FROM products"):
            print("Code\tName\tPrice")
            i = cursor.execute(f"SELECT id,name,price WHERE id = {pr_code}")
            i.fetchone()
            img = qrcode.make(i)
            img.save(f"P{pr_code}.png")
            print(colored("done successfully!","green"))

print("Welcome to Mahdi Store.")
print("Loading...")
load_db()
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
        exit(0)
    else:
        print(colored("*NOTICE: your choosen number should be between 1 and 8.","red"))
