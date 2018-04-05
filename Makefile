.PHONY: help clean test bench package publish

help:
	@echo targets: test bench publish clean

venv:
	virtualenv -q venv
	./venv/bin/pip install -q -e .

test: venv
	@./venv/bin/python tests/test_pyipip.py

bench: venv
	./venv/bin/pip install -q -r tests/reqs_bench.txt
	./venv/bin/python tests/bench.py

package: clean
	python setup.py sdist bdist_wheel

publish: package
	twine upload dist/*

clean:
	rm -rf venv
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete
