# Selenium CI/CD Pipeline using Jenkins (Python + Pytest)

This project demonstrates an end-to-end **CI/CD pipeline** for executing **Selenium automation tests** using **Python, Pytest, and Jenkins**.  
The pipeline is triggered automatically from GitHub and publishes test execution reports in Jenkins.

---

##  Tech Stack

- **Language:** Python 3.x  
- **Automation Tool:** Selenium WebDriver  
- **Test Framework:** Pytest  
- **CI/CD Tool:** Jenkins  
- **Version Control:** Git & GitHub  
- **Reporting:** Pytest HTML Report  

---

##  Project Structure

selenium-ci-cd/
│
├── .venv/                 → Local virtual environment (DO NOT push to GitHub)
│
├── pages/                 → Page Objects
│   └── login_page.py
│
├── tests/                 → Test cases
│   ├── assets/            → Test data / screenshots (optional)
│   └── test_login.py
│
├── utils/                 → Reusable utilities
│   └── driver_factory.py
│
├── reports/               → Test execution reports
│   ├── assets/
│   └── report.html
│
├── conftest.py            → Pytest fixtures
├── pytest.ini             → Pytest configuration
├── Jenkinsfile            → CI/CD pipeline
├── requirements.txt       → Dependencies
└── .gitignore             → Ignore venv, reports, cache



---

##  Jenkins CI/CD Pipeline Flow

1. Checkout source code from GitHub  
2. Verify Python installation  
3. Create Python virtual environment  
4. Install project dependencies  
5. Execute Selenium tests using Pytest  
6. Generate and publish HTML test report in Jenkins  

---

## How to Run Tests Locally

### Clone Repository

git clone https://github.com/pavan1613/selenium-ci-cd.git
cd selenium-ci-cd
Create Virtual Environment

python -m venv .venv
 Activate Virtual Environment
Windows

.venv\Scripts\activate
 Install Dependencies

pip install -r requirements.txt
 Run Tests

pytest --html=reports/report.html --self-contained-html

## Jenkinsfile Highlights
Uses Declarative Pipeline

Runs on Windows Jenkins agent

Handles virtual environment creation

Publishes HTML reports using HTML Publisher Plugin

## Test Report
After successful execution:

Jenkins displays HTML test report

Report includes:

Passed / Failed test cases

Execution time

Error screenshots (if configured)

## GitHub Authentication
GitHub access is configured using Personal Access Token (PAT)

Jenkins credentials securely store the token

## Author
Pavan Kumar Balusupati
QA Automation Engineer | Selenium | Python | Jenkins
