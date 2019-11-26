from datetime import datetime
s1 = '10:33'
s2 = '14:15' # for example
FMT = '%H:%M'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
'''
print(type(tdelta))
print(tdelta.seconds)
print(tdelta)
'''

# get time difference
def diff(startTime, endTime):
    FMT = '%H:%M'
    tdelta = datetime.strptime(endTime, FMT) - datetime.strptime(startTime, FMT)
    return tdelta

#format time difference into a decimal
def hours(td):
    hours,remainder = divmod(td.seconds,3600)
    mintues, seconds = divmod(remainder,60)
    time = hours + (mintues/100)
    return time

#miles per hour

def speed(distance,time):
    mph = distance/time
    return mph

d = 42.0
t = diff('12:01','13:16')
t2 = hours(t)
print(t)
print(t2)
print(speed(d,t2))
'''
print(s)
print(diff('10:00','11:00'))
print(hours(tdelta))
'''
