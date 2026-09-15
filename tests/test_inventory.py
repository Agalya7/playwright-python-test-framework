import pytest
from playwright.sync_api import Page, expect

from test_data.products import PRODUCTS


@pytest.mark.parametrize("product", PRODUCTS)
def test_purchase_product(pages, product):
    inventory_page = pages["inventory"]
    cart_page = pages["cart"]
    checkout_page = pages["checkout"]

    expect(inventory_page.products_title).to_be_visible()
    product_name = product["name"]
    product_price = product["price"]
    inventory_page.add_product_to_cart(product_name)
    inventory_page.expect_product_in_cart(product_name)
    inventory_page.shopping_cart.click()

    expect(cart_page.cart_items.filter(has_text=product_name)).to_be_visible()
    cart_page.checkout_button.click()

    checkout_page.enter_customer_information("User", "Test", "10101")
    checkout_page.click_continue()
    expect(checkout_page.overview_title).to_have_text("Checkout: Overview")
    checkout_page.expect_product_details(product_name, product_price)
    checkout_page.expect_order_totals(product_price)
    checkout_page.finish_order()
    checkout_page.expect_checkout_completion()

def test_cart_with_multiple_products(pages):
    inventory_page = pages["inventory"]
    cart_page = pages["cart"]

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    ]

    for product in products:
        inventory_page.add_product_to_cart(product)

    inventory_page.shopping_cart.click()

    for product in products:
        expect(cart_page.cart_items.filter(has_text=product)).to_be_visible()

    expect(cart_page.cart_items).to_have_count(3)

def test_checkout_requires_first_name(pages):
    inventory_page = pages["inventory"]
    cart_page = pages["cart"]
    checkout_page = pages["checkout"]

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.shopping_cart.click()

    cart_page.checkout_button.click()

    checkout_page.click_continue()
    checkout_page.expect_required_field_error("First Name")

def test_checkout_requires_last_name(pages):
    inventory_page = pages["inventory"]
    cart_page = pages["cart"]
    checkout_page = pages["checkout"]

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.shopping_cart.click()

    cart_page.checkout_button.click()

    checkout_page.enter_customer_information("User", "", "10101")
    checkout_page.click_continue()
    checkout_page.expect_required_field_error("Last Name")

def test_checkout_requires_postal_code(pages):
    inventory_page = pages["inventory"]
    cart_page = pages["cart"]
    checkout_page = pages["checkout"]

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.shopping_cart.click()

    cart_page.checkout_button.click()

    checkout_page.enter_customer_information("User", "Test", "")
    checkout_page.click_continue()
    checkout_page.expect_required_field_error("Postal Code")

