from .MockRequestResult import MockRequestResult

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