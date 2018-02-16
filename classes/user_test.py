import unittest
from user import User

class UserTestCase(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        self.user_1 = User('John','Doe','23rd March 1979')
        self.user_2 = User('Archie','Andrews','2nd March 1989')
        self.user_3 = User('Dean','Winchester','5th August 1994')

    def test_describe_user(self):
        self.assertEqual(self.user_1.describe_user(),'John Doe was born on 23rd March 1979')
        self.assertEqual(self.user_2.describe_user(),'Archie Andrews was born on 2nd March 1989')
        self.assertEqual(self.user_3.describe_user(),'Dean Winchester was born on 5th August 1994')

    def test_greet_user(self):
        self.assertEqual(self.user_1.greet_user(),'Hi, John Doe')
        self.assertEqual(self.user_2.greet_user(),'Hi, Archie Andrews')
        self.assertEqual(self.user_3.greet_user(),'Hi, Dean Winchester')

unittest.main()