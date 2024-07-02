# Tesla QA Automation Project

This project contains automated tests for the Tesla website (https://www.tesla.com/).

## Setup

1. Install Python 3.7 or higher
2. Install dependencies: `pip install -r requirements.txt`

## Running Tests

- To run UI tests: `pytest tests/ui_tests`
- To run API tests: `pytest tests/api_tests`
- To run performance tests: `locust -f tests/performance_tests/locustfile.py`

## Project Structure

- `tests/`: Contains all test files (UI, API, and performance)
- `pages/`: Page Object Model implementations
- `utils/`: Utility functions and configurations
- `conftest.py`: Pytest configurations and fixtures

## Notes

This is a basic implementation and may need adjustments based on the current structure of the Tesla website.
