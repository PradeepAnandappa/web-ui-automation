import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Settings.GeneralSettings.GeneralSettingsUI.SettingsPage import SettingsPage
from src.PageObjects.Company.Settings.PayrollSettings.PayrollSettingsUI.PayRollSettingsPage import PayRollSettingsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_PayRollSettings(BaseTest):
    @pytestrail.case('C25038')
    def test_PayRollSettingsUI(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(5)
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Settings")
        self.settingsPage = SettingsPage(self.driver)
        time.sleep(5)
        page_found = self.settingsPage.getPageTitle("Settings")
        assert page_found
        self.settingsPage.click_settings_tab("Payroll")
        time.sleep(5)
        self.payRollSettingsPage = PayRollSettingsPage(self.driver)
        self.payRollSettingsPage.validate_pageHeader()

        self.payRollSettingsPage.enterRegular_EarningCode("RG101")
        self.payRollSettingsPage.click_SaveBtn()
        time.sleep(2)
        rgCode = self.payRollSettingsPage.getRegular_EarningCode()
        assert "RG101" == rgCode
        self.payRollSettingsPage.clear_Regular_EarningCode()

