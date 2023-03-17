from termcolor import colored
import qrcode
import sqlite3

cart = []
def load_db():
    global connection
    global cursor
    connection= sqlite3.connect("Assignment21\store\store_db.db")
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
    Id = input(colored("enter product's code: "))
    Name = input(colored("enter product's name: "))
    Price = input(colored("enter product's price: "))
    Count = input(colored("enter product's count: "))
    cursor.execute(f"INSERT INTO products(id,name,price,count) VALUES('{Id}','{Name}','{Price}','{Count}')")
    connection.commit()
    print(colored("done succsesfuly","green"))
    
 
def edit():
    global all
    all = cursor.execute("SELECT id,name,price,count FROM products")
    pr_id = int(input(colored("Enter Product's code: ","yellow")))
    selectid = cursor.execute(f"SELECT id FROM products")
    id = int(selectid.fetchone()[0])

    print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
    for data in cursor.execute(f"SELECT * FROM products WHERE id = '{id}'"):
        print(data)
    
    if pr_id == int(id):
        print(colored("1.Name","yellow"))
        print(colored("2.Price","yellow"))
        print(colored("3.Count","yellow"))

        edit_choice = input(colored("Which item do you want to edit?: ","yellow"))

        if edit_choice == "1":
            new_name = input("Enter new product's name: ")
            cursor.execute(f"UPDATE products SET name = '{new_name}' WHERE id == {pr_id}")
            connection.commit()
            print(colored(f"Product's name changed to {new_name}","green"))
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            all.fetchall()
            
            
        elif edit_choice == "2":
            new_price = input("Enter new product's price: ")
            cursor.execute(f"UPDATE products SET price = '{new_price}' WHERE id == {pr_id}")
            connection.commit()
            print(colored(f"Product's price changed to {new_price}","green"))
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            all.fetchall()
            
                
        elif edit_choice == "3":
            new_count = input("Enter new product's count: ")
            cursor.execute(f"UPDATE products SET count = '{new_count}' WHERE id == {pr_id}")
            connection.commit()
            print(colored(f"Product's count changed to {new_count}","green"))
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            all.fetchall()
            
                          
    else:
        print(colored("The Product's code is wrong.","red"))
    connection.commit()
    
 
    

def remove():
    pr_id = input("enter product's code: ")
    selectid = cursor.execute(f"SELECT id FROM products WHERE id == {pr_id}")
    id = int(selectid.fetchone()[0])
    for data in cursor.execute(f"SELECT * FROM products WHERE id == {pr_id}"):
            print(colored("Code\t\tName\t\tPrice\t\tCount","yellow"))
            print(data)
            break
        

    if int(pr_id) == id:
        sure = input(colored("Are you sure to remove this product?(y/n): ","yellow"))

        if sure == "y":
            for data in cursor.execute("SELECT * FROM products"):
                cursor.execute(f"DELETE FROM products WHERE id = {pr_id}")
                connection.commit()
                print(colored("succesfully removed!","green"))
                show_list()
                break
        else:
            exit()
    else:
        print(colored("Product's code is wrong!","red"))
        exit()
  

def search():
    user_input = input("Type name or id to search: ")
    for data in cursor.execute(f"SELECT * FROM products WHERE id == '{user_input}' OR name == '{user_input}'"):
        print(data)

def show_list():
    print("Code\tName\tPrice\tCount")
    for data in cursor.execute("SELECT * FROM products"):
        print(data)

def buy():
    global cart
    
    print(colored("*NOTICE: if you wanna exit, write exit.","yellow"))

    pr_id = input("Enter the Product's code: ").upper()
    selectid = cursor.execute(f"SELECT id FROM products WHERE id == {pr_id}")
    id = int(selectid.fetchone()[0])

    for data in cursor.execute(f"SELECT * FROM products WHERE id == '{id}'"):
        print(data)
    if int(pr_id) == id:
        many = int(input("how many products do you want? "))
        count = cursor.execute(f"SELECT count FROM products WHERE id = {id}")
        count2 = int(count.fetchone()[0])
        n = cursor.execute(f"SELECT name FROM products WHERE id == {id}")
        name = n.fetchone()[0]
        p = cursor.execute(f"SELECT price FROM products WHERE id == {int(id)}")
        price = int(p.fetchone()[0])
                
        if many <= count2:
            result = count2 - many
            cursor.execute(f"UPDATE products SET count = {result} WHERE id = {id}")
            connection.commit()
            cursor.execute(f"INSERT INTO cart(id,name,price,count) VALUES('{id}','{name}','{price}','{count2}')")
            connection.commit()
            print(colored("Product added to your cart.","green"))
            exit(0)
        else:
            print(colored("Insufficient inventory","red"))
            exit()
    elif id == "EXIT":
        exit()
    
        


def qrc():
    pr_id = input("enter product's code: ")
    selectid = cursor.execute(f"SELECT id FROM products WHERE id == {pr_id}")
    id = int(selectid.fetchone()[0])
    for data in cursor.execute("SELECT * FROM products"):
        if int(pr_id) == id:
            print("Code\tName\tPrice")
            i = cursor.execute(f"SELECT id,name,price FROM products WHERE id = {pr_id}")
            info = i.fetchone()
            img = qrcode.make(info)
            img.save(f"P{pr_id}.png")
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
