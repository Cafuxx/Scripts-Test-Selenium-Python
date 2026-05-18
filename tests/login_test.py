from pages.login_page import LoginPage

def test_login_exitoso(driver):
    page = LoginPage(driver).open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    
def test_login_fallido(driver):
    page = LoginPage(driver).open()
    page.login("usuario_invalidado", "pass_malo")
    assert "Username and password do not match" in page.get_error_message()