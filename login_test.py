from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Navegar
driver.get("https://www.saucedemo.com")

#Interactuar
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Verificar
titulo = driver.find_element(By.CLASS_NAME, "title").text
assert titulo == "Products", f"Login fallo. Titulo: {titulo}"

# Cerrar
driver.quit()
print("Test pasó exitosamente.")