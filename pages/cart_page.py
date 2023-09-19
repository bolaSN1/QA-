from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class CartPage(Page):
    CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
    CART_CONT = (By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart']")


    def click_cart_button(self):
        return self.driver.find_element(*self.CART_CONT).click()


    def verify_page(self):
        self.open_url('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
