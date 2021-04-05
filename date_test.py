"""
Use unittest.TestCase methods to confirm that the addition and subtraction 
of date and timedelta objects produce correct results.
"""

import unittest
from datetime import datetime, timedelta


def add_time(x, change):
    if isinstance(change, timedelta):
        return x + change
    else:
        raise TypeError('Can only add timedelta type.')


def subtract_time(x, change):
    if isinstance(change, timedelta):
        return x - change
    else:
        raise TypeError('Can only subtract timedelta type.')



class TestDateTime(unittest.TestCase):
    """
    Test the add and subtract functions
    """

    @classmethod
    def setUpClass(cls):
        """
        Displays start of testing
        """
        print("Testing started...")

    @classmethod
    def tearDownClass(cls):
        """
        Displays end of testing
        """
        print("Testing completed!")

    def setUp(self):
        """
        Sets up date/time object variables for testing for each test
        """
        self.datetime_1 = datetime(2020, 1, 1, 11, 11, 11)
        self.datetime_2 = datetime(2007, 7, 7, 7, 0, 7)
        self.delta_1 = timedelta(days=4, minutes = 4)
        self.delta_2 = timedelta(days = 15, minutes = 15)
        self.delta_3 = timedelta(days = -10, minutes = -10, seconds = -10)
        self.date_3 = datetime(2020, 2, 2, 2, 2, 22)
        self.date_4 = datetime(1, 8, 8, 8, 8, 8)

    def test_add(self):
        """
        Test that the addition of datetime object with timedelta object returns the correct
        date/time
        """

        # Test add function with positive time
        print("1. add - positive time")
        self.assertEqual(add_time(self.datetime_1, self.delta_1), datetime(2020, 1, 5, 11, 15, 11))
        print("2. add - positive time")
        self.assertEqual(add_time(self.datetime_2, self.delta_1), datetime(2007, 7, 11, 7, 4, 7))
        print("3. add - positive time")
        self.assertEqual(add_time(self.date_3, self.delta_2), datetime(2020, 2, 17, 2, 17, 22))
        
        # Test add function with negative time, which should result in past date/time
        print("4. add - negative time")
        self.assertEqual(add_time(self.datetime_2, self.delta_3), datetime(2007, 6, 27, 6, 49, 57))
        
        # Test add function for TypeError exception
        print("5. add - TypeError")
        with self.assertRaises(TypeError):
            add_time(self.date_3, self.date_4)

    def test_subtract(self):
        """
        Test that the subtraction of timedelta object from datetime object returns the
        correct date/time
        """

        # Test subtract function with positive time
        print("1. subtract - positive time")
        self.assertEqual(subtract_time(self.datetime_1, self.delta_1), datetime(2019, 12, 28, 11, 7, 11))
        print("2. subtract - positive time")
        self.assertEqual(subtract_time(self.datetime_2, self.delta_1), datetime(2007, 7, 3, 6, 56, 7))
        print("3. subtract - positive time")
        self.assertEqual(subtract_time(self.date_3, self.delta_2), datetime(2020, 1, 18, 1, 47, 22))

        # Test subtract function with negative time, which should result in future date/time
        print("4. subtract - negative time")
        self.assertEqual(subtract_time(self.datetime_2, self.delta_3), datetime(2007, 7, 17, 7, 10, 17))


        # Test subtract function for TypeError exception
        print("5. subtract - TypeError")
        with self.assertRaises(TypeError):
            subtract_time(self.date_3, self.date_4)


if __name__ == '__main__':
    unittest.main()