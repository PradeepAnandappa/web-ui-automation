import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.BasePage.UnAuthorizePage import UnAuthorizePage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EditEmployeesPage import EditEmployeesPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.ViewEmployeesPage import ViewEmployeesPage
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Company.JobSites.JobSitesUI.AddJobSite.JobSitesPage import JobSitesPage
from src.PageObjects.Company.Managers.ManagerUI.AddManager.ManagersPage import ManagersPage
from src.PageObjects.Company.Managers.ManagerUI.EditManagerGroupAuthorization.EditManagersPage import EditManagersPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest
from src.PageObjects.Schedule.AutomationRules.AutomationRulePage import AutomationRulePage
from src.PageObjects.Schedule.WorkOrder.WorkOrderPage import WorkOrderPage


class Test_Schedule(BaseTest):
    @pytestrail.case('C38779')
    def test_ACLPermission(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(2)
        self.employeesPage.click_company_icon("Managers")
        self.managersPage = ManagersPage(self.driver)
        self.managersPage.click_edit_for_ManagerID("m101")
        self.editManagersPage = EditManagersPage(self.driver)
        assert self.editManagersPage.validateHeaderTitle()
        time.sleep(2)
        self.editManagersPage.set_ACL_for("Group Administration", "Add")
        time.sleep(1)
        self.editManagersPage.set_ACL_for("Group Administration", "View")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(2)
        flag = self.employeesPage.isAvailable_leftPanelOption("Group")
        assert flag == bool(False)
        self.employeesPage.logout_user()
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
        self.editManagersPage.set_ACL_for("Group Administration", "View")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        time.sleep(2)
        assert self.employeesPage.isAvailable_leftPanelOption("Group")


