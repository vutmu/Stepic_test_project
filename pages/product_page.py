from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button=self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()