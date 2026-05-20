from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_cart_validation(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Agregar producto
    inventory_page.add_backpack_to_cart()

    # Ir al carrito
    inventory_page.go_to_cart()

    # Validar producto
    assert cart_page.get_first_item_name() == "Sauce Labs Backpack"