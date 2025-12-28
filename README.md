This project demonstrates a production-like QA Automation setup for testing authentication flows using Playwright + pytest.
The focus is on:

- clean architecture
- realistic scope
- stable smoke tests
- CI integration

The project intentionally avoids overengineering and reflects how UI automation is commonly implemented in real commercial projects.

Covered Scenarios:

1. Authentication (Auth Suite)
    - Login
      - Successful login with valid credentials
      - Redirect to user dashboard
    - Logout
      - Logout from authenticated session
      - Redirect back to login page
    - Password Recovery (UI Smoke)
      - Navigation to "Forgot Password" page
      - Page availability check

2. Smoke Test Strategy
   - The project includes a smoke test suite covering the most critical authentication paths:
     - Login success
     - Logout success
     - Password recovery page availability
   - Smoke tests are marked with @pytest.mark.smoke and are designed to:
      - Run fast
      - Be stable
      - Validate application availability
   - Run smoke tests locally:
      `pytest -m smoke`

3. Project Structure

    playwright-smoke-demo/
    ├── pages/                  # Page Object layer
    │   ├── login_page.py
    │   ├── dashboard_page.py
    │   └── recovery_page.py
    │
    ├── tests/                  # Test cases
    │   ├── test_login.py
    │   ├── test_logout.py
    │   └── test_password_recovery.py
    │
    ├── config/                 # Configuration
    │   └── config.py
    │
    ├── .github/workflows/      # CI configuration
    │   └── smoke-tests.yml
    │
    ├── pytest.ini              # Pytest markers
    ├── requirements.txt
    └── README.md

4. Architecture Principles
    - Page Object Pattern
    - Single Responsibility Principle
    - One test = one test case
    - Clear separation between test logic and UI interactions

5. CI Integration

    The project uses GitHub Actions to run smoke tests automatically.
    CI Behavior:
    - Triggered on every push and pull request to main
    - Runs on Ubuntu runner
    - Installs dependencies and Playwright Chromium
    - Executes only smoke tests
    CI configuration can be found here:
    `.github/workflows/smoke-tests.yml`

6. Security Considerations

    For simplicity, this project does not require any sensitive data to run.

    However, if credentials or tokens were needed in a real project, the setup would be handled via environment
    variables or CI secrets, not hardcoded values.

    Examples:
    - Local runs can use a .env file (excluded from version control)
    - CI pipelines can use GitHub Actions Secrets
   
    This approach allows:
    - keeping sensitive data out of the repository
    - safely running tests in CI
    - using different credentials per environment (local / CI / staging)

7. Tech Stack
   - Python 3.11
   - Playwright
   - pytest
   - GitHub Actions