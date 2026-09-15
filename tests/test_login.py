from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()

def test_login_with_invalid_username(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("invalid_user", "secret_sauce")

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "invalid_password")

    expect(login_page.error_message).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
