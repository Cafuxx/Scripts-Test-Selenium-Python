from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Configurar opciones de Chrome
options = Options()
options.add_argument("--start-maximized")

# Desactivar alertas de contraseñas
options.add_argument("--disable-password-manager-reauthentication")
options.add_argument("--disable-save-password-bubble")

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

options.add_experimental_option("prefs", prefs)

# Iniciar navegador
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 10)

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

# Encontrar dropdown
dropdown_element = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))
)

# Crear objeto Select
dropdown = Select(dropdown_element)

# Ordenar por precio menor a mayor
dropdown.select_by_visible_text("Price (low to high)")

# Obtener todos los precios
price_elements = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
)

# Convertir precios a float
precios = []

for element in price_elements:
    precio_texto = element.text.replace("$", "")
    precios.append(float(precio_texto))

# Validar ordenamiento
assert precios == sorted(precios), "Los productos no están ordenados correctamente"

# Cerrar navegador
driver.quit()

print("Test paso exitosamente")
