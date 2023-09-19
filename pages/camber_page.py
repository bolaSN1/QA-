from selenium.webdriver.common.by import By
from pages.base_page import Page


class CamberPage(Page):
    CAREER_BTN = (By.CSS_SELECTOR, 'div.footer-links')
    RIGHTMENU_BTN = (By.CSS_SELECTOR, 'div.nav-button-wrapper')
    CAREER_PAGE = (By.XPATH, "//a[@href='https://camber-creative.breezy.hr/']")

    def top_right_menu(self):
        self.find_element(*self.RIGHTMENU_BTN).click()

    def select_careers(self):
        self.find_elements(*self.CAREER_BTN)

    def verify_page_opens(self):
        self.find_element(*self.CAREER_PAGE).click()
        print(f'Lets make something delightful together.')