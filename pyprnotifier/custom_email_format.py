def formatTextPR(jsonPRObj):
    prNumber = jsonPRObj['number']
    prTitle = jsonPRObj['title']
    prUser= jsonPRObj['user']['login']
    prLink = jsonPRObj['html_url']
    return f'PR #{prNumber} - {prTitle} by {prUser} - Link: {prLink}'

def formatSortedPRs(sortedDict):
    textResult = ''
    if len(sortedDict['open']) > 0:
        textResult = textResult + 'Pull Requests Opened: \n'
        for pr in sortedDict['open']:
            textResult = textResult + formatTextPR(pr) + '\n'

    if len(sortedDict['in-progress']) > 0:
        textResult = textResult + 'Pull Requests In Progress: \n'
        for pr in sortedDict['in-progress']:
            textResult = textResult + formatTextPR(pr) + '\n'

    if len(sortedDict['closed']) > 0:
        textResult = textResult + 'Pull Requests Closed: \n'
        for pr in sortedDict['closed']:
            textResult = textResult + formatTextPR(pr) + '\n'
    return textResult

def formatEmailBody(org, repo, timescale, sortedDict):
    email = 'Greetings!\n\n'
    if len(sortedDict['open']) == 0 and len(sortedDict['in-progress']) == 0 and len(sortedDict['closed']) == 0:
        email = email + f'No activity has been found for {org}/{repo} in the last {timescale} days.'
    else:
        email = email + formatSortedPRs(sortedDict)
    email = email + '\n\nI hope this information is useful to you.\n-Anson\'s script'
    return email