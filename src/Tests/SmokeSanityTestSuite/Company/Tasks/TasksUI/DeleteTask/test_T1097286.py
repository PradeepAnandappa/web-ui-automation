import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Tasks.TasksUI.AddTask.TasksPage import TasksPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Tasks(BaseTest):
    @pytestrail.case('C27830')
    def test_deleteTask(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        self.employeesPage.click_company_icon("Task")
        self.tasksPage = TasksPage(self.driver)
        time.sleep(5)
        page_found = self.tasksPage.get_page_title()
        assert page_found
        assert self.tasksPage.check_BulkDeleteButton_disabled()
        self.tasksPage.select_record_byindex("1")
        self.tasksPage.select_record_byindex("2")
        assert self.tasksPage.check_BulkDeleteButton_enabled()
        self.tasksPage.bulk_delete()



