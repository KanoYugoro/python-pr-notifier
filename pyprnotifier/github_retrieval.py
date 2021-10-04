import requests
import datetime
import re

def isPRTooOld(PRobj, cutoffTime):
    regexGroups = re.search("(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)T",PRobj.updated_at)
    if regexGroups == None:
        raise ValueError(f'Invalid date pulled from Pull Request update_at field: {PRobj.updated_at}')
    PRTime = datetime.date(int(regexGroups.group('year')),int(regexGroups.group('month')),int(regexGroups.group('day')))
    return cutoffTime > PRTime
    
def getCutoffTime(currentDate, timeDelta):
    return (currentDate - timeDelta)

def get_PRs(org,repo,pr_state = 'all',page_number = 1,req_module = requests):
    return req_module.get(f'https://api.github.com/repos/{org}/{repo}/pulls',{'state':pr_state,'sort':'updated','page':page_number,'per_page':100})

def get_Recent_PRs(currentDate, timeDelta, org, repo, pr_state = 'all', req_module = requests):
    requestResult = get_PRs(org,repo,pr_state,1,req_module)