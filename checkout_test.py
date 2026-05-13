from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Configurar opciones de Chrome
options = Options()
options.add_argument("--start-maximized")

# Desactivar alertas de contraseñas comprometidas
options.add_argument("--disable-password-manager-reauthentication")
options.add_argument("--disable-save-password-bubble")

prefs = {"credentials_enable_service": False, 
         "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)

# Iniciar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.implicitly_wait(10)

# Navegar
driver.get("https://www.saucedemo.com/")

# Iniciar sesion
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Reducir velocidad
time.sleep(3)

# Agregar producto
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(3)

# Entrar al carrito
driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
time.sleep(3)

# Click en checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(3)

# Completar formulario
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Johnson")
driver.find_element(By.ID, "postal-code").send_keys("12345")
time.sleep(3)

# Click en continue
driver.find_element(By.ID, "continue").click()
time.sleep(3)

# Verificar que aparece "checkout: overview"
assert driver.find_element(By.CLASS_NAME, "title").text == "Checkout: Overview", "No se encontro el titulo 'Checkout: Overview'"
print("Test completado exitosamente")
