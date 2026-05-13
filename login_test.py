from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)

# Navegar
driver.get("https://www.saucedemo.com")

# Interactuar
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
).send_keys("secret_sauce")

wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
).click()

# Verificar
titulo = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "title"))
).text

assert titulo == "Products", f"Login fallo. Titulo: {titulo}"

# Cerrar
driver.quit()

print("Test paso exitosamente.")