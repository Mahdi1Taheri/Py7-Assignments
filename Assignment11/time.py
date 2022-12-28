class Time:
    def __init__(self,hh,mm,ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()
    
    def show(self):
        print(self.hour,":",self.minute,":",self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new,m_new,s_new)
        return result

    def sub(self,other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new,m_new,s_new)
        return result

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.second < 0:
            self.minute += 60
            self.hour -= 1
        
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
        t = Time(3,30,0)
        teh = self.sum(t)
        return teh
        

tm = Time(11,0,0)
l = tm.gmt_to_teh()

l.show()

