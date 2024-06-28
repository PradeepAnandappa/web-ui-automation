import random
import string
import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EditEmployeesPage import EditEmployeesPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.ViewEmployeesPage import ViewEmployeesPage
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Company.JobSites.JobSitesUI.AddJobSite.JobSitesPage import JobSitesPage
from src.PageObjects.Company.Managers.ManagerUI.AddManager.ManagersPage import ManagersPage
from src.PageObjects.Company.Managers.ManagerUI.EditManagerGroupAuthorization.EditManagersPage import EditManagersPage
from src.PageObjects.Company.Tasks.TasksUI.AddTask.TasksPage import TasksPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage

from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.AddEditTrackingSchedulePage import \
    AddEditTrackingSchedulePage
from src.PageObjects.Monitor.TrackingScheduler.TrackingScheduleUI.LocateScheduleMainView.TrackingSchedulerPage import \
    TrackingSchedulerPage


class Test_Company(BaseTest):
    @pytestrail.case('C32999', 'C33000')
    def test_ViewSchedule(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.monitorPage.click_TrackingSchedularTab()
        self.trackingSchedulerPage = TrackingSchedulerPage(self.driver)
        page_URL = self.trackingSchedulerPage.getPageURL()
        Expected_URL = config.baseURL + "/monitor/locate-schedule"
        assert Expected_URL == page_URL
        self.trackingSchedulerPage.click_AddNew()
        self.addEditTrackingSchedulePage = AddEditTrackingSchedulePage(self.driver)
        flag = self.addEditTrackingSchedulePage.validate_AddNewTrackingScheduleModal()
        assert flag
        scheduleName = ''.join(random.choices(string.ascii_letters, k=7))
        self.addEditTrackingSchedulePage.addTrackingSchedule(scheduleName)
        time.sleep(2)
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(5)
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Managers")
        self.managersPage = ManagersPage(self.driver)
        self.managersPage.click_edit_for_ManagerID("m101")
        self.editManagersPage = EditManagersPage(self.driver)
        self.editManagersPage.validateHeaderTitle()
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
        assert self.trackingSchedulerPage.check_ActionLink_enabled("view", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("delete", scheduleName)
        self.trackingSchedulerPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage.click_company_icon("Managers")
        self.managersPage.click_edit_for_ManagerID("m101")
        assert self.editManagersPage.validateHeaderTitle()
        time.sleep(2)
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
        self.trackingSchedulerPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage.click_company_icon("Managers")
        self.managersPage.click_edit_for_ManagerID("m101")
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
        assert self.trackingSchedulerPage.check_ActionLink_disabled("edit", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_disabled("delete", scheduleName)
        assert self.trackingSchedulerPage.check_ActionLink_enabled("view", scheduleName)
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


