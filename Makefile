install:
	pip install -r requirements.txt; python setup.py install

unit:
	nosetests -v tests/unit

integration:
	nosetests -v tests/integration

tests: unit integration
