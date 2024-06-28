import random
import string
import time

from pytest_testrail.plugin import pytestrail
import allure
from Configuration.config import config
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.CopyLocateSchedule.CopyTrackingSchedulePage import \
    CopyTrackingSchedulePage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.AddEditTrackingSchedulePage import \
    AddEditTrackingSchedulePage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.TrackingSchedulerPage import TrackingSchedulerPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.ViewLocateSchedule.ViewLocateSchedulePage import \
    ViewLocateSchedulePage
from src.PageObjects.Reports.RunReports.RunReportsMainView.ReportPage import ReportPage


class Test_LocateSchedule(BaseTest):
    @pytestrail.case('C33267', 'C33268')
    def test_LocateScheduleView(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.click_TrackingSchedularTab()
        time.sleep(2)
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        self.trackingSchedulerPage.click_AddNew()
        self.addEditTrackingSchedulePage = AddEditTrackingSchedulePage(self.driver)
        scheduleName = self.addEditTrackingSchedulePage.generate_random_string(5) + "101"
        self.addEditTrackingSchedulePage.addTrackingSchedule(scheduleName)
        time.sleep(60)
        self.trackingSchedulerPage.copy_schedule(scheduleName)
        self.copyTrackingSchedulePage = CopyTrackingSchedulePage(self.driver)
        assert self.copyTrackingSchedulePage.validateHeaderTitle()
        CopyScheduleName = self.copyTrackingSchedulePage.generate_random_string(5) + "101copy"
        self.copyTrackingSchedulePage.addTrackingSchedule(CopyScheduleName)
        self.copyTrackingSchedulePage.close_popup()
        time.sleep(2)
        self.trackingSchedulerPage.click_view_icon_for_schedule(CopyScheduleName)
        self.viewLocateSchedulePage = ViewLocateSchedulePage(self.driver)
        time.sleep(2)
        self.viewLocateSchedulePage.deleteSchedule()
        self.viewLocateSchedulePage.confirm_delete()
