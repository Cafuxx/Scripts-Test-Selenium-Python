from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver

    add_backpack_button = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    remove_backpack_button = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    cart_icon = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    cart_badge = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    sort_dropdown = (
        By.CLASS_NAME,
        "product_sort_container"
    )

    product_prices = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    def open(self):
        self.driver.get(self.URL)

    def add_backpack_to_cart(self):
        self.driver.find_element(
            *self.add_backpack_button
        ).click()

    def remove_backpack_from_cart(self):
        self.driver.find_element(
            *self.remove_backpack_button
        ).click()

    def go_to_cart(self):
        self.driver.find_element(
            *self.cart_icon
        ).click()

    def get_cart_badge_count(self):

        badges = self.driver.find_elements(
            *self.cart_badge
        )

        if not badges:
            return 0

        return int(badges[0].text)

    def sort_products_by_price_low_to_high(self):

        dropdown = Select(
            self.driver.find_element(
                *self.sort_dropdown
            )
        )

        dropdown.select_by_value("lohi")

    def get_product_prices(self):

        price_elements = self.driver.find_elements(
            *self.product_prices
        )

        return [
            float(price.text.replace("$", ""))
            for price in price_elements
        ]