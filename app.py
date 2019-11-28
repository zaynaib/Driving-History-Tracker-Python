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


class Driver:
    def __init__(self,name):
        #do not create speed attribute
        self.name = name
        self.user_time = 0
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
            self.total_miles += d

    def getTotalTime(self):
        durations = [trip.minutes for trip in self.trips]
        for t in durations:
            self.user_time += t

    #total miles
    def avg_speed(self):
        avg_mph = (self.total_miles/self.user_time) * 60
        return avg_mph


    def print_output(self):

        if self.total_miles == 0:
            return "{}: {} miles".format(self.name, self.total_miles)
        return "{}: {} miles @ {} mph".format(self.name, round(self.total_miles),round(self.avg_speed()))


