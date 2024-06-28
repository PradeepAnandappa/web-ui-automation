from pytest_testrail.plugin import pytestrail

from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage_oldUI import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Login(BaseTest):
    @pytestrail.case('C31407')
    def test_user_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_loginByEmail(config.Email, config.Password1)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Tracking")
        assert page_found
        print("Admin has been logged in successfully thru old UI")
