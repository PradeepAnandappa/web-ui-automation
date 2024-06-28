import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Groups(BaseTest):
    @pytestrail.case('C24900')
    def test_GroupsUI(self):
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
        self.employeesPage.click_company_icon("Group")
        self.groupsPage = GroupsPage(self.driver)
        time.sleep(5)
        page_found = self.groupsPage.get_page_title()
        assert page_found
        self.groupsPage.click_AddNew()
        self.addEditGroupPage = AddEditGroupPage(self.driver)
        assert self.addEditGroupPage.validate_Add_Group_Modal()
        grp_id = self.addEditGroupPage.generate_random_string(5) + "101"
        grp_name = self.addEditGroupPage.generate_random_string(7)
        self.addEditGroupPage.add_group(grp_id, grp_name)
        assert self.addEditGroupPage.validate_SuccessUpdateMessage("successfully")
        time.sleep(5)
        self.groupsPage.click_AddNew()
        assert self.addEditGroupPage.validate_Add_Group_Modal()
        self.addEditGroupPage.add_group(grp_id, grp_name)
        expectedAlert ="Group ID already exists"
        actualAlert = self.addEditGroupPage.getErrorMessage()
        assert expectedAlert == actualAlert
        time.sleep(2)
        self.groupsPage.deleteGroupById(grp_id)

