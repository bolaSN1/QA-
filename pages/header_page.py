from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page



class Header(Page):
    FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")



    def hover_lang(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_spanish_lang_present(self):
        self.find_element(*self.SPANISH_LANG).click()

