class Person:
    def __init__(self,a,b,c,d,e):
        # properties
        self.name = a
        self.age = b
        self.height = c
        self.city = d
        self.eye_color = e

    # methods
    def sleep(self):
        ...
    def walk(self):
        ...
    def marry(self):
        ...
    def programing(self):
        ...
    def study(self):
        ...
    def eat(self):
        ...

my_friend = Person("ali",30,170,"shiraz","blue")
my_sister = Person("bahare",22,165,"neyshabour","black")
my_boss = Person("mamad",45,172,"mashad","black")

print(my_friend.__dir__)
print(my_friend)

my_friend.eat()
my_sister.eat()
my_boss.eat()

my_friend.programing()
my_boss.programing()

print(my_sister.name)