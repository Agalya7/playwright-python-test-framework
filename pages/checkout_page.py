from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.overview_title = page.locator('[data-test="title"]')
        self.product_name = page.locator('[data-test="inventory-item-name"]')
        self.product_price = page.locator('[data-test="inventory-item-price"]')
        self.subtotal = page.locator('[data-test="subtotal-label"]')
        self.tax = page.locator('[data-test="tax-label"]')
        self.total = page.locator('[data-test="total-label"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('[data-test="complete-header"]')
        self.error_message = page.locator('[data-test="error"]')

    def expect_required_field_error(self, field_name):
        expect(self.error_message).to_have_text(f"Error: {field_name} is required")

    def enter_customer_information(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

    def expect_product_details(self, product, expected_price):
        expect(self.product_name).to_have_text(product)
        expect(self.product_price).to_have_text(f"${expected_price:.2f}")

    def expect_order_totals(self, expected_price):
        expect(self.subtotal).to_have_text(f"Item total: ${expected_price:.2f}")

        expected_tax = round(expected_price * 0.08, 2)
        expect(self.tax).to_have_text(f"Tax: ${expected_tax:.2f}")

        expected_total = round(expected_price + expected_tax, 2)
        expect(self.total).to_have_text(f"Total: ${expected_total:.2f}")

    def finish_order(self):
        self.finish_button.click()

    def expect_checkout_completion(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")
