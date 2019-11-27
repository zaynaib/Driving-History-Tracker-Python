import unittest
from app import Driver

class TestAppMethods(unittest.TestCase):
    #setup
    def setUp(self):
        self.dan = Driver('Dan')
        self.kumi = Driver('Kumi')
        self.lauren = Driver('Lauren')

    def test_driver(self):
        self.assertEqual(self.dan.name, 'Dan')
        self.assertEqual(self.dan.total_miles,0)
        self.assertEqual(self.dan.user_time,0)
        self.assertEqual(self.dan.user_speed,0)

    def test_diff(self):
        self.dan.diff("07:15","07:45")
        self.assertEqual(type(self.dan.user_time),float)
        self.assertEqual(self.dan.user_time,0.30)
        self.dan.diff("06:12","06:32")
        self.assertEqual(self.dan.user_time,0.50)

    def test_miles(self):
        self.dan.miles(17.3)
        self.assertEqual(self.dan.total_miles, 17.3)
        self.dan.miles(21.8)
        self.assertEqual(self.dan.total_miles, 39.1)

    def test_speed(self):

        self.dan.user_time = 0.50
        self.dan.total_miles = 39.1
        

        self.dan.speed(self.dan.total_miles,self.dan.user_time)
        self.assertEqual(self.dan.user_speed,46.92)

        self.assertEqual(self.kumi.user_speed,0)

        self.lauren.diff("12:01","13:16")
        self.lauren.miles(42.0)
        self.lauren.speed(42,self.lauren.user_time)
        self.assertEqual(self.lauren.user_speed,36.52)

    def test_output(self):
        self.dan.user_time = 0.50
        self.dan.total_miles = 39.1
        self.dan.speed(self.dan.total_miles,self.dan.user_time)
        self.assertEqual(self.dan.user_speed,46.92)


        self.assertEqual(self.dan.print_out(), "Dan: 39 miles @ 47 mph")
        self.assertEqual(self.kumi.print_out(), "Kumi: 0 miles")


    

if __name__ == '__main__':
    unittest.main()