import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Managers.ManagerUI.AddManager.ManagersPage import ManagersPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Company(BaseTest):
    @pytestrail.case('C26709', 'C26710')
    def test_deleteManager(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        self.employeesPage.click_company_icon("Managers")
        self.managersPage = ManagersPage(self.driver)
        time.sleep(5)
        page_found = self.managersPage.getPageTitle("Managers")
        assert page_found
        self.managersPage.addManager("TM101", "tm101@yomail.com", "1234567823")
        time.sleep(2)
        assert self.managersPage.validate_SuccessUpdateMessage("manager has been added successfully")
        time.sleep(2)
        self.managersPage.deleteManagerById("TM101")
        time.sleep(2)
        assert self.managersPage.validate_SuccessUpdateMessage("deleted Successfully")
