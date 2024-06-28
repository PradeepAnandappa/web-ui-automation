import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Settings.GeneralSettings.GeneralSettingsUI.SettingsPage import SettingsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_GeneralSettings(BaseTest):
    @pytestrail.case('C25005', 'C24991')
    def test_GeneralSettingsUI(self):
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

        self.settingsPage.update_EmployeeNomenclature("Emp")
        time.sleep(5)
        self.leftNavigationPanelPage.click_Monitor()
        time.sleep(5)
        assert self.monitorPage.validate_Table_columnsName("Emp Number")
        assert self.monitorPage.validate_columnName_under_filter("Emp Number")
        self.leftNavigationPanelPage.click_Company()
        time.sleep(2)
        self.employeesPage.click_company_icon("Settings")
        time.sleep(5)
        self.settingsPage.update_EmployeeNomenclature("Employee")
        time.sleep(5)
        self.leftNavigationPanelPage.click_Monitor()
        assert self.monitorPage.validate_Table_columnsName("Employee Number")
        assert self.monitorPage.validate_columnName_under_filter("Employee Number")


