install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

language-install:
	installs/setup_rust.sh
	installs/setup_swift.sh

global-install: install language-install

test:
	#ignores the virus of pandas warnings
	python -m pytest -vv -p no:warnings test_*.py tests/

format:	
	black .

refactor: format lint

lint:
	find . -type f -name "*.py" \
	 | xargs pylint --disable=R,C --ignore-patterns=test_.*?py 

all: install lint test