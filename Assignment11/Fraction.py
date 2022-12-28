from math import gcd

class Fraction:
    def __init__(self,ss,mm):
        # properties
        self.s = ss
        self.m = mm

    
    # Methods
    def multiply(self,Kasr1,Kasr2): # ضرب کسر
        result_s = Kasr1.s * Kasr2.s
        result_m = Kasr1.m * Kasr2.m
        x = Fraction(result_s,result_m)
        return x
    
    def division(self,Kasr1,Kasr2): # تقسیم کسر
        result_s = Kasr1.s * Kasr2.m
        result_m = Kasr1.m * Kasr2.s
        
        x = Fraction(result_s,result_m)
        return x
    
    def sum(self,K1,K2): # جمع کسر
        s = K1.s * K2.m + K1.m * K2.s
        m = K1.m * K2.m
        x = Fraction(s,m)
        return x

    
    def subtraction(self,K1,K2): # تفریق کسر
        s = K1.s * K2.m - K1.m * K2.s
        m = K1.m * K2.m
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







    