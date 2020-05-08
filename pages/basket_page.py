from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        count = len(self.browser.find_elements(*BasketPageLocators.SHOPPING_LIST))
        assert count == 1, "basket is not empty!"
