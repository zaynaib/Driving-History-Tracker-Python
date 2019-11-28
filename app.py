from datetime import datetime
class Trip:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


    def duration(self, startTime, endTime):
        # get diff between start and end in minutes
        time_format = '%H:%M'
        delta_time = datetime.strptime(endTime, time_format) - datetime.strptime(startTime,time_format)
        mintues = delta_time.seconds/60
        return mintues
        
    #miles per hour   
    def speed(self,distance,time):
        mph = (distance/time)* 60
        return mph

t1 = Trip("12:01","13:16",42.0)
print(t1.start)
print(t1.end)
print(t1.duration(t1.start,t1.end))
print(t1.speed(42.0,75.0))

class Driver:
    def __init__(self,name):
        self.name = name
        self.user_time = 0
        self.user_speed = 0
        self.total_miles = 0
        self.trips = []

    def addTrip(self, start, end, distance):
        trip = Trip(start, end, distance)
        if trip.speed() > 5 and trip.speed() < 100:
            self.trips.append(trip)

    def getTotalDistance(self):
        distances = [trip.distance for trip in self.trips]
        total = 0
        for d in distances:
            total = total + d
        return total
        
    # get time difference


    #miles per hour

    def speed(self, distance,time):
        mph = 0

        if self.user_time < 1:
            mph = distance * (60/(time*100))
            self.user_speed = round(self.user_speed + mph,2)
            
        else:
            mph = distance/time
            self.user_speed = round(self.user_speed + mph,2)
        
        if mph< 5 or mph > 100:
            self.user_speed = 0
        return self.user_speed

    #total miles
    def miles(self,miles):
        self.total_miles = self.total_miles + miles
        self.total_miles = self.total_miles
        return self.total_miles

    def print_out(self):
        if self.total_miles == 0:
            return "{}: {} miles".format(self.name, self.total_miles)
        return "{}: {} miles @ {} mph".format(self.name, round(self.total_miles),round(self.user_speed))



