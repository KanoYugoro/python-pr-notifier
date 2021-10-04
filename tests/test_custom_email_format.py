from pyprnotifier import custom_email_format
import unittest
from .MockGithubRequests import MockGithubRequests

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_formatTextPR(self):
        ghq = MockGithubRequests()
        PRObj = ghq.testingGetAll()[0]
        self.assertEqual(custom_email_format.formatTextPR(PRObj), "PR #6 - The Sixth PR by OtherGuy - Link: https://github.com/dummyOrg/dummyRepo/pull/6")