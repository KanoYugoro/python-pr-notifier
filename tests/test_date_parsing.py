from pyprnotifier import date_parsing
import unittest
import datetime

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_reParseDate_validInput(self):
        testDate = '2011-01-26T19:01:12Z'
        self.assertEqual(date_parsing.reParseDate(testDate), datetime.date(2011,1,26))

    def test_reParseDate_invalidInput(self):
        testDate = 'NotADate'
        self.assertRaisesRegex(ValueError, 'Invalid date: NotADate', date_parsing.reParseDate, testDate)