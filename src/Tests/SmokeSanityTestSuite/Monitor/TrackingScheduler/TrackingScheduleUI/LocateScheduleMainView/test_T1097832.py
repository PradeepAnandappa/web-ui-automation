import time

from pytest_testrail.plugin import pytestrail
import allure
from Configuration.config import config
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.AddEditTrackingSchedulePage import \
    AddEditTrackingSchedulePage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.TrackingSchedulerPage import TrackingSchedulerPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser
from src.PageObjects.Reports.RunReports.RunReportsMainView.ReportPage import ReportPage


class Test_LocateSchedule(BaseTest):
    @pytestrail.case('C33091')
    def test_LocateScheduleView(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.click_TrackingSchedularTab()
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        self.trackingSchedulerPage.select_Status("Inactive")
        time.sleep(5)
        flag = self.trackingSchedulerPage.validateScheduleStatus("Inactive")
        assert flag






