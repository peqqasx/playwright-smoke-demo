from playwright.sync_api import expect
from config.config import RECOVERY_URL


class RecoveryPage:
    def __init__(self, page):
        self.page = page

        self.email_input = page.locator("#userName")
        self.submit_button = page.locator("#submit")
        self.confirmation_text = page.locator("#content")

    def open(self):
        self.page.goto(RECOVERY_URL)

    def submit_recovery(self, email: str):
        self.email_input.fill(email)
        self.submit_button.click()

    def assert_recovery_requested(self):
        expect(self.confirmation_text).to_contain_text(
            "Check your email"
        )
