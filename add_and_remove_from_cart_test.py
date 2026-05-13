from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

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

wait = WebDriverWait(driver,10)

# Navegar
driver.get("https://www.saucedemo.com/")

# Iniciar sesion
wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
).send_keys("secret_sauce")

wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
).click()

# Agregar al carrito
wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
).click()

# Verificar agregado
boton_remove = wait.until(
    EC.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack"))
)

assert boton_remove.is_displayed(), "El producto no se agrego"

# Eliminar del carrito
boton_remove.click()

# Verificar eliminado
boton_add = wait.until(
    EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
)

assert boton_add.is_displayed(), "El producto no se elimino del carrito"

# Cerrar el navegador
driver.quit()
print("Test paso exitosamente")
