from pyprnotifier import github_retrieval
import unittest
import datetime

class MockModel:
    pass

class MockGithubRequests:
    def get(self, url, paramsdict):
        if (url == 'https://api.github.com/repos/dummyEmptyOrg/dummyEmptyRepo/pulls'):
            return []
        elif (url == 'https://api.github.com/repos/dummyOrg/dummyRepo/pulls'):
            return [{
                'number': 1,
                'state': 'open',
                'title': 'The First PR',
                'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/1',
                'updated_at': '2011-01-16T19:01:12Z',
                'user': {
                    'login': 'CoolUser13'
                }
            },{
                'number': 2,
                'state': 'closed',
                'title': 'The Second PR',
                'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/2',
                'updated_at': '2011-01-17T19:01:12Z',
                'user': {
                    'login': 'OtherGuy'
                }
            },{
                'number': 3,
                'state': 'open',
                'title': 'The Third PR',
                'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/3',
                'updated_at': '2011-01-18T19:01:12Z',
                'user': {
                    'login': 'CoolUser13'
                }
            }]

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_dummyTest(self):
        assert True

    def test_isPRTooOld_yes(self):
        PRObject = MockModel()
        PRObject.updated_at = '2011-01-26T19:01:12Z'
        self.assertTrue(github_retrieval.isPRTooOld(PRObject,datetime.date(2012,1,1)))
    
    def test_isPRTooOld_no(self):
        PRObject = MockModel()
        PRObject.updated_at = '2011-01-26T19:01:12Z'
        self.assertFalse(github_retrieval.isPRTooOld(PRObject,datetime.date(2011,1,25)))
    
    def test_isPRTooOld_invalidInput(self):
        PRObject = MockModel()
        PRObject.updated_at = 'NotADate'
        self.assertRaisesRegex(ValueError, 'Invalid date pulled from Pull Request update_at field: NotADate', github_retrieval.isPRTooOld, PRObject, datetime.date(2011,1,25))

    def test_getCutoffTime(self):
        now = datetime.date(2011,1,25)
        a_week_ago = github_retrieval.getCutoffTime(now, datetime.timedelta(days=7))
        self.assertEqual(a_week_ago, datetime.date(2011,1,18))
    
    def test_get_PRs(self):
        ghq = MockGithubRequests()
        self.assertEqual(github_retrieval.get_PRs('dummyEmptyOrg','dummyEmptyRepo',req_module=ghq),[])
    
    def test_get_PRs_withcontent(self):
        ghq = MockGithubRequests()
        self.assertEqual(len(github_retrieval.get_PRs('dummyOrg','dummyRepo',req_module=ghq)),3)


if __name__ == '__main__':
    unittest.main()