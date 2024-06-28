import time

from pytest_testrail.plugin import pytestrail

from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Login(BaseTest):
    @pytestrail.case('C31402')
    def test_user_login(self):
        self.loginPage = LoginPage(self.driver)

        self.loginPage.user_login(config.ManagerAccoundID, config.ManagerUserName, config.ManagerPassword)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        print("Manager has been logged in successfully thru new UI")
