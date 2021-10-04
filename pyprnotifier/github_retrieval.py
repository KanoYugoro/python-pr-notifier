import requests
import datetime
import re

from requests.api import request

def isPRTooOld(PRobj, cutoffTime):
    updateTime = PRobj['updated_at']
    regexGroups = re.search("(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)T",updateTime)
    if regexGroups == None:
        raise ValueError(f'Invalid date pulled from Pull Request update_at field: {updateTime}')
    PRTime = datetime.date(int(regexGroups.group('year')),int(regexGroups.group('month')),int(regexGroups.group('day')))
    return cutoffTime > PRTime
    
def getCutoffTime(currentDate, timeDelta):
    return (currentDate - timeDelta)

def get_PRs(org,repo,pr_state = 'all',page_number = 1,req_module = requests):
    return req_module.get(f'https://api.github.com/repos/{org}/{repo}/pulls',{'state':pr_state,'sort':'updated','page':page_number})

def get_Recent_PRs(currentDate, timeDelta, org, repo, pr_state = 'all', req_module = requests):
    jsonCollection = []
    page_number = 0
    cutoffDate = getCutoffTime(currentDate, timeDelta)
    foundCutoff = False

    while (not foundCutoff):
        page_number = page_number + 1
        requestResult = get_PRs(org,repo,pr_state,page_number,req_module).json()
        if (requestResult == []): # We've exceeded the number of pages
            foundCutoff = True
            break

        index = 0
        while (index < len(requestResult) and not foundCutoff):
            foundCutoff = isPRTooOld(requestResult[index], cutoffDate)
            if (not foundCutoff):
                index = index + 1
        
        if (not foundCutoff or index > len(requestResult)): #So we went all the way through the first page and we haven't found the end of the PRs in the time span we want.
            jsonCollection = jsonCollection + requestResult
        elif (foundCutoff): #we found the PR in the list that is too old to care about, so append to that point
            jsonCollection = jsonCollection + (requestResult[0:index])
    
    return jsonCollection
    