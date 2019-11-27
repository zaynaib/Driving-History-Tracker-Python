from datetime import datetime
class Driver:
    def __init__(self,name):
        self.name = name
        self.user_time = 0
        self.user_speed = 0
        self.total_miles = 0
        
    # get time difference
    def diff(self,startTime, endTime):
        FMT = '%H:%M'
        tdelta = datetime.strptime(endTime, FMT) - datetime.strptime(startTime, FMT)
        hours,remainder = divmod(tdelta.seconds,3600)
        mintues,seconds = divmod(remainder,60)
        time = hours + (mintues/100)
        self.user_time = self.user_time + time
        return time

    #miles per hour

    def speed(self, distance,time):
        mph = distance/time
        if mph < 5 or mph > 100:
            self.user_speed = self.user_speed + 0

       
        elif time < 1:
            mph = distance * (60/(time*100))
            self.user_speed = round(self.user_speed + mph,2)
            
        else:
            self.user_speed = round(self.user_speed + mph,2)
            #self.user_speed = self.user_speed
        #return mph

    #total miles
    def miles(self,miles):
        self.total_miles = self.total_miles + miles
        self.total_miles = self.total_miles

    def print_out(self):
        if self.total_miles == 0:
            return "{}: {} miles".format(self.name, self.total_miles)
        return "{}: {} miles @ {} mph".format(self.name, round(self.total_miles),round(self.user_speed))


'''
p1 = Driver('John')
print(p1.name)
print(p1.diff("12:01","13:16"))
print(p1.user_time)
p1.user_time = 0.50
p1.speed(39.1,p1.user_time)
'''


#print(p1.diff("10:00","12:00"))
#print(p1.user_time)


#print(p1.diff("10:00","12:00"))
#print(p1.user_time)
