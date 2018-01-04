# Makefile for RHEL7-CIS
.PHONY: help
help:
	@echo
	@echo This Makefile is used to test this role. Typical use:
	@echo
	@echo	make test
	@echo	make clean
	@echo
	@echo To use an isolated python from this directory: 
	@echo
	@echo	make venv
	@echo	. bin/activate
	@echo

# virtualenv allows isolation of python libraries
.PHONY: venv
venv: bin/python

bin/python:
	## System's python 2.7 needs only 2 things:
	# pip is the package manager for python
	pip -V || sudo easy_install pip
	# virtualenv allows isolation of python libraries
	virtualenv --version || sudo easy_install virtualenv

	# Now with those two we can isolate our test setup.
	virtualenv --system-site-packages .
	bin/pip install -r requirements.txt
	virtualenv --relocatable .

# cleanup virtualenv and molecule
clean:
	rm -rf .molecule bin lib include lib64
	rm -f .Python pip-selfcheck.json
	
.PHONY: lint
lint: bin/python
	( . bin/activate && find . -name "*.yml" |grep -v .molecule |xargs yamllint )

.PHONY: test
test: bin/python
	( . bin/activate && molecule test )
