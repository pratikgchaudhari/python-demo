import unittest
from favourite_book import favourite_book

class FavouriteBookTestCase(unittest.TestCase):
    """Tests for 'favourite_book.py'"""

    def test_favourite_book(self):
        book = "Alice in Wonderland".title()
        self.assertEquals(favourite_book(book),"One of my favourite books is " + book)

unittest.main()