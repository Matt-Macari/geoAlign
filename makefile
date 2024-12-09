# Set the test directory
TEST_DIR = unit

# Python command
PYTHON = python3

# Run unit tests
.PHONY: unit
unit:
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p '*_test.py'

# Run the main script
run:
	$(PYTHON) src/main.py

# Install dependencies from requirements.txt
install-dependencies:
	pip install -r requirements.txt

# Add dependencies to requirements.txt
add-dependencies:
	pip freeze > requirements.txt