import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest
from pathlib import Path



class Test_Company(BaseTest):
    @pytestrail.case('C34861', 'C34863', 'C34864', 'C34888')
    def test_addEmployee(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        file_path = str(Path.home())+"\PycharmProjects\/allGeo_webApp\src\Resources\employeeData.csv"
        self.employeesPage.add_multiple_employees(file_path)
        time.sleep(2)
        self.employeesPage.searchEmployeeByName("TestUser")
        self.employeesPage.select_record_byindex(1)
        assert self.employeesPage.check_BulkDeleteButton_disabled()
        self.employeesPage.select_record_byindex(2)
        assert self.employeesPage.check_BulkDeleteButton_enabled()
        self.employeesPage.click_BulkDelete()
        self.employeesPage.confirm_Delete()
        time.sleep(2)
