from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button=self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def check_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name not found"
        assert self.is_element_present(*ProductPageLocators.BASKET_CONFIRM), "name in basket not found"
        product_name= self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_confirm = self.browser.find_element(*ProductPageLocators.BASKET_CONFIRM).text
        assert product_name == product_confirm, "product name in basket not match"

    def check_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "product price not found"
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "price in not found"
        product_price= self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price= self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "product price in basket not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_CONFIRM),"Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_CONFIRM), "Success message should disappear, but still is presented"

