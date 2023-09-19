from selenium.webdriver.common.by import By
from behave import then,when

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')
ORDERS_BTN = (By.ID, 'nav-orders')


@then('Verify Sign In page opens')
def verify_signin_opens(context):
    context.driver.find_element(*EMAIL)
    context.app.sign_in_page.verify_signin_opens()

@when('Click Orders')
def click_orders(context):
    element = context.driver.find_element(*ORDERS_BTN)
    print('Before refresh: ', element)
    context.driver.refresh()
    element = context.driver.find_element(*ORDERS_BTN)
    print('After refresh: ', element)
    element.click()