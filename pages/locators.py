from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    BASKET_CONFIRM = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner>strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR,".col-sm-6 h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,"p.price_color")

class CommonLocators():
    BASKET_LINK =(By.CSS_SELECTOR,".btn-group a.btn.btn-default")

class BasketPageLocators():
    SHOPPING_LIST=(By.CSS_SELECTOR,"#content_inner p")