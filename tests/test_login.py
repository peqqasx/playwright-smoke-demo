import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from config.config import PROFILE_URL


@pytest.mark.smoke
def test_login_success(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username="testuser", password="Password123!")

    expect(page).to_have_url(PROFILE_URL)


def test_login_invalid_password(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username="testuser", password="wrong_password")

    login_page.assert_error_visible()
