class MyTime:
    def __init__(self,h,m,s):
        self.hour = h
        self.minute = m
        self.second = s

    def plus(self):
        self.second = int(self.second) + 1
        self.fix()

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = MyTime(h_new,m_new,s_new)
        return result

    def sub_sec(self):
        self.second = int(self.second) - 1
        self.fix()

    def sub(self,other):
        s_new = int(self.second) - other.second
        m_new = int(self.minute) - other.minute
        h_new = int(self.hour )- other.hour
        self.fix()
        result = MyTime(h_new,m_new,s_new)
        return result
    
    def same_time(self, other):
        if self.hour == other.hour and self.min == other.min:
            return True
        else:
            return False
        
    def fix(self):
        while int(self.second) >= 60:
            self.second -= 60
            self.minute = int(self.minute) + 1

        while int(self.minute) >= 60:
            self.minute = int(self.minute) - 60
            self.hour = int(self.hour) + 1

        while int(self.hour) >= 24:
            self.hour = int(self.hour) - 24

        while int(self.second) < 0:
            self.second = int(self.second) - 60
            self.minute = int(self.minute) -  1

        while int(self.minute) < 0:
            self.minute = int(self.minute) + 60
            self.hour = int(self.hour) + 1
            
        while int(self.hour) < 0:
            self.hour = int(self.hour) + 24
        
    def sec_to_time(self):
        sec = self.second + 60
        sec_hour = sec // 3600
        sec_minute = (sec % 3600) // 60 
        second = (sec % 3600) % 60
        print(sec_hour,":",sec_minute,":",second)

    def time_to_sec(self):
        hour_sec = self.hour * 3600
        minute_sec = self.minute * 60
        print(hour_sec + minute_sec + self.second ,"sec")

    def gmt_to_teh(self):
        t = MyTime(3,30,0)
        teh = self.sum(t)
        return teh 

    def minus(self):
        self.second -= 1 