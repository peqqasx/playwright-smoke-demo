from playwright.sync_api import expect
from config.config import RECOVERY_URL


class RecoveryPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(RECOVERY_URL)

    def assert_page_opened(self):
        expect(self.page).to_have_url(RECOVERY_URL)
