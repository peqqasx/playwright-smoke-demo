from playwright.sync_api import Page, expect
from config.config import LOGIN_URL


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = page.locator("#userName")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login")
        self.error_message = page.locator("#name")

    def open(self):
        self.page.goto(LOGIN_URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_visible(self):
        expect(self.error_message).to_be_visible()
