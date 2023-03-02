VENV := $(PWD)/env
PYTHON := python
PIP := $(PYTHON) -m pip
PYV=$(shell $(PYTHON) -c "import sys;t='{v[0]}{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)")

.PHONY: help venv3 clean

help:	# The following lines will print the available commands when entering just 'make'
ifeq ($(UNAME), Linux)
	@grep -P '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
else
	@awk -F ':.*###' '$$0 ~ FS {printf "%15s%s\n", $$1 ":", $$2}' \
		$(MAKEFILE_LIST) | grep -v '@awk' | sort
endif

venv3: ### Creates a virtual environment for this project
	test -d $(VENV) || $(PYTHON) -m venv $(VENV) && source $(VENV)/bin/activate
	$(PIP) install --upgrade pip
	make install-all

test:
	python -m pytest src/

test-cov:
	python -m pytest --cov=. src/

clean: clean-build clean-pyc clean-env ### Cleans artifacts

clean-build: ### Removes builds
	find . -type d -iname "build" ! -path "./.venv/*" -exec rm -rf {} +
	find . -type d -iname "dist" ! -path "./.venv/*" -exec rm -rf {} +
	find . -type d -iname "*.egg-info" ! -path "./.venv/*" -exec rm -rf {} +

clean-env: ### Removes environment directory
	rm -rf $(VENV)

clean-pyc: ### Removes python compiled bytecode files
	find . -iname "*.pyc" ! -path "./.venv/*" -delete
	find . -type d -iname "__pycache__" ! -path "./.venv/*" -exec rm -rf {} +

install: ### Installs regular dependencies
	$(PIP) install -e .

install-dev: ### Installs regular and dev dependencies
	$(PIP) install -e ".[dev]"

install-doc: ### Installs regular and doc dependencies
	$(PIP) install -e ".[doc]"

install-test: ### Installs regular and test dependencies
	$(PIP) install -e ".[dev]"

install-all: ### Installs regular, dev, doc, and test dependencies
	$(PIP) install -e ".[dev,doc,test]"

package:  ### Builds the package in wheel format
	rm -rf build dist
	echo "$(version)" > src/ydata/sdk/VERSION
	$(PYTHON) -m build --wheel
	twine check dist/*

wheel:  ### Compiles the wheel
	test -d wheels || mkdir -p wheels
	cp dist/ydata_sdk-$(version)-py3-none-any.whl wheels/ydata_sdk-$(version)-py$(PYV)-none-any.whl
	$(PYTHON) -m pyc_wheel wheels/ydata_sdk-$(version)-py$(PYV)-none-any.whl
	twine check wheels/*

publish-docs: ### Publishes the documentation
	mike deploy --push --update-aliases $(version) latest
