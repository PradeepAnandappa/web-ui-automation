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
    @pytestrail.case('C34854', 'C34855')
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
        self.employeesPage.click_MutipleTab()
        time.sleep(2)
        self.employeesPage.click_DownloadEmployeeData()
        time.sleep(2)
        file_path = str(Path.home()) + "\\PycharmProjects\\allGeo_webApp\\src\\Resources\\Download\\employee-sample.csv"
        color = self.employeesPage.getColorOfAddButton()
        print("Before selecting file, color of add button: ", color)
        assert "rgba(235, 235, 235, 1)" == color
        self.employeesPage.uploadCSVFile(file_path)
        time.sleep(2)
        color = self.employeesPage.getColorOfAddButton()
        print("After selection of file, color of add button: ", color)
        assert "rgba(37, 163, 214, 1)" == color
        time.sleep(5)
        assert self.employeesPage.deleteFile(file_path)
