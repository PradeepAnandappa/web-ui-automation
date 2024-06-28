import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Company(BaseTest):
    @pytestrail.case('C34773', 'C34774')
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
        assert self.employeesPage.check_AddButton_disabled()
        self.employeesPage.accept_termCheckbox()
        assert self.employeesPage.check_AddButton_enabled()
