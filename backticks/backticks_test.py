from unittest import TestCase
from unittest import main

class BackTicksUnitTest(TestCase):
    """Test cases for 'backticks.py'"""

    def test(self):
        self.assertEqual(`3+2`,'5')

main()