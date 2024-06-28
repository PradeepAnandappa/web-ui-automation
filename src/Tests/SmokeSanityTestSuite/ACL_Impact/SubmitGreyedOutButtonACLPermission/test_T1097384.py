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
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Company(BaseTest):
    @pytestrail.case('C29678', 'C29679', 'C29680', 'C29686', 'C29687')
    def test_addEmployee(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        time.sleep(2)
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(5)
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Task")
        self.tasksPage = TasksPage(self.driver)
        time.sleep(5)
        page_found = self.tasksPage.get_page_title()
        assert page_found
        taskId = self.employeesPage.generate_random_string(5)+str(1)
        taskName = self.employeesPage.generate_random_string(7)
        self.tasksPage.addTask(taskId, taskName)
        time.sleep(2)
        assert self.tasksPage.validate_SuccessUpdateMessage("added successfully")
        time.sleep(2)
        self.employeesPage.click_company_icon("Managers")
        self.managersPage = ManagersPage(self.driver)
        self.managersPage.click_edit_for_ManagerID("m101")
        self.editManagersPage = EditManagersPage(self.driver)
        self.editManagersPage.validateHeaderTitle()
        time.sleep(2)
        self.editManagersPage.set_ACL_for("Task", "Edit")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Task")
        time.sleep(5)
        page_found = self.tasksPage.get_page_title()
        assert page_found
        assert self.tasksPage.check_ActionLink_enabled("edit", taskName)
        assert self.tasksPage.check_ActionLink_disabled("delete", taskName)
        assert self.tasksPage.check_ActionLink_enabled("view", taskName)
        self.tasksPage.logout_user()
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
        self.editManagersPage.set_ACL_for("Task", "Add")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Task")
        time.sleep(5)
        page_found = self.tasksPage.get_page_title()
        assert page_found
        assert self.tasksPage.check_ActionLink_enabled("edit", taskName)
        assert self.tasksPage.check_ActionLink_enabled("delete", taskName)
        assert self.tasksPage.check_ActionLink_enabled("view", taskName)
        self.tasksPage.logout_user()
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
        self.editManagersPage.set_ACL_for("Task", "Add")
        self.editManagersPage.set_ACL_for("Task", "Edit")
        self.editManagersPage.click_saveBtn()
        time.sleep(2)
        self.editManagersPage.click_Cancel()
        time.sleep(2)
        self.managersPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "Test@123")
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Task")
        time.sleep(5)
        page_found = self.tasksPage.get_page_title()
        assert page_found
        assert self.tasksPage.check_ActionLink_disabled("edit", taskName)
        assert self.tasksPage.check_ActionLink_disabled("delete", taskName)
        assert self.tasksPage.check_ActionLink_enabled("view", taskName)
        self.tasksPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        time.sleep(2)
        self.employeesPage.click_company_icon("Task")
        time.sleep(2)
        page_found = self.tasksPage.get_page_title()
        assert page_found
        self.tasksPage.deleteTaskByName(taskName)
        self.tasksPage.confirm_DeleteAction()


