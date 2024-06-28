import time

from pytest_testrail.plugin import pytestrail

from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Login(BaseTest):
    @pytestrail.case('C31404')
    def test_user_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        time.sleep(2)
        flag = self.monitorPage.validate_parent_child_tree_under_user_profile()
        assert flag
        print("Parent-Child relation found")
