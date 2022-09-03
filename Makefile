install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

# format all python files nested in sub-directories using python black
format:	
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test