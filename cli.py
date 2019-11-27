#export my app.py class here then put this in a function in main
from app import Driver

#have a class that calculates trips
driver_dict = {}

filepath = 'trips.txt'

def initDriver(filepath):
    #open the file and create a person/driver object
    with open(filepath) as fp:
        driver_dict = {}

        for line in fp:
            if 'Driver' in line:

                driver = line[6:].strip()
                person_driver=Driver(driver)

                driver_dict[driver] = person_driver
    return driver_dict


print(initDriver(filepath))


def driverInfo(driver_dict):
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

                if driver_dict[driver_name]:
                    driver_obj = driver_dict[driver_name]
                    user_time = driver_obj.diff(start,end)
                    user_miles = driver_obj.miles(miles)
                    driver_obj.speed(user_miles,user_time)
                    #driver_dict[driver_name].speed(driver_dict[driver_name].total_miles,driver_dict[driver_name].user_time )
        return driver_dict
               

driver_infomation = initDriver(filepath)
x = driverInfo(driver_infomation)
print(x)
print(x['Lauren'].total_miles,'lauren miles')
print(x['Lauren'].user_speed)
print(x['Lauren'].print_out())
print(x['Dan'].print_out())
print(x['Dan'].user_time,'dan time')
print(x['Dan'].total_miles,'dan miles')




           
               

       
           
               
        

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