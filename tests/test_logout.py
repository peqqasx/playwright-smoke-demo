from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_user_can_logout(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Arrange
    login_page.open()
    login_page.login(username="testuser", password="Password123!")

    # Act
    dashboard_page.logout()

    # Assert
    dashboard_page.assert_logged_out()
