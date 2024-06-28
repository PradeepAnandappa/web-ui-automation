import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
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
    @pytestrail.case('C32957')
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
        self.employeesPage.click_company_icon("Group")
        self.groupsPage = GroupsPage(self.driver)
        time.sleep(5)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        self.groupsPage.click_AddNew()
        self.addEditGroupPage = AddEditGroupPage(self.driver)
        assert self.addEditGroupPage.validate_Add_Group_Modal()
        groupId = self.addEditGroupPage.generate_random_string(5)+"02"
        groupName = self.addEditGroupPage.generate_random_string(5)
        self.addEditGroupPage.add_group(groupId, groupName)
        assert self.addEditGroupPage.validate_SuccessUpdateMessage("successfully")
        self.leftNavigationPanelPage.click_Monitor()
        self.monitorPage.click_TrackingSchedularTab()
        time.sleep(2)
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        self.trackingSchedulerPage.click_AddNew()
        self.addEditTrackingSchedulePage = AddEditTrackingSchedulePage(self.driver)
        scheduleName = self.addEditTrackingSchedulePage.generate_random_string(5)+"101"
        self.addEditTrackingSchedulePage.enter_ScheduleName(scheduleName)

        self.addEditTrackingSchedulePage.select_Group(groupName)
        time.sleep(2)
        self.addEditTrackingSchedulePage.set_TrackFrequency("20")
        time.sleep(1)
        actual = self.addEditTrackingSchedulePage.get_TrackFrequency()
        assert actual == "20"
        self.addEditTrackingSchedulePage.click_Done()
        self.trackingSchedulerPage.validate_SuccessUpdateMessage("successfully")


