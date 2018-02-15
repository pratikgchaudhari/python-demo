import unittest
from city_functions import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'. """
    def test_city_country(self):
        formatted_name = get_formatted_name("New York","United States")
        self.assertEqual(formatted_name,"New York, United States")
    
    def test_city_country_population(self):
        formatted_name = get_formatted_name("New York","United States",8550405)
        self.assertEqual(formatted_name,"New York, United States - Population 8550405")

unittest.main()