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
    @pytestrail.case('C25640', 'C25611', 'C25641', 'C25642', 'C25643', 'C25644', 'C25645', 'C25646', 'C25647')
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
        EmpCode ="Test101"
        time.sleep(1)
        self.editEmployeesPage.setCompanyCode(EmpCode)
        time.sleep(2)
        self.editEmployeesPage.click_Save()
        self.employeesPage.click_edit_for_employee(empPhone)
        self.editEmployeesPage.click_on_Tab("Payroll")
        assert EmpCode == self.editEmployeesPage.getCompanyCode()



