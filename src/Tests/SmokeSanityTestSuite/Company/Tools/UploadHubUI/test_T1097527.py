import time
from pathlib import Path

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.JobSites.JobSitesUI.AddJobSite.JobSitesPage import JobSitesPage
from src.PageObjects.Company.Tasks.TasksUI.AddTask.TasksPage import TasksPage
from src.PageObjects.Company.Tools.UploadHubUI.UploadHubPage import UploadHubPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_JobSites(BaseTest):
    @pytestrail.case('C30416')
    def test_addJobSite(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(2)
        self.employeesPage.click_company_icon("Tools")
        self.uploadHubPage = UploadHubPage(self.driver)
        time.sleep(5)
        assert self.uploadHubPage.validate_PageHeader()
        self.uploadHubPage.select_CategoryofFileUpload("Task")
        time.sleep(2)
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\task_details_with_duplicateRecord.csv"
        self.uploadHubPage.uploadCSVFile(file_path)
        time.sleep(2)
        self.uploadHubPage.click_Upload()
        assert self.uploadHubPage.validate_ErrorMessage("1 entries were uploaded Error:1 entries were not uploaded")
        self.uploadHubPage.click_Cancel()
        time.sleep(1)
        self.uploadHubPage.click_company_icon("Task")
        self.tasksPage = TasksPage(self.driver)
        self.tasksPage.deleteTaskByName("name1")
        time.sleep(2)
        self.tasksPage.confirm_DeleteAction()
        time.sleep(2)





