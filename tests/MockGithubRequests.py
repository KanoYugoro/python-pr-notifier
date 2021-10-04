from .MockRequestResult import MockRequestResult

class MockGithubRequests:
    def testingGetAll(self):
        return [] + self.get('https://api.github.com/repos/dummyOrg/dummyRepo/pulls',{'page': 1}).json() + self.get('https://api.github.com/repos/dummyOrg/dummyRepo/pulls',{'page': 2}).json()

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
                    'created_at': '2011-01-20T19:01:12Z',
                    'updated_at': '2011-01-21T19:01:12Z',
                    'closed_at': '2011-01-21T19:01:12Z',
                    'user': {
                        'login': 'OtherGuy'
                    }
                },{
                    'number': 5,
                    'state': 'open',
                    'title': 'The Fifth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/5',
                    'created_at': '2011-01-19T19:01:12Z',
                    'updated_at': '2011-01-20T19:01:12Z',
                    'closed_at': None,
                    'user': {
                        'login': 'CoolUser13'
                    }
                },{
                    'number': 4,
                    'state': 'closed',
                    'title': 'The Fourth PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/4',
                    'created_at': '2011-01-18T19:01:12Z',
                    'updated_at': '2011-01-19T19:01:12Z',
                    'closed_at': '2011-01-19T19:01:12Z',
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
                    'created_at': '2011-01-17T19:01:12Z',
                    'updated_at': '2011-01-18T19:01:12Z',
                    'closed_at': None,
                    'user': {
                        'login': 'CoolUser13'
                    }
                },{
                    'number': 2,
                    'state': 'open',
                    'title': 'The Second PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/2',
                    'created_at': '2011-01-14T19:01:12Z',
                    'updated_at': '2011-01-17T19:01:12Z',
                    'closed_at': None,
                    'user': {
                        'login': 'OtherGuy'
                    }
                },{
                    'number': 1,
                    'state': 'closed',
                    'title': 'The First PR',
                    'html_url': 'https://github.com/dummyOrg/dummyRepo/pull/1',
                    'created_at': '2011-01-14T19:01:12Z',
                    'updated_at': '2011-01-16T19:01:12Z',
                    'closed_at': '2011-01-16T19:01:12Z',
                    'user': {
                        'login': 'CoolUser13'
                    }
                }])
            elif paramsdict['page'] == 3: #Tested github api, if you specify a page past what exists it returns an empty set.
                return MockRequestResult(jsonBlob = [])