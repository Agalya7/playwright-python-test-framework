# Playwright Python Test Automation Framework

## Overview

A maintainable end-to-end test automation framework built with **Playwright, Python, and pytest**.

The project demonstrates practical automation engineering practices including Page Object Model, reusable fixtures, parameterized testing, cross-browser testing, failure diagnostics, reporting, and CI execution.

## Tech Stack

* Python
* Playwright
* pytest
* GitHub Actions
* Git

## Framework Features

* **Page Object Model (POM)** for maintainable UI automation
* **Reusable pytest fixtures** for test setup and page objects
* **Parameterized tests** for data-driven test execution
* **Cross-browser testing** across Chromium, Firefox, and WebKit
* **Extensible architecture for UI and API automation**
* **Failure screenshots** for easier debugging
* **HTML test reports**
* **Centralized test configuration**
* **CI execution with GitHub Actions**
* **Reusable test data management**
* **Positive and negative test scenarios**
* **End-to-end checkout workflow validation**

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── test_data/
│   └── products.py
├── tests/
│   ├── test_login.py
│   └── test_inventory.py
├── utils/
│   └── logger.py
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Architecture

```text
Test Cases
    ↓
Pytest Fixtures
    ↓
Page Objects
    ↓
Playwright
    ↓
Web Application
```

Page objects encapsulate UI interactions and locators, while fixtures provide reusable test setup. Tests focus on **business scenarios and assertions** rather than implementation details.

## Test Coverage

The framework currently covers:

* Login validation
* Product selection
* Add-to-cart workflows
* Multiple-product cart scenarios
* Checkout validation
* Required-field validation
* Product and price verification
* Order subtotal, tax, and total validation
* Order completion
* Cross-browser execution

## Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run the test suite:

```bash
pytest
```

Run a specific browser:

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

## CI/CD

Tests are executed through **GitHub Actions** to validate the framework automatically in CI.

The workflow runs the automated test suite and provides a repeatable validation process for changes.

## Reporting & Debugging

The framework provides:

* HTML test reports
* Automatic screenshots for failed tests
* Logging support
* Playwright's built-in test diagnostics

These features help reduce debugging time when investigating failed automation runs.

## Why This Project

This project is designed to demonstrate how I approach test automation beyond writing individual test cases:

* Building reusable automation components
* Designing maintainable test architecture
* Reducing duplication through fixtures and Page Objects
* Supporting multiple browsers
* Automating regression scenarios
* Integrating automated tests into CI/CD
* Designing tests for both positive and negative scenarios
* Making failures easier to investigate
