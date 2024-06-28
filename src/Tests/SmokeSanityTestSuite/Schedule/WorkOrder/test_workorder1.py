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
from src.PageObjects.Schedule.WorkOrder.AddWorkOrder.AddWorkOrderPage import AddWorkOrderPage
from src.PageObjects.Schedule.WorkOrder.WorkOrderPage import WorkOrderPage


class Test_WorkOrder(BaseTest):
    @pytestrail.case('C39994')
    def test_workOrder(self):
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

        #self.employeesPage.click_Addnew()
        #time.sleep(2)
        #empName = self.employeesPage.generate_random_string(7)
        #empPhone = self.employeesPage.generate_random_phone_number()
        #self.employeesPage.populate_addEmployeeForm(empName, empPhone)
        #self.employeesPage.accept_termCheckbox()
        #self.employeesPage.click_Add()
        #assert self.employeesPage.validate_SuccessUpdateMessage("Successfully")

        time.sleep(2)
        self.leftNavigationPanelPage.click_Schedule()
        self.workOrderPage = WorkOrderPage(self.driver)
        time.sleep(5)
        page_found = self.workOrderPage.validate_PageHeader()
        assert page_found
        self.workOrderPage.click_LeftPanelOption("Work Order")
        time.sleep(2)

        self.workOrderPage.click_plusIcon()
        time.sleep(2)
        self.addWorkOrderPage = AddWorkOrderPage(self.driver)
        title = self.addWorkOrderPage.get_page_title()
        assert title == 'Upload Work Order(s)'
        self.addWorkOrderPage.enterFieldvalue("Work Order Id", "testWO11march")
        time.sleep(2)
        self.addWorkOrderPage.enterFieldvalue("Employee Name", "QUozLVB")
        time.sleep(2)
        self.addWorkOrderPage.enterFieldvalue("Start Time", "5:58 PM")
        time.sleep(2)
        self.addWorkOrderPage.enterFieldvalue("Stop Time", "9:58 PM")
        time.sleep(10)
        self.addWorkOrderPage.click_Save()
        time.sleep(2)



