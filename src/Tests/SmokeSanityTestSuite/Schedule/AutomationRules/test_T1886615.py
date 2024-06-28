import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
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
    @pytestrail.case('C40043', 'C40044', 'C40045', 'C40042', 'C40046', 'C40047', 'C40111', 'C40112')
    def test_automationRule(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        time.sleep(5)
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
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
        self.editAutomationRulePage.click_cancel()
        self.automationRulePage.click_View_for_RuleName(ruleId)
        self.viewAutomationRulePage = ViewAutomationRulePage(self.driver)
        self.viewAutomationRulePage.editRule()
        assert self.editAutomationRulePage.validateHeaderTitle()
        self.editAutomationRulePage.click_cancel()
        time.sleep(2)
        self.automationRulePage.deleteRuleById(ruleId)
        self.automationRulePage.confirm_DeleteAction()
        time.sleep(2)

