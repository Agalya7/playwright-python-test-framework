from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def is_loaded(self):
        return self.page.get_by_text("Your Cart").is_visible()

    def expect_product(self, product_name: str):
        product = self.cart_items.filter(has_text=product_name)
        expect(product).to_be_visible()

    def checkout(self):
        self.checkout_button.click()