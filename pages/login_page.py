from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "wrong login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self,email, password):
        mail=self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        mail.send_keys(email)
        passw=self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        passw.send_keys(password)
        conf=self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        conf.send_keys(password)
        but=self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        but.click()
