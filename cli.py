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

driver_list = {}

#have class that creates drivers from text filea

#have a class that calculates trips

filepath = 'trips.txt'

#open the file and create a person/driver object
with open(filepath) as fp:
   for line in fp:
       if 'Driver' in line:

           driver = line[6:].strip()
           person_driver=Person(driver)

           driver_list[driver] = person_driver


print(driver_list)
#put driver list as a set to re move dups



#open the file and save number of miles and times each person object
with open(filepath) as fp:
   for line in fp:
       driver_name = ''
       start = ''
       end = ''
       miles = ''
    
       if 'Trip' in line:
           #split line
           split_line = line.split()

           #separate useful information
           driver_name = split_line[1]
           start = split_line[2]
           end = split_line[3]
           miles = float(split_line[4])
           print(miles)

           if driver_list[driver_name]:
               driver_list[driver_name].diff(start,end)
               driver_list[driver_name].miles(miles)
               driver_list[driver_name].speed(driver_list[driver_name].total_miles,driver_list[driver_name].user_time )
               

print(driver_list['Lauren'].total_miles)
print(driver_list['Lauren'].user_speed)



           
               

       
           
               
        

          # print(driver_name)

           

           

#print(driver_list[0].name,"driver name")


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