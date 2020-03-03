# Makefile for RHEL7-CIS
.PHONY: help
help:
	@echo
	@echo This Makefile is used to test this role. Typical use:
	@echo
	@echo '   make test'
	@echo '   make clean'
	@echo '   make compare'
	@echo
	@echo
	@echo To use the isolated environment from this directory:
	@echo
	@echo '   make venv'
	@echo '   . bin/activate'
	@echo
	@echo Molecule has built-in help
	@echo
	@echo '   molecule'
	@echo
	@echo "Run just the role 'molecule converge'"
	@echo "Login to the VM 'molecule login'"
	@echo
	@echo To run an audit using 'molecule verify' see tests/test_default.yml
	@echo To compare audit results between setups with docker vs vagrant run 'make compare'

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
	virtualenv .
	bin/pip install -r requirements.txt
	virtualenv --relocatable .

# cleanup virtualenv and molecule leftovers
clean:
	rm -rf bin lib include lib64 share
	rm -f .Python pip-selfcheck.json

.PHONY: lint
lint: bin/python
	( . bin/activate && bin/molecule lint )

.PHONY: test
test: bin/python
	( . bin/activate && bin/molecule test )
