import time
from pathlib import Path

from pytest_testrail.plugin import pytestrail
import allure
from Configuration.config import config
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser
from src.PageObjects.Reports.EditReports.EditReportsMainView.EditReportPage import EditReportPage
from src.PageObjects.Reports.EditReports.EditReportsMainView.EditTimeClockReportPage import EditTimeClockReportPage
from src.PageObjects.Reports.RunReports.RunReportsMainView.AccountReportPage import AccountReportPage
from src.PageObjects.Reports.RunReports.RunReportsMainView.ReportPage import ReportPage


class Test_Report(BaseTest):
    @pytestrail.case('C32601', 'C32602', 'C32603')
    def test_ReportPage(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Reports()
        self.reportPage = ReportPage(self.driver)
        page_found = self.reportPage.getPageTitle("Report")
        assert page_found
        print("User has been navigated to Reports screen")
        self.reportPage.click_newUI_Reports()
        time.sleep(2)
        tab_found = self.reportPage.validate_tab_EditReports()
        assert tab_found
        self.reportPage.click_EditReportsTab()
        self.editReportPage = EditReportPage(self.driver)
        time.sleep(10)
        assert self.editReportPage.validate_EditReportPage()
        self.editReportPage.click_EditReports_tabs("Advanced Time Clock")
        self.editTimeClockReportPage = EditTimeClockReportPage(self.driver)
        time.sleep(2)
        self.editTimeClockReportPage.select_Export_option("PDF")
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\Download\\editReports.pdf"
        time.sleep(5)
        assert self.editTimeClockReportPage.deleteFile(file_path)
        self.editTimeClockReportPage.select_Export_option("Excel")
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\Download\\editReports.xlsx"
        time.sleep(5)
        assert self.editTimeClockReportPage.deleteFile(file_path)
        self.editTimeClockReportPage.click_AddNew()
        time.sleep(1)
        self.editTimeClockReportPage.add_Employee_in_kendo("parent")
        self.editTimeClockReportPage.T("Ashish")
        self.editTimeClockReportPage.delete_Record()