from selenium.webdriver.common.by import By

from pages_or.base_page_or import BasePage_OR


class HomePage_OR(BasePage_OR):
    def __init__(self, driver):
        self.driver = driver

        self.logo = (By.CSS_SELECTOR, "img.logo")
        self.header = (By.CSS_SELECTOR, "img.logo + span")
        self.account_link = (By.ID, "navbarAccount")
        self.login_button = (By.ID, "navbarLoginButton")
        self.dismiss_btn = (By.XPATH, "//span[text()='Dismiss']")
