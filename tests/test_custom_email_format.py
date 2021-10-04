from pyprnotifier import custom_email_format
import unittest
from .MockGithubRequests import MockGithubRequests

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_formatTextPR(self):
        ghq = MockGithubRequests()
        PRObj = ghq.testingGetAll()[0]
        self.assertEqual(custom_email_format.formatTextPR(PRObj), "PR #6 - The Sixth PR by OtherGuy - Link: https://github.com/dummyOrg/dummyRepo/pull/6")

    def test_formatSortedPRs_OnlyOpen(self):
        mockSortedPRs = {
            'open': [{
                    'number': 5,
                    'state': 'open',
                    'title': 'The Fifth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/5',
                    'user': {
                        'login': 'CoolUser13'
                    }
                },{
                    'number': 4,
                    'state': 'open',
                    'title': 'The Fourth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/4',
                    'user': {
                        'login': 'CoolUser13'
                    }
                }],
            'closed': [],
            'in-progress': []
        }
        output = custom_email_format.formatSortedPRs(mockSortedPRs)
        self.assertEqual(output,'Pull Requests Opened: \nPR #5 - The Fifth PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/5\nPR #4 - The Fourth PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/4\n')

    def test_formatSortedPRs_OnlyClosed(self):
        mockSortedPRs = {
            'open': [],
            'closed': [{
                    'number': 5,
                    'state': 'closed',
                    'title': 'The Fifth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/5',
                    'user': {
                        'login': 'CoolUser13'
                    }
                },{
                    'number': 4,
                    'state': 'closed',
                    'title': 'The Fourth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/4',
                    'user': {
                        'login': 'CoolUser13'
                    }
                }],
            'in-progress': []
        }
        output = custom_email_format.formatSortedPRs(mockSortedPRs)
        self.assertEqual(output,'Pull Requests Closed: \nPR #5 - The Fifth PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/5\nPR #4 - The Fourth PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/4\n')

    def test_formatSortedPRs_OnlyInProgress(self):
        mockSortedPRs = {
            'open': [],
            'closed': [],
            'in-progress': [{
                    'number': 5,
                    'state': 'open',
                    'title': 'The Fifth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/5',
                    'user': {
                        'login': 'CoolUser13'
                    }
                },{
                    'number': 4,
                    'state': 'open',
                    'title': 'The Fourth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/4',
                    'user': {
                        'login': 'CoolUser13'
                    }
                }]
        }
        output = custom_email_format.formatSortedPRs(mockSortedPRs)
        self.assertEqual(output,'Pull Requests In Progress: \nPR #5 - The Fifth PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/5\nPR #4 - The Fourth PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/4\n')

    def test_formatSortedPRs_AllTypes(self):
        mockSortedPRs = {
            'open': [{
                    'number': 3,
                    'state': 'open',
                    'title': 'The Third PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/3',
                    'user': {
                        'login': 'CoolUser13'
                    }
                }],
            'closed': [{
                    'number': 4,
                    'state': 'closed',
                    'title': 'The Fourth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/4',
                    'user': {
                        'login': 'OtherGuy'
                    }
                }],
            'in-progress': [{
                    'number': 5,
                    'state': 'open',
                    'title': 'The Fifth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/5',
                    'user': {
                        'login': 'CoolUser13'
                    }
                }]
        }
        output = custom_email_format.formatSortedPRs(mockSortedPRs)
        self.maxDiff = None
        self.assertEqual(output,'Pull Requests Opened: \nPR #3 - The Third PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/3\nPull Requests In Progress: \nPR #5 - The Fifth PR by CoolUser13 - Link: https://github.com/dummyOrg/dummyRepo/pull/5\nPull Requests Closed: \nPR #4 - The Fourth PR by OtherGuy - Link: https://github.com/dummyOrg/dummyRepo/pull/4\n')
    
    def test_formatEmailBody_No_Activity(self):
        mockSortedPRs = {
            'open': [],
            'closed': [],
            'in-progress': []
        }

        output = custom_email_format.formatEmailBody('SomeOrg', 'SomeRepo', '7', mockSortedPRs)
        self.assertEqual(output,'Greetings!\n\nNo activity has been found for SomeOrg/SomeRepo in the last 7 days.\n\nI hope this information is useful to you.\n-Anson\'s script')
