freeze:
	pip freeze >> requirements.txt

lint:
	black markov/
	flake8 markov/
	mypy markov/
	isort markov/
