import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Groups.GroupsUI.AddEditGroupPage import AddEditGroupPage
from src.PageObjects.Company.Groups.GroupsUI.GroupViewPage import GroupViewPage
from src.PageObjects.Company.Groups.GroupsUI.GroupsPage import GroupsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest


class Test_Groups(BaseTest):
    @pytestrail.case('C24917', 'C26835', 'C24911')
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

        self.groupsPage.click_view_for_GroupId(grp_id)
        self.groupViewPage = GroupViewPage(self.driver)
        assert self.groupViewPage.validate_View_Group_Modal()
        assert self.groupViewPage.validate_Employee_Group_Id()
        assert self.groupViewPage.validate_Employee_Group_Name()
        self.groupViewPage.click_Done()
        time.sleep(2)
        self.groupsPage.deleteGroupById(grp_id)


