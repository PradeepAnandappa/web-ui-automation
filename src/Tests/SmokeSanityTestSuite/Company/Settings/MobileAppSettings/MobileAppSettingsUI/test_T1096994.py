import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Settings.GeneralSettings.GeneralSettingsUI.SettingsPage import SettingsPage
from src.PageObjects.Company.Settings.MobileAppSettings.MobileAppSettingsUI.MobileAppSettingsPage import \
    MobileAppSettingsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_MobileAppSettings(BaseTest):
    @pytestrail.case('C25259', 'C25260', 'C25261')
    def test_MobileAppSettingsUI(self):
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
        self.settingsPage.click_settings_tab("Mobile App")
        time.sleep(5)
        self.mobileAppsettingsPage = MobileAppSettingsPage(self.driver)
        self.mobileAppsettingsPage.select_requiredAttachmentForAttribute("Start", "Task")
        time.sleep(2)
        self.mobileAppsettingsPage.click_SaveBtn()
        time.sleep(5)
        assert self.mobileAppsettingsPage.validate_requiredAttachmentForAttribute("Start", "Task")
        self.mobileAppsettingsPage.remove_selected_requiredAttachmentForAttribute("Start", "Task")
        time.sleep(2)
        self.mobileAppsettingsPage.click_SaveBtn()
        time.sleep(2)



