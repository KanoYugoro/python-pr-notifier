init:
	pip install -r requirements.txt

run:
	python main.py --org PyGithub --repo PyGithub

test:
	python -m unittest discover 

test-verbose:
	python -m unittest discover -v