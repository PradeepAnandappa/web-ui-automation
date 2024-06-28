import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class ReportPage(BasePage):
    UserInfo = (By.XPATH, "//div[@class='topheader']/div[contains(@class,'userinfo2')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    RunReports = (By.XPATH, "//a[contains(., 'Run Reports')]")
    EditReports = (By.XPATH, "//a[contains(., 'Edit reports')]")
    ScheduleReports = (By.XPATH, "//a[contains(., 'Schedule reports')]")
    Location = (By.XPATH, "//ul[@class='typeMenu']/li/a[contains(.,'Location')]")
    Account = (By.XPATH, "//ul[@class='typeMenu']/li/a[contains(.,'Account')]")
    Time = (By.XPATH, "//ul[@class='typeMenu']/li/a[contains(.,'Time')]")
    FieldData = (By.XPATH, "//ul[@class='typeMenu']/li/a[contains(.,'Field Data')]")
    WorkOrder = (By.XPATH, "//ul[@class='typeMenu']/li/a[contains(.,'Work Order')]")
    NewUIReportsBtn = (By.ID, "new_ui_report_navigation_btn")
    RunReportBtn = (By.XPATH, "//button[contains(.,'Run Report')]")
    Employee_radio =(By.XPATH, "//input[@id='Employee']/following-sibling::label")
    SelectDevice_dropdown = (By.XPATH, "//label[contains(.,'Select Device')]/following-sibling::span/span/span")
    SelectGroup_dropdown = (By.XPATH, "//label[contains(.,'Select Group')]/following-sibling::span/span/span")
    EmployeeReport = (By.XPATH, "(//td/a[contains(.,'Employee')])[1]")
    Timezone = (By.XPATH, "//select[@name='timezone']")
    StartDate_inputbox = (By.XPATH, "//label[contains(.,'Start Date & Time')]/following-sibling::div/span/input")
    EndDate_inputbox = (By.XPATH, "//label[contains(.,'End Date & Time')]/following-sibling::div/span/input")





    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def logout_user(self):
        self.clickToElement(self.UserInfo)
        time.sleep(5)
        self.clickToElement(self.Logout)
        time.sleep(5)

    def validate_parent_child_tree_under_user_profile(self):
        self.clickToElement(self.UserInfo)
        time.sleep(5)
        return self.isElementDisplayed(self.ChildAccount)

    def click_newUI_Reports(self):
        self.clickToElementByJavaScriptExecutor(self.NewUIReportsBtn)


    def click_Employee_Reports(self):
        self.clickToElementByJavaScriptExecutor(self.EmployeeReport)

    def validate_tab_RunReports(self):
        return self.isElementDisplayed(self.RunReports)

    def validate_tab_EditReports(self):
        return self.isElementDisplayed(self.EditReports)

    def click_EditReportsTab(self):
        self.clickToElementByJavaScriptExecutor(self.EditReports)

    def validate_tab_ScheduleReports(self):
        return self.isElementDisplayed(self.ScheduleReports)

    def validate_Report_type_tabs(self, tabName):
        element_locator = (By.XPATH, "//ul[@class='typeMenu']/li/a[contains(.,'"+tabName+"')]")
        return self.isElementDisplayed(element_locator)

    def click_report_type_tab(self, tabName):
        element_locator = (By.XPATH, "//ul[@class='typeMenu']/li/a[contains(.,'" + tabName + "')]")
        self.clickToElement(element_locator)

    def isAvailable_RunReportBtn(self):
        return self.isElementDisplayed(self.RunReportBtn)

    def selectEmployee(self, empName):
        self.clickToElementByJavaScriptExecutor(self.Employee_radio)
        self.clickToElementByJavaScriptExecutor(self.SelectDevice_dropdown)
        element_locator = (By.XPATH, "(//span[contains(.,'" + empName + "')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def selectGroup(self, groupName):
        self.clickToElementByJavaScriptExecutor(self.SelectGroup_dropdown)
        element_locator = (By.XPATH, "(//span[contains(.,'" + groupName + "')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def validate_Default_Group_Selection(self):
        return self.getElementText(self.SelectGroup_dropdown)

    def click_RunReportButton(self):
        self.clickToElement(self.RunReportBtn)

    def get_Timezone(self):
        return self.get_selectedValueinDropdown(self.Timezone)

    def set_Timezone(self, timezone):
        self.selectDropdownValueByText(self.Timezone, timezone)

    def select_StartDate(self, startDate):
        self.enterValueToTextboxByJavascriptExecutor(self.StartDate_inputbox, startDate)

    def select_EndDate(self, endDate):
        self.enterValueToTextboxByJavascriptExecutor(self.StartDate_inputbox, endDate)








