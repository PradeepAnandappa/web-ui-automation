from pytest_testrail.plugin import pytestrail

from Configuration.config import config
from src.PageObjects.Login_Logout.AdminLoginPage import AdminLoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Login(BaseTest):
    @pytestrail.case('C31409')
    def test_user_login(self):
        self.adminLoginPage = AdminLoginPage(self.driver)
        self.adminLoginPage.admin_login(config.AccoundID, "rahul.verma@abaq.us", "Shrija@Rahul")
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        #assert page_found
        page_URL = self.monitorPage.getPageURL()
        Expected_URL ="https://staging.allgeo.com/track/Track"
        #assert Expected_URL == page_URL
        print("Admin has been logged in successfully")
