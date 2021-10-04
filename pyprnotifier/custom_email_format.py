def formatTextPR(jsonPRObj):
    prNumber = jsonPRObj['number']
    prTitle = jsonPRObj['title']
    prUser= jsonPRObj['user']['login']
    prLink = jsonPRObj['html_url']
    return f'PR #{prNumber} - {prTitle} by {prUser} - Link: {prLink}'