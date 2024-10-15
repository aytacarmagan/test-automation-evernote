# Evernote Automation Test Project

This project contains automated tests for Evernote using Selenium WebDriver and Python. It follows the Page Object Model (POM) design pattern for better maintainability and readability.

## Project Structure

```
project_root/
├── config/
│   └── config.yaml
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── editor_page.py
│   ├── login_page.py
│   └── notes_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login_create_note.py
│   └── test_login_find_note.py
├── utilities/
│   ├── __init__.py
│   └── driver_factory.py
├── requirements.txt
└── conftest.py
```

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Chrome browser installed

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/aytacarmagan/test-automation-evernote.git
   cd <project-directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

The `config.yaml` file contains important settings for the tests, including:

- Evernote URLs
- User Credentials (with email & password)
- User manual open mode

Make sure to keep this file updated with the correct information.

## Running the project

To run all tests:

```
pytest
```

To run a specific test file:

```
pytest tests/<name_of_the_file.py>
```


## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed.
2. Check that the Chrome browser and ChromeDriver versions are compatible.
3. Verify that the `config.yaml` file contains the correct information.
4. Check the console output for any error messages or stack traces.
