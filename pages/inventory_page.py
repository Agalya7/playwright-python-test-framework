import logging

from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

        self.products_title = page.get_by_text("Products")
        #self.backpack = page.get_by_text("Sauce Labs Backpack")
        self.add_to_cart_button = page.get_by_role(
            "button", name="Add to cart"
        )
        self.shopping_cart = page.locator(".shopping_cart_link")

    def is_loaded(self):
        return self.products_title.is_visible()

    def add_product_to_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.get_by_role("button", name="Add to cart").click()
    
    def expect_product_in_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )

        expect(product.get_by_role("button", name="Remove")).to_be_visible()

