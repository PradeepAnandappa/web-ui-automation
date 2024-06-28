from pytest_testrail.plugin import pytestrail

from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Login(BaseTest):
    @pytestrail.case('C31420')
    def test_user_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, "UserName", "Password")
        alert_found = self.loginPage.is_ErrorAlertPresent()
        assert alert_found
        print("Invalid UserName & Password")
