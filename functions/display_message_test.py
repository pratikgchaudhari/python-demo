import unittest
from display_message import display_message

class DisplayMessageTestCase(unittest.TestCase):
    """Test cases for 'display_message.py'"""

    def test_display_message(self):
        self.assertEqual(display_message(),"Hi, we are learning how to write functions in Python.")

unittest.main()