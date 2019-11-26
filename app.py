from datetime import datetime

class Person:
    def __init__(self,name):
        self.name = name
        self.user_time = 0
        self.user_speed = 0
        self.total_miles = 0
        super().__init__()
    
    def myfunc(self):
        print("Hello my name is " + self.name)

    # get time difference
    def diff(self,startTime, endTime):
        FMT = '%H:%M'
        tdelta = datetime.strptime(endTime, FMT) - datetime.strptime(startTime, FMT)
        
        hours,remainder = divmod(tdelta.seconds,3600)
        mintues,seconds = divmod(remainder,60)
        time = hours + (mintues/100)
        self.user_time = self.user_time + time
        return time

    #format time difference into a decimal
    def hours(self, td):
        hours,remainder = divmod(td.seconds,3600)
        mintues, seconds = divmod(remainder,60)
        time = hours + (mintues/100)
        return time

    #miles per hour

    def speed(self, distance,time):
        mph = distance/time
        self.user_speed = self.user_speed + mph
        return mph

    #total miles
    def miles(self,miles):
        self.total_miles = self.total_miles + miles


p1 = Person('John')
p1.myfunc()
print(p1.diff("10:00","12:00"))
print(p1.user_time)

print(p1.diff("10:00","12:00"))
print(p1.user_time)


print(p1.diff("10:00","12:00"))
print(p1.user_time)