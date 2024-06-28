import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.JobSites.JobSitesUI.AddJobSite.JobSitesPage import JobSitesPage
from src.PageObjects.Company.JobSites.JobSitesUI.EditJobSite.EditJobSitePage import EditJobSitePage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Jobsites(BaseTest):
    @pytestrail.case('C26258')
    def test_jobsites(self):
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
        self.employeesPage.click_company_icon("Jobsite")
        self.jobSitesPage = JobSitesPage(self.driver)
        time.sleep(5)
        page_found = self.jobSitesPage.getPageTitle("Jobsite")
        assert page_found
        siteName = self.jobSitesPage.generate_random_string(5)
        self.jobSitesPage.addJobSite(siteName, "Noida 201301")
        self.jobSitesPage.click_edit_for_JobSiteName(siteName)
        self.editJobSitePage = EditJobSitePage(self.driver)
        self.editJobSitePage.set_Status()
        self.editJobSitePage.click_Save()
        self.jobSitesPage.select_Status("Inactive")
        time.sleep(2)
        self.jobSitesPage.deleteJobSiteByName(siteName)
        self.jobSitesPage.confirm_DeleteAction()
        time.sleep(2)