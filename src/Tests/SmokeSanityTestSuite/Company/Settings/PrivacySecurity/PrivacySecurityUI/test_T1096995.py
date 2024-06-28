import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Settings.GeneralSettings.GeneralSettingsUI.SettingsPage import SettingsPage
from src.PageObjects.Company.Settings.PrivacySecurity.PrivacySecurityUI.PrivacySecuritySettingsPage import \
    PrivacySecuritySettingsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_PrivacySecuritySettings(BaseTest):
    @pytestrail.case('C25294', 'C25295', 'C25296', 'C25298', 'C25315', 'C25311')
    def test_PrivacySecuritySettingsUI(self):
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
        self.settingsPage.click_settings_tab("Security & Privacy")
        time.sleep(5)
        self.privacySecuritySettingsPage = PrivacySecuritySettingsPage(self.driver)
        assert self.privacySecuritySettingsPage.validate_pageHeader()
        self.privacySecuritySettingsPage.click_settings_tab("Legacy")
        self.privacySecuritySettingsPage.check_SettingTab_Highlited("Legacy")

        self.privacySecuritySettingsPage.select_TwofactorToggle()
        flag = self.privacySecuritySettingsPage.validate_TwoFactorEnable_Modals()
        assert flag

        self.privacySecuritySettingsPage.select_TwofactorToggle()
        flag = self.privacySecuritySettingsPage.validate_TwoFactorDisable_Modals()
        assert flag

