import argparse
import datetime
import os.path
import json
from pyprnotifier import github_retrieval
from pyprnotifier import custom_email_format
from pyprnotifier import emailing

parser = argparse.ArgumentParser(description='This script retrieves recent Pull Requests from a publicly available git repository, formats info about them, and outputs them.')
parser.add_argument('--org', type=str,  help='The github org the repository lives in.', required=True)
parser.add_argument('--repo', type=str, help='The github repository name', required=True)
parser.add_argument('--timeframe', type=int, default=7, help='The number of days to look back in time. (the default is 7)')
parser.add_argument('--email', type=str, default='notprovided@nodomain.com', help='The email you want to send it to.  (If not provided, output will be to console.)')
args = parser.parse_args()

today = datetime.date.today()
timeDelta = datetime.timedelta(days=args.timeframe)
all_relevant_prs = github_retrieval.get_Recent_PRs(today, timeDelta, args.org, args.repo, pr_state = 'all')
sorted_prs = github_retrieval.SortPRs(all_relevant_prs, today, timeDelta)

email_body = custom_email_format.formatEmailBody(args.org, args.repo, args.timeframe, sorted_prs)

print('Script Output:')
print('FROM: no-reply@ansonscript.com')
print(f'TO: {args.email}')
email_subject = f'Pull Request report for {args.org}/{args.repo} for the {args.timeframe} days preceding {today}'
print(f'SUBJECT: {email_subject}')
print(f'BODY: \n{email_body}')

if (os.path.exists('./credential.json')):
    print('Credentials.json found, attempting to send results out via email.')
    if args.email is not None and args.email != "" and args.email != 'notprovided@nodomain.com':
        print(f'Attempting to send results to {args.email}')
        with open('./credential.json', mode='r') as creds:
            c = json.load(creds)
            emailing.sendEmail(args.email,c['username'],c['password'],c['smtp_host'],c['smtp_port'],email_subject,email_body)
    else:
        print('Must provide --email argument with intended recipient.')