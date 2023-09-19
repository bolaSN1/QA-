from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, 'i.sprite svg-search-icon')
SEARCH_BAR = (By.ID, 'input#searchInput')


@given('Open wikipedia org')
def open_wiki_org(context):
    context.driver.get('https://www.wikipedia.org/')


@given('Input {search_query} into search field')
def input_search(context, search_query):
    search_bar = context.driver.find_element(*SEARCH_INPUT)
    search_query = "python"
    search_bar.clear()
    search_bar.send_keys(search_query)
    sleep(4)


@then('Verify python is on the results')
def verify_search(context):
    search_query = context.driver.find_element(*SEARCH_INPUT)
    assert search_query, f"Search query {search_query} not in {verify_search}"
    print("Test case passed")