import time

import arrow
from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Company.Settings.GeneralSettings.GeneralSettingsUI.SettingsPage import SettingsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.AddEditTrackingSchedulePage import \
    AddEditTrackingSchedulePage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.TrackingSchedulerPage import \
    TrackingSchedulerPage
from conftest import setup_driver, getEnvironment, getBrowser
from src.PageObjects.Reports.RunReports.RunReportsMainView.ReportPage import ReportPage

class Test_Groups(BaseTest):
    @pytestrail.case('C32955')
    def test_GroupsUI(self):
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
        date_format = self.settingsPage.get_selected_Date_format()
        date_format = date_format.upper()
        print("Date format: "+date_format)
        time.sleep(2)
        self.leftNavigationPanelPage.click_Monitor()
        self.monitorPage.click_TrackingSchedularTab()
        time.sleep(2)
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        self.trackingSchedulerPage.click_AddNew()
        self.addEditTrackingSchedulePage = AddEditTrackingSchedulePage(self.driver)
        trackDefaultFrequency = self.addEditTrackingSchedulePage.get_TrackFrequency()
        print(trackDefaultFrequency)
        assert trackDefaultFrequency == "15"



