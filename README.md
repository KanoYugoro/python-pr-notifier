# python-pr-notifier
A python script to retrieve a summary of all opened, closed, and in progress pull requests for a given Github repository within some time frame, with email output.

## Script Usage
A simple makefile has been provided to facilitate running this python project.  Simply type `make run` and this project will scan against PyGithub/PyGithub.  If you wish to run this script against a different project, execute the main.py file in this directory with the provided arguments in the next section. `make test` and `make test-verbose` will execute the unit tests for this project.

In order to have the output sent as an email, you must create a `credentials.json` file in the same directory as `main.py`.  This file should look something like this:
``` json
{
    "smtp_host": "smtp.gmail.com",
    "smtp_port": 465,
    "username": "SoAndSo@gmail.com",
    "password": "SoAndSoSPasSWord"
}
```
If the intended solution is to use gmail, you'll have to [make an app specific password](https://support.google.com/accounts/answer/185833?hl=en) and use that password in the credential.json file.  In addition, the `--email` parameter must be provided to the script.

## Argument Reference
- `--org`, a required, case-sensitive string argument that indicates which public github organization the repository lives in.
- `--repo`, a required, case-sensitive string argument that indicates which public github repository to look at.
- `--timeframe`, The number of days to look back in time. (the default is 7)
- `--email`, The email you want to send the results of the script run to.  (If not provided, output will be to console.)

## Example Script Output
When I ran the script on the evening of October 4th, 2021, this was the console output I received.

```
Script Output:
FROM: no-reply@ansonscript.com
TO: notprovided@nodomain.com
SUBJECT: Pull Request report for PyGithub/PyGithub for the 7 days preceding 2021-10-04
BODY:
Greetings!

Pull Requests Opened:
PR #2068 - Pass a required parameter (headers) to GithubException constructor. by akhilg - Link: https://github.com/PyGithub/PyGithub/pull/2068
PR #2066 - Add support for merge-upstream Repository action by deriamis - Link: https://github.com/PyGithub/PyGithub/pull/2066
Pull Requests In Progress:
PR #1951 - Add support for workflow jobs and steps by Tenzer - Link: https://github.com/PyGithub/PyGithub/pull/1951
PR #1985 - Add Artifact class and WorkflowRun.get_artifacts by yixinguo2 - Link: https://github.com/PyGithub/PyGithub/pull/1985
PR #1986 - Support full GitHub app authentication by dblanchette - Link: https://github.com/PyGithub/PyGithub/pull/1986
PR #2006 - Add Github Actions Secrets to organization by peresypkinamarina - Link: https://github.com/PyGithub/PyGithub/pull/2006
PR #2063 - ADD code scanning results by eric-nieuwland - Link: https://github.com/PyGithub/PyGithub/pull/2063
Pull Requests Closed:
PR #2007 - tox.ini: Ignoring long lines and setting max-line-length? by cclauss - Link: https://github.com/PyGithub/PyGithub/pull/2007


I hope this information is useful to you.
-Anson's script
```

## Notes about this script
This script should handle the github api's pagination that occurs if too many results were returned, for example if it was run against a really busy repo.  If that was done unauthenticated, however, the script may not complete or may error out because of the unauthenticated rate limit of 60 requests per hour.