import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.JobSites.JobSitesUI.AddJobSite.JobSitesPage import JobSitesPage
from src.PageObjects.Company.JobSites.JobSitesUI.EditJobSite.EditJobSitePage import EditJobSitePage
from src.PageObjects.Company.JobSites.JobSitesUI.ViewJobSite.ViewJobSitePage import ViewJobSitePage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_JobSites(BaseTest):
    @pytestrail.case('C25997')
    def test_editJobSites(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
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
        siteName = self.employeesPage.generate_random_string(5)
        self.jobSitesPage.addJobSite(siteName, "Noida 201301")
        time.sleep(3)
        assert self.jobSitesPage.validate_SuccessUpdateMessage("added successfully")
        time.sleep(2)
        self.jobSitesPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login("test-web-automation-child", "m101", "1234")
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Dashboard")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        self.employeesPage.click_company_icon("Jobsite")
        self.jobSitesPage = JobSitesPage(self.driver)
        time.sleep(5)
        page_found = self.jobSitesPage.getPageTitle("Jobsite")
        assert page_found
        assert self.jobSitesPage.validate_EditLink_disabled(siteName)
        self.jobSitesPage.click_View_for_JobSiteName(siteName)
        self.viewJobSitePage = ViewJobSitePage(self.driver)
        assert self.viewJobSitePage.validate_EditLink_disabled()
        self.viewJobSitePage.click_Back()
        time.sleep(2)
        self.jobSitesPage.logout_user()
        time.sleep(2)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.monitorPage.switch_to_ChildAccount()
        time.sleep(2)
        self.leftNavigationPanelPage.click_Company()
        time.sleep(5)
        page_found = self.employeesPage.validate_page_title()
        assert page_found
        self.employeesPage.click_company_icon("Jobsite")
        self.jobSitesPage = JobSitesPage(self.driver)
        time.sleep(2)
        page_found = self.jobSitesPage.getPageTitle("Jobsite")
        assert page_found
        self.jobSitesPage.deleteJobSiteByName(siteName)
        self.jobSitesPage.confirm_DeleteAction()
        time.sleep(2)



