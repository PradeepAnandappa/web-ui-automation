import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.JobSites.JobSitesUI.AddJobSite.JobSitesPage import JobSitesPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest
from pathlib import Path



class Test_Company(BaseTest):
    @pytestrail.case('C26268')
    def test_addEmployee(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(2)
        self.employeesPage.click_company_icon("Jobsite")
        self.jobSitesPage = JobSitesPage(self.driver)
        time.sleep(5)
        page_found = self.jobSitesPage.getPageTitle("Jobsite")
        assert page_found
        file_path = str(Path.home())+"\PycharmProjects\/allGeo_webApp\src\Resources\jobsitesData.csv"

        self.jobSitesPage.add_multiple_jobsites(file_path)
        time.sleep(2)
        self.jobSitesPage.deleteJobSiteByName("TestSite")
        self.jobSitesPage.confirm_DeleteAction()
        self.jobSitesPage.deleteJobSiteByName("TestSite2")
        self.jobSitesPage.confirm_DeleteAction()
