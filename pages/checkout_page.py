from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    first_name_input = (
        By.ID,
        "first-name"
    )

    last_name_input = (
        By.ID,
        "last-name"
    )

    postal_code_input = (
        By.ID,
        "postal-code"
    )

    continue_button = (
        By.ID,
        "continue"
    )

    cart_item_name = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    def fill_checkout_form(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.driver.find_element(
            *self.first_name_input
        ).send_keys(first_name)

        self.driver.find_element(
            *self.last_name_input
        ).send_keys(last_name)

        self.driver.find_element(
            *self.postal_code_input
        ).send_keys(postal_code)

    def click_continue(self):

        self.driver.find_element(
            *self.continue_button
        ).click()

    def get_first_item_name(self):

        return self.driver.find_element(
            *self.cart_item_name
        ).text