from pytest_testrail.plugin import pytestrail

from src.PageObjects.Login_Logout.AdminLoginPage import AdminLoginPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser


class Test_Login(BaseTest):
    @pytestrail.case('C31415', 'C31409')
    def test_user_login(self):
        self.adminLoginPage = AdminLoginPage(self.driver)
        self.adminLoginPage.validateComponents()
        print("Admin Login page components available")
