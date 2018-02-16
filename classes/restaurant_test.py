import unittest
from restaurant import Restaurant


class RestaurantTestCase(unittest.TestCase):
    """Test cases for Restaurant class"""

    def setUp(self):
        self.restaurant_1 = Restaurant('Little Italy', 'Italian')
        self.restaurant_2 = Restaurant('CopaCabana', 'Mexican and Thai')
        self.restaurant_3 = Restaurant('Exotica Pune', 'North Indian')

    def test_describe_restaurant(self):
        self.assertEqual(self.restaurant_1.describe_restaurant(),'Little Italy serves Italian')
        self.assertEqual(self.restaurant_2.describe_restaurant(),'CopaCabana serves Mexican and Thai')
        self.assertEqual(self.restaurant_3.describe_restaurant(),'Exotica Pune serves North Indian')

    def test_open_restaurant(self):
        self.assertEqual(self.restaurant_1.open_restaurant(),'Little Italy is now open')
        self.assertEqual(self.restaurant_2.open_restaurant(),'CopaCabana is now open')
        self.assertEqual(self.restaurant_3.open_restaurant(),'Exotica Pune is now open')


unittest.main()
