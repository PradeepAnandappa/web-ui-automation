import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EditEmployeesPage import EditEmployeesPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Company(BaseTest):
    @pytestrail.case('C25654', 'C25655', 'C25657', 'C25658', 'C25659', 'C25660', 'C25661', 'C25663', 'C25667')
    def test_addEmployee(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        self.employeesPage.click_Addnew()
        time.sleep(2)
        empName = self.employeesPage.generate_random_string(7)
        empPhone = self.employeesPage.generate_random_phone_number()
        self.employeesPage.populate_addEmployeeForm(empName, empPhone)
        self.employeesPage.accept_termCheckbox()
        self.employeesPage.click_Add()
        assert self.employeesPage.validate_SuccessUpdateMessage("Successfully")
        time.sleep(2)
        self.employeesPage.click_edit_for_employee(empPhone)
        self.editEmployeesPage = EditEmployeesPage(self.driver)
        assert self.editEmployeesPage.validateHeaderTitle()
        self.editEmployeesPage.click_on_Tab("Payroll")
        time.sleep(1)
        self.editEmployeesPage.set_PayRollHours("Daily")
        time.sleep(2)
        self.editEmployeesPage.setRegularEarningCode("TestCode")
        self.editEmployeesPage.click_Save()
        time.sleep(2)
        self.employeesPage.click_edit_for_employee(empPhone)
        self.editEmployeesPage.setRegularEarningCode("TestCode2")
        self.editEmployeesPage.click_Save()



