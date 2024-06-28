import time

from pytest_testrail.plugin import pytestrail
from Configuration.config import config
from src.PageObjects.Company.Forms.FormsUI.AddForm.FormsPage import FormsPage
from src.PageObjects.Company.Forms.FormsUI.EditForm.EditFormsPage import EditFormsPage
from src.PageObjects.Login_Logout.LoginPage import LoginPage
from src.PageObjects.Monitor.MonitorPage import MonitorPage
from src.PageObjects.BasePage.LeftNavigationPanelPage import LeftNavigationPanelPage
from src.PageObjects.Company.Employees.MainView.EmployeesCRUD_UI.EmployeesPage import EmployeesPage
from src.BaseFile.BaseTest import BaseTest
from pathlib import Path



class Test_Company(BaseTest):
    @pytestrail.case('C28050', 'C28051', 'C28052', 'C28106', 'C28107', 'C28111', 'C28090', 'C28091', 'C28093')
    def test_addForms(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.user_login(config.AccoundID, config.UserName, config.Password)
        self.monitorPage = MonitorPage(self.driver)
        page_found = self.monitorPage.getPageTitle("Monitor")
        assert page_found
        self.leftNavigationPanelPage = LeftNavigationPanelPage(self.driver)
        self.leftNavigationPanelPage.click_Company()
        self.employeesPage = EmployeesPage(self.driver)
        time.sleep(2)
        self.employeesPage.click_company_icon("Forms")
        self.formsPage = FormsPage(self.driver)
        self.formsPage.click_Addnew()
        time.sleep(1)
        self.formsPage.enterFormName("LoginForm")
        assert self.formsPage.check_AddButton_disabled()
        file_path = str(Path.home()) + "\PycharmProjects\/allGeo_webApp\src\Resources\LoginForm.html"
        self.formsPage.uploadHTML(file_path)
        time.sleep(2)
        assert self.formsPage.check_AddButton_enabled()
        self.formsPage.click_Add()
        assert self.formsPage.validate_SuccessUpdateMessage("successfully")
        self.formsPage.click_edit_for_TaskName("LoginForm")
        self.editFormsPage = EditFormsPage(self.driver)
        self.editFormsPage.editFormName("NewLoginForm")
        self.editFormsPage.click_StatusToggle()
        self.editFormsPage.click_Save()
        time.sleep(2)
        self.formsPage.select_Status("Inactive")
        self.formsPage.deleteFormByName("NewLoginForm")
        time.sleep(2)
        self.formsPage.confirm_DeleteAction()



