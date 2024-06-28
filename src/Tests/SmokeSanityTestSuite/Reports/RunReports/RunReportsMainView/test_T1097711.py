import time

from pytest_testrail.plugin import pytestrail
import allure
from Configuration.config import config
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser
from src.PageObjects.Reports.RunReports.RunReportsMainView.AccountReportPage import AccountReportPage
from src.PageObjects.Reports.RunReports.RunReportsMainView.DebugReportPage import DebugReportPage
from src.PageObjects.Reports.RunReports.RunReportsMainView.ReportPage import ReportPage


class Test_Report(BaseTest):
    @pytestrail.case('C32838')
    def test_ReportPage(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        time.sleep(2)
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Reports()
        self.reportPage = ReportPage(self.driver)
        page_found = self.reportPage.getPageTitle("Report")
        assert page_found
        print("User has been navigated to Reports screen")
        self.reportPage.click_newUI_Reports()
        time.sleep(2)
        tab_found = self.reportPage.validate_Report_type_tabs("Time")
        assert tab_found
        self.reportPage.click_report_type_tab("Time")
        actual = self.reportPage.getPageURL()
        expected = config.baseURL + "/ngui/reports"
        assert actual == expected
        assert "All" == self.reportPage.validate_Default_Group_Selection()
        self.reportPage.select_StartDate("2023/09/01 12:00:00 AM")
        self.reportPage.select_EndDate("2023/10/18 11:59:00 PM")

