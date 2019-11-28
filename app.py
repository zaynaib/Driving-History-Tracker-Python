from datetime import datetime
class Trip:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance
        self.minutes = 0

    def duration(self):
        # get diff between start and end in minutes
        time_format = '%H:%M'
        delta_time = datetime.strptime(self.end, time_format) - datetime.strptime(self.start,time_format)
        self.minutes = delta_time.seconds/60
        return self.minutes
    #miles per hour   
    def speed(self):
        mph = (self.distance/self.minutes)* 60
        return mph

t1 = Trip("12:01","13:16",42.0)
print(t1.start)
print(t1.end)
print(t1.duration())
#print(t1.speed(42.0,75.0))
print(t1.speed())


class Driver:
    def __init__(self,name):
        self.name = name
        self.user_speed = 0
        self.total_miles = 0
        self.trips = []

    def addTrip(self, start, end, distance):
        trip = Trip(start, end, distance)
        trip.duration()
        if trip.speed() > 5 and trip.speed() < 100:
            self.trips.append(trip)

    def getTotalDistance(self):
        distances = [trip.distance for trip in self.trips]
        for d in distances:
            self.total_miles = self.total_miles + d
        return self.total_miles

    #total miles
    def miles(self,miles):
        self.total_miles = self.total_miles + miles
        self.total_miles = self.total_miles
        return self.total_miles

    def print_out(self):
        if self.total_miles == 0:
            return "{}: {} miles".format(self.name, self.total_miles)
        return "{}: {} miles @ {} mph".format(self.name, round(self.total_miles),round(self.user_speed))



p1 = Driver("Lauren")
print(p1.name)
p1.addTrip("12:01","13:16",42.0)
print(p1.getTotalDistance())


p2 = Driver("Dan")
print(p2.name)
#p2.addTrip("07:15","07:45",17.3)
#p2.addTrip("06:12","06:32",21.8)

#print(p2.getTotalDistance())