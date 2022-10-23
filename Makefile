simulate:
	pip install -r requirements.txt && \
	python tcs.py

test:
	pip install -r requirements.txt && \
		pytest --cov=. test_tcs.py