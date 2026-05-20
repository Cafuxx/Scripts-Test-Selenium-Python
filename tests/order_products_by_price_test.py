from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.regression
def test_order_products_by_price(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page.sort_products_by_price_low_to_high()

    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices)