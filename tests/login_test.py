import pytest

from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")])

def test_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert "inventory" in driver.current_url