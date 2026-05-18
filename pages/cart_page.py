from selenium.webdriver.common.by import By

class CartPage:
    
    def __init__(self,driver):
        self.driver = driver
        
    cart_item = (By.CLASS_NAME, "inventory_item_name")
    
    def get_cart_item_name(self):
        return self.driver.find_element(*self.cart_item).text
    
    def remove_item_from_cart(self):
        remove_button = (By.ID, "remove-sauce-labs-backpack")
        self.driver.find_element(*remove_button).click()
        
    def click_checkout(self):
        checkout_button = (By.ID, "checkout")
        self.driver.find_element(*checkout_button).click()