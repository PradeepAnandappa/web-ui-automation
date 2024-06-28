import time

from pytest_testrail.plugin import pytestrail
import allure
from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Signup.SignupPage import SignupPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Signup(BaseTest):
    @pytestrail.case('C31392')
    def test_user_signup(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_TrailAccountLink()
        self.signupPage = SignupPage(self.driver)
        page_found = self.signupPage.getPageTitle("Free Trial")
        assert page_found
        self.signupPage.close_chatpanel()
        self.signupPage.signup_user("Test user", "Hike QA", "8447760115", "test.allgeo@gmail.com", "GMT+05:30")
        time.sleep(2)
