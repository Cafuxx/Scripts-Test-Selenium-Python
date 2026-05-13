from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Configurar opciones de Chrome
options = Options()
options.add_argument("--start-maximized")  # Iniciar maximizado

# Desactivar alertas de contraseñas comprometidas
options.add_argument("--disable-password-manager-reauthentication")
options.add_argument("--disable-save-password-bubble")

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

options.add_experimental_option("prefs", prefs)

# Iniciar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

# Navegar
driver.get("https://www.saucedemo.com/")

# Iniciar sesion
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Reducir velocidad
time.sleep(2)

# Agregar al carrito
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)

# Verificar que el producto se agregó al carrito
boton_remove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
assert boton_remove.is_displayed(), "El producto no se agrego al carrito"

# Eliminar del carrito
boton_remove.click()
time.sleep(2)

# Verificar
boton_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
assert boton_add.is_displayed(), "El producto no se elimino del carrito"

# Cerrar el navegador
driver.quit()
print("Test paso exitosamente")
