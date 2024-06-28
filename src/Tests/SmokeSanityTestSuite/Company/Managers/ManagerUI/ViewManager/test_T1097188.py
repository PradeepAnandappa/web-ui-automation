import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.JobSites.JobSitesUI.AddJobSite.JobSitesPage import JobSitesPage
from src.PageObjects.Company.Managers.ManagerUI.AddManager.ManagersPage import ManagersPage
from src.PageObjects.Company.Managers.ManagerUI.ViewManager.ViewManagerPage import ViewManagerPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Managers(BaseTest):
    @pytestrail.case('C26722', 'C26720', 'C26718', 'C26716')
    def test_manager(self):
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
        self.employeesPage.click_company_icon("Managers")
        self.managersPage = ManagersPage(self.driver)
        time.sleep(5)
        page_found = self.managersPage.getPageTitle("Managers")
        assert page_found
        self.managersPage.addManager("TM102", "tm102@yomail.com", "1234567823")
        time.sleep(2)
        assert self.managersPage.validate_SuccessUpdateMessage("manager has been added successfully")
        time.sleep(2)
        self.managersPage.click_view_for_ManagerID("TM102")
        self.viewManagerPage = ViewManagerPage(self.driver)
        time.sleep(2)
        assert self.viewManagerPage.validateHeaderTitle()
        self.viewManagerPage.click_Back()
        self.managersPage.click_view_for_ManagerID("TM102")
        self.viewManagerPage.deleteManager()


