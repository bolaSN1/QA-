from behave import when, then, given
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart-count')
CART_CONT = (By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart']")

@given('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

@when('click on cart button')
def click_cart_button(context):
    # context.driver.find_element(*CART_CONT).click()
    context.app.cart_page.click_cart_button()


@then('Verify page opens')
def verify_page(context):
    context.app.cart_page.verify_page()