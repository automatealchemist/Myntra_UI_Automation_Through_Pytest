# Myntra UI Automation Through Pytest -v1

## Overview
This project automates the homepage of Myntra using Selenium and Python with the Pytest framework. It follows the **Page Object Model (POM)** to keep test scripts clean, modular, and maintainable. Each webpage has a dedicated page object file, which is then used in the test cases.

## Features
- Uses **Selenium WebDriver** for UI automation.
- Implements the **Page Object Model (POM)** for better structure.
- Test execution is handled through the **Pytest** framework.
- Different types of **locators** (XPath, CSS Selectors, etc.) are used.
- **time.sleep()** is used for waits instead of explicit and implicit waits (this can be optimized in future versions).
- **HTML test reports** can be generated for better insights into test results.

## Prerequisites
Make sure you have the following installed:
- Python (3.x recommended)
- Selenium
- Pytest
- WebDriver (ChromeDriver, GeckoDriver, etc.)

Dependencies can be installed the using:
```sh
pip install -r requirements.txt
```

## Running the Tests
To execute the test cases and generate an HTML report, run:
```sh
pytest --html=report.html --self-contained-html
```

To simply run the test cases without a report, use:
```sh
pytest teste2e.py -v -s
```

## Folder Structure
```
Myntra_UI_Automation_Through_Pytest/
│-- pageObjects/      # Contains POM classes for different pages
│-- tests/            # Contains test cases
│-- utilities/        # Utility functions and helpers
│-- requirements.txt  # Required dependencies
│-- README.md         # Project documentation
```

## Future Scope Of Enhancements -v2
- Implement **Explicit Waits** instead of `time.sleep()`.
- Add more test scenarios for better coverage.
- Integrate with CI/CD pipelines like **Jenkins** or **GitHub Actions**.
- Improve reporting using **Allure Reports**.
- **Handle Flakiness**: Introduce retry mechanisms or rerun failed tests to improve test reliability.

This project serves as a starting point for automating UI flows using Pytest and Selenium. Contributions and improvements are always welcome!

