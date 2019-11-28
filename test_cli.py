import unittest
from app import Driver
from cli import initDriver, driverTrips, driverOutput, calcTotal


class TestCLIMethods(unittest.TestCase):
    #setup
    def setUp(self):
        self.drivers = initDriver('trips.txt')
        self.driver_trips = driverTrips(self.drivers)
        self.totals = calcTotal(self.driver_trips)


       

    def test_initDriver(self):
        self.assertEqual(len(self.drivers),3)
        self.assertEqual(self.drivers['Dan'].name, 'Dan')
        self.assertEqual(self.drivers['Kumi'].name, 'Kumi')
        self.assertEqual(self.drivers['Lauren'].name, 'Lauren')

    def test_driverTrips(self):
        self.assertEqual(len(self.driver_trips),3)

        #lauren

        lauren = self.driver_trips['Lauren']
        self.assertEqual(lauren.name, 'Lauren') 

        self.assertEqual(len(lauren.trips),1)
        self.assertEqual(lauren.trips[0].start,"12:01")
        self.assertEqual(lauren.trips[0].end,"13:16")
        self.assertEqual(lauren.trips[0].distance,42)
        self.assertEqual(lauren.trips[0].minutes,75)

       #dan

        dan = self.driver_trips['Dan']
        self.assertEqual(dan.name, 'Dan')        
        self.assertEqual(len(dan.trips),2)
        self.assertEqual(dan.trips[0].start,"07:15")
        self.assertEqual(dan.trips[0].end,"07:45")
        self.assertEqual(dan.trips[0].distance,17.3)
        self.assertEqual(dan.trips[0].minutes,30)

    def test_calcTotal(self):
        self.assertEqual(self.totals['Dan'].total_miles,39.1)

    def test_driverOutput(self):
        self.assertEqual(self.driver_trips['Dan'].print_output(), 'Dan: 39 miles @ 47 mph' )
        self.assertEqual(self.driver_trips['Lauren'].print_output(), 'Lauren: 42 miles @ 34 mph' )
        self.assertEqual(self.driver_trips['Kumi'].print_output(), 'Kumi: 0 miles' )



if __name__ == '__main__':
    unittest.main()