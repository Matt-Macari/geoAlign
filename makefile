.PHONY: test clean run

# Run all unit tests within the virtual environment
test:
	source env/bin/activate && python3 -m unittest discover -s src/unit

# Run the main script within the virtual environment
run:
	source env/bin/activate && python3 src/main.py

# Clean up any __pycache__ files within the virtual environment
clean:
	source env/bin/activate && find . -type d -name '__pycache__' -exec rm -rf {} +
