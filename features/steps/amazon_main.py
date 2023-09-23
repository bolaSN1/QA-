from selenium.webdriver.common.by import By
from behave import given, when, then


FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")


@when('Hover over language options')
def hover_lang(context):
    context.app.header_page.hover_lang()


@then('Verify Spanish option present')
def verify_spanish_lang_present(context):
    # context.driver.wait.until(EC.presence_of_element_located(*SPANISH_LANG))
    context.app.header_page.verify_spanish_lang_present()



@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))
    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) # 32
    print(type(links_count))
    # 32 == 32
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'
