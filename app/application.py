from pages.camber_page import CamberPage
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.camber_page = CamberPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)



