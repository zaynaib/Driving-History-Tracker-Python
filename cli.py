#https://stackabuse.com/read-a-file-line-by-line-in-python/
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
'''
read file
while file is open
if word driver then do x
if word is trip then do y
'''

#export my app.py class here then put this in a function in main
from app import Person

driver_list = []

#have class that creates drivers from text filea

#have a class that calculates trips


filepath = 'trips.txt'

#figure how to account for dup names
with open(filepath) as fp:
   for line in fp:
       if 'Driver' in line:

           #get drivers name
           driver = line[6:]

           #create a person
           person_driver = Person(driver)

           #save person in a data structure - list
           driver_list.append(person_driver)

print(driver_list)
#put driver list as a set to re move dups

'''

with open(filepath) as fp:
   for line in fp:
       if 'Trip' in line:
           #split each line
           line_split = line.split()
           name = line_split[1]
           start = line_split[2]
           end = line_split[3]
           miles = line_split[4]

           for driver in driver_list:
               if name in driver_list:
                   driver.diff(end,start)
                   driver.miles(miles)
           print(line_split)

            
'''
#print(driver_list)


#for driver in driver_list:
#    driver.myfunc()
'''
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       #if line contains driver print drive
       #if line contains trip then do hey

       if 'Driver' in line:
           #create a constructor with the name of driver
           print(line[6:])
           #print("Line {}: {}".format(cnt, line.strip()))
           line = fp.readline()

       #if trip use the method
       cnt += 1
'''