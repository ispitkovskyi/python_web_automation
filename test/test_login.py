import logging

import pages.home_page  # do not use 'from' when importing pages
from assets.constants import *
from utility.drivermanager import DriverManager

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class TestFacebookLogin(DriverManager):

    def test_login(self):
        home_page = pages.home_page.HomePage(self.driver)
        home_page.click_dismiss_btn()
        home_page.verify_welcome_page()
        login_page = home_page.click_login_button()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()
