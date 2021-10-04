import re
import datetime

def reParseDate(dateString):
    regexGroups = re.search("(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)T",dateString)
    if regexGroups == None:
        raise ValueError(f'Invalid date: {dateString}')
    return datetime.date(int(regexGroups.group('year')),int(regexGroups.group('month')),int(regexGroups.group('day')))