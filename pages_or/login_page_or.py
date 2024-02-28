from selenium.webdriver.common.by import By

from pages_or.base_page_or import BasePage_OR


class LoginPage_OR(BasePage_OR):
    def __init__(self, driver):
        self.driver = driver

        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")
