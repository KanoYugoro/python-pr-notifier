# python-pr-notifier
A python script to retrieve a summary of all opened, closed, and in progress pull requests for a given Github repository within some time frame, with email output.

## Script Usage
A simple makefile has been provided to facilitate running this python project.  Simply type `make run` and this project will scan against PyGithub/PyGithub.  If you wish to run this script against a different project, execute the main.py file in this directory with the provided arguments in the next section. `make test` and `make test-verbose` will execute the unit tests for this project.

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