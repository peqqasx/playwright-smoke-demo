from playwright.sync_api import expect
from config.config import LOGIN_URL


class DashboardPage:
    def __init__(self, page):
        self.page = page

        self.logout_button = page.locator("#submit")

    def logout(self):
        self.logout_button.click()

    def assert_logged_out(self):
        expect(self.page).to_have_url(LOGIN_URL)
