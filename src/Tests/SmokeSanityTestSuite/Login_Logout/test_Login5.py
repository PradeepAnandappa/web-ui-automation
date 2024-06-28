from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Login(BaseTest):

    def test_user_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.tick_RememberMe()
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.logout_user()
        page_found = self.loginPage.getPageTitle("Login")
        assert page_found
        accountID = self.loginPage.getAccountValue()
        assert config.AccoundID == accountID
        userName = self.loginPage.getUserNameValue()
        assert config.UserName == userName
        print("User Login Account Id & User name has been remembered by system")
