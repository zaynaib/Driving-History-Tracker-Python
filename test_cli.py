import unittest
from app import Driver
from cli import initDriver, driverInfo

class TestCLIMethods(unittest.TestCase):
    #setup
    def setUp(self):
        self.drivers = initDriver('trips.txt')
       

    def test_initDriver(self):
        self.assertEqual(len(self.drivers),3)
        self.assertEqual(self.drivers['Dan'].name, 'Dan')
        self.assertEqual(self.drivers['Kumi'].name, 'Kumi')
        self.assertEqual(self.drivers['Lauren'].name, 'Lauren')

    #def driverInfo_



    


    

if __name__ == '__main__':
    unittest.main()