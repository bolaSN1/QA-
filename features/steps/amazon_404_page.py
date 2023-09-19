from selenium.webdriver.common.by import By
from behave import given, when, then


DOG_IMG = (By.CSS_SELECTOR, "img[alt='Dogs of Amazon']")


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)
    print('All windows:', context.driver.window_handles)


@when('Click on a dog image')
def click_on_dog_image(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to a new window')
def switch_new_window(context):
    all_windows = context.driver.window_handles
    print('After window opened:, all windows:', all_windows)
    context.driver.switch_to.window(all_windows[1])


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.get('https://www.aboutamazon.com/news')


@then('Close blog')
def close_blog(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print('After blog closed:, all windows:', all_windows)


@then('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)