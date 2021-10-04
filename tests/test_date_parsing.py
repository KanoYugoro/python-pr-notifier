from pyprnotifier import date_parsing
import unittest
import datetime
from .MockGithubRequests import MockGithubRequests

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_reParseDate_validInput(self):
        testDate = '2011-01-26T19:01:12Z'
        self.assertEqual(date_parsing.reParseDate(testDate), datetime.date(2012,1,1))

    def test_reParseDate_invalidInput(self):
        testDate = 'NotADate'
        self.assertRaisesRegex(ValueError, 'Invalid date: NotADate', date_parsing.reParseDate, testDate)