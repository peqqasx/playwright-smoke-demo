from pages.recovery_page import RecoveryPage


def test_user_can_request_password_recovery(page):
    recovery_page = RecoveryPage(page)

    # Arrange
    recovery_page.open()

    # Act
    recovery_page.submit_recovery(email="testuser@example.com")

    # Assert
    recovery_page.assert_recovery_requested()
