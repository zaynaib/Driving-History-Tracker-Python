import unittest
from app import Driver
from cli import initDriver, driverInfo

class TestCLIMethods(unittest.TestCase):
    #setup
    def setUp(self):
        self.drivers = initDriver('trips.txt')
        self.driver_info = driverInfo(self.drivers)
       

    def test_initDriver(self):
        self.assertEqual(len(self.drivers),3)
        self.assertEqual(self.drivers['Dan'].name, 'Dan')
        self.assertEqual(self.drivers['Kumi'].name, 'Kumi')
        self.assertEqual(self.drivers['Lauren'].name, 'Lauren')

    def test_driverInfo(self):
        self.assertEqual(len(self.driver_info),3)

        lauren = self.driver_info['Lauren']
        self.assertEqual(lauren.name, 'Lauren')
        self.assertEqual(lauren.total_miles,42.0)
        self.assertEqual(lauren.user_time,1.15)
        self.assertEqual(lauren.user_speed,36.52)
        self.assertEqual(lauren.print_out(), "Lauren: 42 miles @ 34 mph")


        dan = self.driver_info['Dan']
        self.assertEqual(dan.name, 'Dan')
        self.assertEqual(dan.total_miles,39.1)
        self.assertEqual(dan.user_time,0.5)
        #self.assertEqual(dan.user_speed,46.92)

        
        kumi = self.driver_info['Kumi']
        self.assertEqual(kumi.name, 'Kumi')
        self.assertEqual(kumi.total_miles,0)
        self.assertEqual(kumi.user_time,0)
        self.assertEqual(kumi.user_speed,0)
        self.assertEqual(kumi.print_out(), "Kumi: 0 miles")






        
        #self.assertEqual()



    


    

if __name__ == '__main__':
    unittest.main()