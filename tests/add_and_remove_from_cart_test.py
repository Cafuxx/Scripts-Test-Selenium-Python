import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.regression
def test_add_and_remove_from_cart(driver):
    
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Agregar producto
    inventory_page.open()
    inventory_page.add_backpack_to_cart()

    # Ir al carrito
    inventory_page.go_to_cart()

    # Validar producto agregado
    assert cart_page.get_first_item_name() == "Sauce Labs Backpack"

    # Eliminar producto
    cart_page.remove_backpack_from_cart()

    # Validar carrito vacío
    assert cart_page.get_cart_items_count() == 0