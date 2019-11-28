from app import Driver, Trip
import operator


filepath = 'trips.txt'

#create driver instances

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



#add trips to drivers
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

#calculate total distance and times of drivers    
def calcTotal(d_info):
    for key in d_info:
        d_info[key].getTotalDistance()
        d_info[key].getTotalTime()
    return d_info


#print out drivers sorted by highest number of miles   
def driverOutput(d_info):
    for driver in (sorted(d_info.values(),key=operator.attrgetter('total_miles'),reverse=True)):
        print(driver.print_output())

     

if __name__ == '__main__':
  

    #create drivers
    create_drivers = initDriver(filepath)

    #add trips
    driver_trips = driverTrips(create_drivers)

    #aggerate 
    calcTotal(driver_trips)

    #print drivers mile information
    driverOutput(driver_trips)










           
               

       
           
               
        

 