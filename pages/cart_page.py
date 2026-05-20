from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    
    def __init__(self,driver):
        self.driver = driver
        
    cart_item = (By.CLASS_NAME, "inventory_item_name")
    remove_button = (By.ID, "remove-sauce-labs-backpack")
    checkout_button = (By.ID, "checkout")
    
    def get_first_item_name(self):
        return self.driver.find_element(*self.cart_item).text
        
    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        
    def remove_backpack_from_cart(self):
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_button)
        )
        remove_button.click()

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_item))