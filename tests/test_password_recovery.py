import pytest
from pages.recovery_page import RecoveryPage


@pytest.mark.smoke
def test_user_can_open_password_recovery_page(page):
    recovery_page = RecoveryPage(page)

    recovery_page.open()
    recovery_page.assert_page_opened()
