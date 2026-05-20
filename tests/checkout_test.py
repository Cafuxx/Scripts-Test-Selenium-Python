import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "first_name, last_name, postal_code",
    [
        ("John", "Moreno", "96042"),
        ("Jane", "Doe", "12345"),
    ]
)
def test_checkout(
    driver,
    first_name,
    last_name,
    postal_code
):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

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

    # Ir al checkout
    cart_page.click_checkout()

    # Completar formulario
    checkout_page.fill_checkout_form(
        first_name,
        last_name,
        postal_code
    )

    checkout_page.click_continue()

    # Validar navegación
    assert "checkout-step-two" in driver.current_url