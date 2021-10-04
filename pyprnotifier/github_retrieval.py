import requests
import datetime
import re

def isPRTooOld(PRobj, cutoffTime):
    regexGroups = re.search("(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)T",PRobj.updated_at)
    if regexGroups == None:
        raise ValueError(f'Invalid date pulled from Pull Request update_at field: {PRobj.updated_at}')
    PRTime = datetime.date(int(regexGroups.group('year')),int(regexGroups.group('month')),int(regexGroups.group('day')))
    return cutoffTime > PRTime
    

def get_PRs(org,repo,pr_state = 'all',req_module = requests):
    r = req_module.get(f'https://api.github.com/repos/{org}/{repo}/pulls',{'state':pr_state,'sort':'updated'})
    print(r.headers)
    return r.json()
