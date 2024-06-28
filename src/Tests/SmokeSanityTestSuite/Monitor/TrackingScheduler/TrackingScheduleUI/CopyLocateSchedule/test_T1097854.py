import random
import string
import time

from pytest_testrail.plugin import pytestrail
import allure
from Configuration.config import config
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.PageObjects.Company.Managers.ManagerUI.AddManager.ManagersPage import ManagersPage
from src.PageObjects.Company.Managers.ManagerUI.EditManagerGroupAuthorization.EditManagersPage import EditManagersPage
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


class Test_LocateScheduleCopy(BaseTest):
    @pytestrail.case('C33234', 'C33235', 'C33236', 'C33237')
    def test_LocateScheduleCopy(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
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
        time.sleep(2)

        self.leftNavigationPanelPage.click_Monitor()
        time.sleep(4)
        self.monitorPage.click_TrackingSchedularTab()
        time.sleep(2)
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        self.trackingSchedulerPage.click_AddNew()
        self.addEditTrackingSchedulePage = AddEditTrackingSchedulePage(self.driver)
        scheduleName = self.addEditTrackingSchedulePage.generate_random_string(5) + "101"
        self.addEditTrackingSchedulePage.enter_ScheduleName(scheduleName)
        self.addEditTrackingSchedulePage.select_Employee()
        time.sleep(1)
        self.addEditTrackingSchedulePage.select_Group(empName)
        time.sleep(1)
        self.addEditTrackingSchedulePage.click_Done()
        time.sleep(2)
        self.trackingSchedulerPage.logout_user()
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.click_TrackingSchedularTab()
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        assert self.trackingSchedulerPage.check_ActionLink_disabled("edit", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_enabled("view", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("delete", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("copy", scheduleName)
        self.trackingSchedulerPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage.click_company_icon("Managers")
        self.managersPage = ManagersPage(self.driver)
        time.sleep(2)
        self.managersPage.click_edit_for_ManagerID("m101")
        self.editManagersPage = EditManagersPage(self.driver)
        assert self.editManagersPage.validateHeaderTitle()
        time.sleep(2)
        self.editManagersPage.set_ACL_for("Schedule", "Edit")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.click_TrackingSchedularTab()
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        assert self.trackingSchedulerPage.check_ActionLink_enabled("edit", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("delete", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_enabled("view", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("copy", scheduleName)
        self.trackingSchedulerPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage.click_company_icon("Managers")
        time.sleep(2)
        self.managersPage.click_edit_for_ManagerID("m101")
        time.sleep(2)
        assert self.editManagersPage.validateHeaderTitle()
        self.editManagersPage.set_ACL_for("Schedule", "Add")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.click_TrackingSchedularTab()
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        assert self.trackingSchedulerPage.check_ActionLink_enabled("edit", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_enabled("delete", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_enabled("view", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_enabled("copy", scheduleName)
        self.trackingSchedulerPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage.click_company_icon("Managers")
        time.sleep(2)
        self.managersPage.click_edit_for_ManagerID("m101")
        time.sleep(2)
        assert self.editManagersPage.validateHeaderTitle()
        self.editManagersPage.set_ACL_for("Schedule", "Add")
        self.editManagersPage.set_ACL_for("Schedule", "Edit")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.click_TrackingSchedularTab()
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        assert self.trackingSchedulerPage.check_ActionLink_disabled("edit", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("delete", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_enabled("view", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("copy", scheduleName)
        self.trackingSchedulerPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.monitorPage.click_TrackingSchedularTab()
        page_URL = self.monitorPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        self.trackingSchedulerPage.delete_schedule(scheduleName)
        self.trackingSchedulerPage.confirm_DeleteAction()
