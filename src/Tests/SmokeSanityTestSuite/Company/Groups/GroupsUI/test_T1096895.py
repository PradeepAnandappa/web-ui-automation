import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EditEmployeesPage import EditEmployeesPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.ViewEmployeesPage import ViewEmployeesPage
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Company.Managers.ManagerUI.AddManager.ManagersPage import ManagersPage
from src.PageObjects.Company.Managers.ManagerUI.EditManagerGroupAuthorization.EditManagersPage import EditManagersPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Company(BaseTest):
    @pytestrail.case('C24921', 'C24922')
    def test_addEmployee(self):
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
        time.sleep(5)
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Group")
        self.groupsPage = GroupsPage(self.driver)
        time.sleep(5)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        self.groupsPage.click_AddNew()
        self.addEditGroupPage = AddEditGroupPage(self.driver)
        assert self.addEditGroupPage.validate_Add_Group_Modal()
        groupName = self.employeesPage.generate_random_string(5)
        groupId = self.employeesPage.generate_random_string(5)
        self.addEditGroupPage.add_group(groupId, groupName)
        assert self.addEditGroupPage.validate_SuccessUpdateMessage("successfully")
        time.sleep(2)
        self.employeesPage.click_company_icon("Managers")
        self.managersPage = ManagersPage(self.driver)
        self.managersPage.click_edit_for_ManagerID("m101")
        self.editManagersPage = EditManagersPage(self.driver)
        self.editManagersPage.validateHeaderTitle()
        time.sleep(2)
        self.editManagersPage.set_ACL_for("Group Administration", "Edit")
        #self.editManagersPage.set_ACL_for("Group Administration", "Add")
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
        self.employeesPage.click_company_icon("Group")
        time.sleep(5)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        assert self.groupsPage.check_ActionLink_enabled("view", groupId)
        assert self.groupsPage.check_ActionLink_enabled("edit", groupId)
        assert self.groupsPage.check_ActionLink_disabled("delete", groupId)

        self.groupsPage.logout_user()
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
        self.editManagersPage.set_ACL_for("Group Administration", "Add")
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
        self.employeesPage.click_company_icon("Group")
        time.sleep(5)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        assert self.groupsPage.check_ActionLink_enabled("view", groupId)
        assert self.groupsPage.check_ActionLink_enabled("edit", groupId)
        assert self.groupsPage.check_ActionLink_enabled("delete", groupId)
        self.groupsPage.logout_user()
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
        self.editManagersPage.set_ACL_for("Group Administration", "Add")
        self.editManagersPage.set_ACL_for("Group Administration", "Edit")
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
        self.employeesPage.click_company_icon("Group")
        time.sleep(5)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        assert self.groupsPage.check_ActionLink_enabled("view", groupId)
        assert self.groupsPage.check_ActionLink_disabled("edit", groupId)
        assert self.groupsPage.check_ActionLink_disabled("delete", groupId)
        self.groupsPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        time.sleep(2)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        time.sleep(2)
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Group")
        time.sleep(2)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        self.groupsPage.deleteGroupById(groupId)


