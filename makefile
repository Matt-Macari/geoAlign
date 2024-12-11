# Python command
PYTHON = python3

# Run unit tests
.PHONY: unit
unit:
	$(PYTHON) -m unittest discover -s unit -p '*_test.py'

# Run the main script
run:
	$(PYTHON) src/main.py
