from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_checkout(driver):

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Agregar producto
    inventory_page.open()
    inventory_page.add_backpack_to_cart()

    # Ir al carrito
    inventory_page.go_to_cart()

    # Validar producto agregado
    assert cart_page.get_cart_items_count() == 1

    # Checkout
    cart_page.click_checkout()

    checkout_page.fill_checkout_form(
        "Juan",
        "Perez",
        "73412"
    )

    checkout_page.click_continue()

    # Validar que el producto siga presente en el checkout
    assert checkout_page.get_first_item_name() == "Sauce Labs Backpack"