import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest
from src.PageObjects.Schedule.AutomationRules.AutomationRulePage import AutomationRulePage
from src.PageObjects.Schedule.AutomationRules.EditAutomationRulePage import EditAutomationRulePage
from src.PageObjects.Schedule.AutomationRules.ViewAutomationRulePage import ViewAutomationRulePage
from src.PageObjects.Schedule.WorkOrder.WorkOrderPage import WorkOrderPage


class Test_AutomationRules(BaseTest):
    @pytestrail.case('C40067', 'C40069')
    def test_automationRule(self):
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
        self.employeesPage.click_company_icon("Group")
        self.groupsPage = GroupsPage(self.driver)
        time.sleep(5)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        self.groupsPage.click_AddNew()
        self.addEditGroupPage = AddEditGroupPage(self.driver)
        assert self.addEditGroupPage.validate_Add_Group_Modal()
        grpId = self.addEditGroupPage.generate_random_string(5)
        grpName = self.addEditGroupPage.generate_random_string(7)
        self.addEditGroupPage.add_group(grpId, grpName)
        assert self.addEditGroupPage.validate_SuccessUpdateMessage("successfully")
        time.sleep(2)
        self.leftNavigationPanelPage.click_Schedule()
        self.workOrderPage = WorkOrderPage(self.driver)
        time.sleep(5)
        page_found = self.workOrderPage.validate_PageHeader()
        assert page_found
        self.workOrderPage.click_LeftPanelOption("Automation Rules")
        self.automationRulePage = AutomationRulePage(self.driver)
        time.sleep(2)
        page_found = self.automationRulePage.validate_PageHeader()
        assert page_found
        self.automationRulePage.click_AddNew()
        time.sleep(2)
        self.automationRulePage.close_popup()
        ruleId = "Rule" + self.automationRulePage.generate_random_string(5)
        self.automationRulePage.addRule(ruleId)
        self.automationRulePage.click_edit_for_RuleName(ruleId)
        self.editAutomationRulePage = EditAutomationRulePage(self.driver)
        time.sleep(2)
        assert self.editAutomationRulePage.validateHeaderTitle()
        grpId = grpId.lower()
        self.editAutomationRulePage.select_Group(grpId)
        time.sleep(2)
        self.editAutomationRulePage.click_Save()
        time.sleep(2)
        self.automationRulePage.deleteRuleById(ruleId)
        self.automationRulePage.confirm_DeleteAction()
        time.sleep(2)

