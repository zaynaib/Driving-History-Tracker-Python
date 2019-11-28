#export my app.py class here then put this in a function in main
from app import Driver, Trip

#have a class that calculates trips

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


#print(initDriver(filepath))


def driverTrips(driver_dict):
    #open the file and save number of miles and times each person object
    with open(filepath) as fp:
        for line in fp:            
            if 'Trip' in line:

                #split line
                split_line = line.split()

                #separate useful information
                driver_name = split_line[1]
                start = split_line[2]
                end = split_line[3]
                miles = float(split_line[4])

                if driver_dict[driver_name]:
                    #Get driver from dictionary
                    driver_obj = driver_dict[driver_name]

                    #Add trips to driver
                    driver_obj.addTrip(start,end,miles)
                 
        return driver_dict

    
def driverOutput(d_info):
    #open the file and save number of miles and times each person object
    for key in d_info:
        driver_obj = d_info[key]
        print(driver_obj.print_output())
    
               

if __name__ == '__main__':
  

    #create drivers
    create_drivers = initDriver(filepath)

    #add trips
    driver_trips = driverTrips(create_drivers)

    #print drivers mile information
    driverOutput(driver_trips)






    '''
    print(x['Lauren'].total_miles,'lauren miles')
    print(x['Lauren'].user_speed)
    print(x['Lauren'].print_out())
    print(x['Dan'].print_out())
    print(x['Dan'].user_time,'dan time')
    print(x['Dan'].total_miles,'dan miles')
    print(x['Kumi'].print_out())
    '''




           
               

       
           
               
        

 