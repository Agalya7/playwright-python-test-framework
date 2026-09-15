import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from test_data.products import PRODUCTS


@pytest.mark.parametrize("product", PRODUCTS)
def test_add_product_to_cart(logged_in_page, product):
    inventory_page = InventoryPage(logged_in_page)

    expect(inventory_page.products_title).to_be_visible()
    inventory_page.add_product_to_cart(product)
    inventory_page.expect_product_in_cart(product)

    inventory_page.shopping_cart.click()

    cart_page = CartPage(logged_in_page)
    
    expect(cart_page.cart_items.filter(has_text=product)).to_be_visible()

