from pyprnotifier import github_retrieval
import unittest
import datetime

class MockRequestResult:
    def __init__(self, jsonBlob):
        self.parsedJsonBlob = jsonBlob
    def json(self):
        return self.parsedJsonBlob

class MockGithubRequests:
    def get(self, url, paramsdict):
        if (url == 'https://api.github.com/repos/dummyEmptyOrg/dummyEmptyRepo/pulls'):
            return MockRequestResult(jsonBlob = [])
        elif (url == 'https://api.github.com/repos/dummyOrg/dummyRepo/pulls'):
            if paramsdict['page'] == 1:
                return MockRequestResult(jsonBlob = [{
                    'number': 6,
                    'state': 'closed',
                    'title': 'The Sixth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/6',
                    'updated_at': '2011-01-21T19:01:12Z',
                    'user': {
                        'login': 'OtherGuy'
                    }
                },{
                    'number': 5,
                    'state': 'open',
                    'title': 'The Fifth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/5',
                    'updated_at': '2011-01-20T19:01:12Z',
                    'user': {
                        'login': 'CoolUser13'
                    }
                },{
                    'number': 4,
                    'state': 'closed',
                    'title': 'The Fourth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/4',
                    'updated_at': '2011-01-19T19:01:12Z',
                    'user': {
                        'login': 'OtherGuy'
                    }
                }])
            elif paramsdict['page'] == 2:
                return MockRequestResult(jsonBlob = [{
                    'number': 3,
                    'state': 'open',
                    'title': 'The Third PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/3',
                    'updated_at': '2011-01-18T19:01:12Z',
                    'user': {
                        'login': 'CoolUser13'
                    }
                },{
                    'number': 2,
                    'state': 'open',
                    'title': 'The Second PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/2',
                    'updated_at': '2011-01-17T19:01:12Z',
                    'user': {
                        'login': 'OtherGuy'
                    }
                },{
                    'number': 1,
                    'state': 'closed',
                    'title': 'The First PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/1',
                    'updated_at': '2011-01-16T19:01:12Z',
                    'user': {
                        'login': 'CoolUser13'
                    }
                }])
            elif paramsdict['page'] == 3: #Tested github api, if you specify a page past what exists it returns an empty set.
                return MockRequestResult(jsonBlob = [])

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_dummyTest(self):
        assert True

    def test_isPRTooOld_yes(self):
        PRObject = {'updated_at': '2011-01-26T19:01:12Z'}
        self.assertTrue(github_retrieval.isPRTooOld(PRObject,datetime.date(2012,1,1)))
    
    def test_isPRTooOld_no(self):
        PRObject = {'updated_at': '2011-01-26T19:01:12Z'}
        self.assertFalse(github_retrieval.isPRTooOld(PRObject,datetime.date(2011,1,25)))
    
    def test_isPRTooOld_invalidInput(self):
        PRObject = {'updated_at': 'NotADate'}
        self.assertRaisesRegex(ValueError, 'Invalid date pulled from Pull Request update_at field: NotADate', github_retrieval.isPRTooOld, PRObject, datetime.date(2011,1,25))

    def test_getCutoffTime(self):
        now = datetime.date(2011,1,25)
        a_week_ago = github_retrieval.getCutoffTime(now, datetime.timedelta(days=7))
        self.assertEqual(a_week_ago, datetime.date(2011,1,18))
    
    def test_get_PRs(self):
        ghq = MockGithubRequests()
        self.assertEqual(github_retrieval.get_PRs('dummyEmptyOrg','dummyEmptyRepo',req_module=ghq).json(),[])
    
    def test_get_PRs_withcontent(self):
        ghq = MockGithubRequests()
        self.assertEqual(len(github_retrieval.get_PRs('dummyOrg','dummyRepo',page_number=1, req_module=ghq).json()),3)

    def test_get_Recent_PRs_ResultOnFirstPage(self):
        ghq = MockGithubRequests()
        #This test should grab only the first two PRs in the list, because the "current date" is set for 7 days ahead of the 5th PR
        result = github_retrieval.get_Recent_PRs(datetime.date(2011,1,27), datetime.timedelta(days=7), 'dummyOrg', 'dummyRepo', pr_state = 'all', req_module = ghq)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['number'],6)
        self.assertEqual(result[0]['title'],'The Sixth PR')
        self.assertEqual(result[1]['number'],5)
        self.assertEqual(result[1]['title'],'The Fifth PR')
    
    def test_get_Recent_PRs_ResultOnSecondPage(self):
        ghq = MockGithubRequests()
        #This test should grab only the first two PRs in the list, because the "current date" is set for 7 days ahead of the 5th PR
        result = github_retrieval.get_Recent_PRs(datetime.date(2011,1,24), datetime.timedelta(days=7), 'dummyOrg', 'dummyRepo', pr_state = 'all', req_module = ghq)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0]['number'],6)
        self.assertEqual(result[0]['title'],'The Sixth PR')
        self.assertEqual(result[1]['number'],5)
        self.assertEqual(result[1]['title'],'The Fifth PR')
        self.assertEqual(result[2]['number'],4)
        self.assertEqual(result[2]['title'],'The Fourth PR')
        self.assertEqual(result[3]['number'],3)
        self.assertEqual(result[3]['title'],'The Third PR')
        self.assertEqual(result[4]['number'],2)
        self.assertEqual(result[4]['title'],'The Second PR')

    def test_get_Recent_PRs_AllResultsMatter(self):
        ghq = MockGithubRequests()
        #This test should grab all PRs in the list, they should fall within 7 days of this date.
        result = github_retrieval.get_Recent_PRs(datetime.date(2011,1,22), datetime.timedelta(days=7), 'dummyOrg', 'dummyRepo', pr_state = 'all', req_module = ghq)
        self.assertEqual(len(result), 6)

    def test_get_Recent_PRs_NoResultsMatter(self):
        ghq = MockGithubRequests()
        #This test should grab no PRs in the list, because it is more than 7 days past the last date.
        result = github_retrieval.get_Recent_PRs(datetime.date(2011,1,29), datetime.timedelta(days=7), 'dummyOrg', 'dummyRepo', pr_state = 'all', req_module = ghq)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()