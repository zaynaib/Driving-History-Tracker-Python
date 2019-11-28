import unittest

from app import Driver,Trip


class TestTripMethods(unittest.TestCase):
    def setUp(self):
        self.t1 = Trip("12:01","13:16",42.0)

    def testInitTrip(self):
        self.assertEqual(self.t1.start,"12:01")
        self.assertEqual(self.t1.end,"13:16")
        self.assertEqual(self.t1.distance, 42.0)

    def testDuration(self):
        self.t1.duration()
        self.assertEqual(self.t1.minutes,75.0)

    def testSpeed(self):
        self.t1.duration()
        self.t1.speed()
        self.assertEqual(self.t1.speed(),33.6)


class TestAppMethods(unittest.TestCase):
    #setup
    def setUp(self):

        #setup Dan
        self.dan = Driver('Dan')
        self.dan.addTrip("07:15","07:45",17.3)
        self.dan.addTrip("06:12","06:32",21.8)

        #setup kumi
        self.kumi = Driver('Kumi')

        #setup lauren
        self.lauren = Driver('Lauren')
        self.lauren.addTrip("12:01","13:16",42.0)

    def test_driver(self):
        self.assertEqual(self.kumi.name, 'Kumi')
        self.assertEqual(self.kumi.total_miles,0)
        self.assertEqual(self.kumi.user_time,0)
        self.assertEqual(len(self.kumi.trips),0)
    
    def test_addTrip(self):
        self.kumi.addTrip("12:01","13:16",42.0)
        self.assertEqual(len(self.kumi.trips),1)

    def test_getTotalTime(self):
        self.dan.getTotalTime()
        self.assertEqual(self.dan.user_time,50.0)

    def test_getTotalDistance(self):
        self.dan.getTotalDistance()
        self.assertEqual(self.dan.total_miles, 39.1)

    def test_speed(self):
        self.dan.getTotalDistance()
        self.dan.getTotalTime()
        #self.dan.avg_speed()
        self.assertEqual(self.dan.avg_speed(),46.92)


    def test_output(self):
        self.assertEqual(self.dan.print_output(), "Dan: 39 miles @ 47 mph")
        self.assertEqual(self.kumi.print_output(), "Kumi: 0 miles")
        self.assertEqual(self.lauren.print_output(), "Lauren: 42 miles @ 34 mph")



if __name__ == '__main__':
    unittest.main()