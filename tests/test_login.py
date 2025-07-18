import pytest
from pages import login_page
from pages.login_page import LoginPage
import config


class TestLogin:
    @pytest.mark.parametrize("username, password, expected", [
        (config.STANDARD_USER, config.CORRECT_PASSWORD, "inventory.html"),
        (config.LOCKED_USER, config.CORRECT_PASSWORD, "Epic sadface: Sorry, this user has been locked out."),
    ])
    def test_login_scenarios(self, browser, username, password, expected):
        login_page = LoginPage(browser)
        login_page.login(username, password)
        assert expected in browser.current_url or expected in login_page.get_error_message()
