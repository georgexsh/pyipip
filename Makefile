.PHONY: clean test bench package publish

help:
	@echo targets: test bench publish clean

dev_venv:
	virtualenv -q dev_venv
	./dev_venv/bin/pip install -q -e .

test: dev_venv
	@./dev_venv/bin/python tests/test_pyipip.py

bench: dev_venv
	./dev_venv/bin/pip install -q -r tests/reqs_bench.txt
	./dev_venv/bin/python tests/bench.py

package: clean
	python setup.py sdist bdist_wheel

publish: package
	twine upload dist/*

clean:
	rm -rf dev_venv
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete
