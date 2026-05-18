from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_cart_validation(driver):

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Agregar producto al carrito
    inventory_page.open()
    inventory_page.add_backpack_to_cart()

    # Ir al carrito
    inventory_page.go_to_cart()

    # Validar producto agregado
    assert cart_page.get_first_item_name() == "Sauce Labs Backpack"