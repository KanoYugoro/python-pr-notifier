init:
	pip install -r requirements.txt

test:
	python -m unittest discover

test-verbose:
	python -m unittest discover -v