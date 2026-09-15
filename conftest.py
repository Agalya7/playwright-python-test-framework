import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from config import USERNAME, PASSWORD


@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)

    return page

@pytest.fixture
def pages(logged_in_page):
    return {
        "inventory": InventoryPage(logged_in_page),
        "cart": CartPage(logged_in_page),
        "checkout": CheckoutPage(logged_in_page),
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"\nScreenshot saved: {screenshot_path}")
