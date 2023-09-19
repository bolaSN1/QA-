from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from app.application import Application
from support.logger import logger


# def browser_init(context):

def browser_init(context):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    ####### GOOGLE CHROME ######################
    service = Service(executable_path="/Users/priscillao/QA/Bola Project/chromedriver")
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    ############################################

    ######## HEADLESS MODE ########################
    # service = Service(executable_path=r'C/Users/priscillao/QA/Bola Project/chromedriver')
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # context.driver = webdriver.Chrome(options=options,service=service)
    ###############################################

    ##################### FIREFOX #########################
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(executable_path='/Users/priscillao/QA/Bola Project/geckodriver')
    # options = webdriver.FirefoxOptions()
    # context.driver = webdriver.Firefox(service=service,options=options)
    ########################################################

    ###################### BROWSERSTACK######################
    # options = ChromeOptions()
    # bs_user = 'bolanleoso_tj7eAn'
    # bs_key = 'sYVfdEQpAKsppEKyy5qK'
    #
    # # Setting the capabilities
    # caps = {
    #     "os": "OS X",
    #     "osVersion": "Ventura",
    #     "sessionName": test_name
    # }
    #
    # options.set_capability('bstack:options', caps)
    # options.set_capability('browserVersion', '95')
    # options.set_capability('browserName', 'Chrome')
    #
    # # connecting the test to Browserstack
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(
    #     command_executor=url,
    #     options=options)
    #################################################################

    ##################### MOBILE EMULATION ############################
    # service = Service()
    # options = webdriver.ChromeOptions()
    # # mobile_emulation = { "deviceName": "Samsung Galaxy S8+" }
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 740 },
    #                  "clientHints": {"platform": "Android", "mobile": True}}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(service=service,options=options)

    ##################################################################################

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
