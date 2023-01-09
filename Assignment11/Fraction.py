from math import gcd

class Fraction:
    def __init__(self,ss,mm):
        # properties
        self.s = ss
        self.m = mm

    
    # Methods
    def multiply(self,other): # ضرب کسر
        result_s = self.s * other.s
        result_m = self.m * other.m
        x = Fraction(result_s,result_m)
        return x
    
    def division(self,other): # تقسیم کسر
        result_s = self.s * other.m
        result_m = self.m * other.s
        x = Fraction(result_s,result_m)
        return x
    
    def sum(self,other): # جمع کسر
        s = self.s * other.m + self.m * other.s
        m = self.m * other.m
        x = Fraction(s,m)
        return x

    
    def subtraction(self,other): # تفریق کسر
        s = self.s * other.m - self.m * other.s
        m = self.m * other.m
        x = Fraction(s,m)
        return x

    def convert_to_num(self):
        if self.s / self.m % 2 or 3 or 5 or 7 or 11 or 13 == 0:
            print(self.s // self.m)
        else:
            print("Can not convert the Fraction to a number")

    def reduce(self):
        d = gcd(self.s, self.m)
        x = self.s // d
        y = self.m // d
        print(x,"/", y)

    def show(self): 
        print(self.s, "/", self.m)

a = Fraction(8,2)
b = Fraction(9,3)

z = a.sum(b)
z.show()
