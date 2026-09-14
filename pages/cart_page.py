from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item_label")

    def open(self):
        self.page.locator(".shopping_cart_link").click()
    
    def is_loaded(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")

    def expect_product_visible(self, product_name: str):
        product = self.cart_items.locator(
            ".inventory_item_name"
        ).filter(has_text=product_name)

        expect(product).to_be_visible()
