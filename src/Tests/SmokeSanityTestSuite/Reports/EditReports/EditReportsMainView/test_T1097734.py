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
from src.PageObjects.Reports.RunReports.RunReportsMainView.AccountReportPage import AccountReportPage
from src.PageObjects.Reports.RunReports.RunReportsMainView.ReportPage import ReportPage


class Test_Report(BaseTest):
    @pytestrail.case('C32910', 'C32912', 'C32913', 'C32915', 'C32916', 'C32919', 'C32921', 'C32922', 'C32925', 'C32926', 'C32927', 'C32928', 'C32930', 'C32931')
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
        assert self.editReportPage.validate_EditReports_tabs("Miles")
        assert self.editReportPage.validate_EditReports_tabs("Advanced Time Clock")
        assert self.editReportPage.validate_EditReports_tabs("Audit")

        self.editReportPage.select_Export_option("PDF")
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\Download\\editReports.pdf"
        time.sleep(5)
        assert self.editReportPage.deleteFile(file_path)

        self.editReportPage.select_Export_option("Excel")
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\Download\\editReports.xlsx"
        time.sleep(5)
        assert self.editReportPage.deleteFile(file_path)
        self.editReportPage.click_AddNew()
        time.sleep(1)
        self.editReportPage.add_Employee_in_kendo("Test QA")
        self.editReportPage.search_record("Test QA")
        self.editReportPage.delete_Record()
