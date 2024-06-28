import time
from pathlib import Path

from pytest_testrail.plugin import pytestrail
import allure
from Configuration.config import config
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.BaseFile.BaseTest import BaseTest
from conftest import setup_driver, getEnvironment, getBrowser
from src.PageObjects.Reports.EditReports.EditReportsMainView.EditReportPage import EditReportPage
from src.PageObjects.Reports.EditReports.EditReportsMainView.EditTimeClockReportPage import EditTimeClockReportPage
from src.PageObjects.Reports.EditReports.EditReportsUI.EditMilesReport.EditMilesReportPage import EditMilesReportPage
from src.PageObjects.Reports.RunReports.RunReportsMainView.AccountReportPage import AccountReportPage
from src.PageObjects.Reports.RunReports.RunReportsMainView.ReportPage import ReportPage


class Test_Report(BaseTest):
    @pytestrail.case('C32652', 'C32664', 'C32668', 'C32669', 'C32671', 'C32679')
    def test_ReportPage(self):
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
        self.employeesPage.click_Addnew()
        time.sleep(2)
        empName = self.employeesPage.generate_random_string(7)
        empPhone = self.employeesPage.generate_random_phone_number()
        self.employeesPage.populate_addEmployeeForm(empName, empPhone)
        self.employeesPage.accept_termCheckbox()
        self.employeesPage.click_Add()
        assert self.employeesPage.validate_SuccessUpdateMessage("Successfully")

        self.leftNavigationPanelPage.click_Reports()
        self.reportPage = ReportPage(self.driver)
        page_found = self.reportPage.getPageTitle("Report")
        assert page_found
        print("User has been navigated to Reports screen")
        self.reportPage.click_newUI_Reports()
        time.sleep(5)
        tab_found = self.reportPage.validate_tab_EditReports()
        assert tab_found
        self.reportPage.click_EditReportsTab()
        self.editReportPage = EditReportPage(self.driver)
        assert self.editReportPage.validate_EditReportPage()
        self.editReportPage.click_EditReports_tabs("Miles")
        self.editMilesReportPage = EditMilesReportPage(self.driver)
        time.sleep(5)
        self.editMilesReportPage.select_Export_option("PDF")
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\Download\\editReports.pdf"
        time.sleep(10)
        assert self.editMilesReportPage.deleteFile(file_path)
        self.editMilesReportPage.searchEmployeeByName(empName)
        time.sleep(5)
        self.editMilesReportPage.remove_distance()
        self.editMilesReportPage.add_Distance_in_kendo("5")
        self.editMilesReportPage.add_Notes_in_kendo("Test")
        time.sleep(2)
        self.editMilesReportPage.click_SaveChanges()
        self.editMilesReportPage.confirm_SaveChangesAlert()
        self.editMilesReportPage.enter_ManagerNoteOnPopup("Manager Note2")
        self.editMilesReportPage.click_SaveOnPopup()
        time.sleep(5)
        self.editMilesReportPage.remove_Notes()
        actual = self.editMilesReportPage.get_alertMessage()
        expected = "This is a mandatory field. It cannot be left empty.\nClose"
        assert actual == expected
        self.editMilesReportPage.closeAlertMessage()
        time.sleep(2)
        #self.editMilesReportPage.click_SaveChanges()
        #self.editMilesReportPage.click_YesOnPopup()
        time.sleep(5)
        self.editTimeClockReportPage.select_Export_option("Excel")
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\Download\\editReports.xlsx"
        time.sleep(5)
        assert self.editTimeClockReportPage.deleteFile(file_path)

