from selenium.webdriver.common.by import By
from behave import given, when,then
from time import sleep

CAREER_BTN = (By.CSS_SELECTOR, 'div.footer-links')
RIGHTMENU_BTN = (By.CSS_SELECTOR, 'div.nav-button-wrapper')

@given('open camber creative homepage')
def open_camber(context):
    context.driver.get('https://www.cmbr.co/')

@given('user can click the top right menu button')
def top_right_menu(context):
    context.app.camber_page.top_right_menu()
    sleep(3)

@when('user selects {expected_text} from the menu')
def select_careers(context, expected_text):
    context.app.camber_page.select_careers()

@then('verify careers page opens')
def verify_page_opens(context):
    context.app.camber_page.verify_page_opens()

