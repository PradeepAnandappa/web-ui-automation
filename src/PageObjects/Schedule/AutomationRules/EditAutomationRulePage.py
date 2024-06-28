import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class EditAutomationRulePage(BasePage):
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    AddRuleModalTitle = (By.XPATH, "//div[contains(.,'Add New Rule')][@class='popupHeading']")
    RuleName = (By.NAME, "ruleName")
    Status_Toggle = (By.XPATH, "//input[@name='active']/following-sibling::label")
    TimeBasedRule_Toggle = (By.XPATH, "//input[@name='cronRule']/following-sibling::label")
    EmpNumber = (By.NAME, "phoneNumber")
    EmpId = (By.NAME, "employeeId")
    RuleSelector = (By.NAME, "selector")
    EmployeeType = (By.NAME, "phoneType")
    EmpDesc = (By.NAME, "employeeDescription")
    NotificationEmail = (By.NAME, "emailNotified")
    TermsCheckbox = (By.XPATH, "//label[contains(.,'Accept service terms')]")
    DownLoadLinkCheckbox = (By.XPATH, "//label[contains(.,'send App download link')]")
    SaveBtn = (By.XPATH, "//button[contains(.,'Save')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteIcon = (By.XPATH, "(//li/img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditIcon = (By.XPATH, "(//li/img[contains(@src,'edit')])[1]")
    HeaderTitle = (By.XPATH, "//h2[contains(.,'Edit Rules Information')]")
    ShortName = (By.NAME, "employeeShortName")
    FirstName = (By.NAME, "employeeFirstName")
    RegularDailyHours = (By.NAME, "dailyRegularHrs")
    RegularDailyMinutes = (By.NAME, "dailyRegularMinutes")
    RegularEarningCode = (By.NAME, "reguerEarningCode")
    OTEarningCode = (By.NAME, "otEarningCode")
    DoubleOTEarningCode = (By.NAME, "doubleOTEarningCode")
    MileageDailyMinutes = (By.NAME, "mileageEarningcode")
    Employee_dropdown = (By.NAME, "device")
    Group_dropdown = (By.NAME, "group")
    Group_radioBtn = (By.XPATH, "// label[contains(., 'Group ID')]")
    StatusCode_dropdown = (By.NAME, "code")
    GroupSelectionHeader = (By.XPATH, "//h3[contains(.,'Employee / Group Code Selection')]")
    CancelEditAlert = (By.XPATH, "//div[@class='msgContent'][contains(.,'The changes are still unsaved. Are you sure you want to leave?')]")



    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def editRule(self, name, number):
        self.clickToElement(self.AddNewBtn)
        time.sleep(5)
        self.isElementDisplayed(self.AddRuleModalTitle)
        self.enterValueToTextbox(self.EmpName, name)
        self.enterValueToTextbox(self.EmpNumber, number)
        self.scrollIntoViewElement(self.TermsCheckbox)
        self.clickToElementByJavaScriptExecutor(self.TermsCheckbox)
        self.clickToElementByJavaScriptExecutor(self.DownLoadLinkCheckbox)
        self.clickToElement(self.AddBtn)
        if self.isElementDisplayed(self.ConfirmBtn):
            time.sleep(2)
            self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Employee Added -", name)

    def select_Status(self):
        self.clickToElementByJavaScriptExecutor(self.Status_Toggle)

    def select_Cron(self):
        self.clickToElementByJavaScriptExecutor(self.TimeBasedRule_Toggle)



    def validateHeaderTitle(self):
        return self.isElementDisplayed(self.HeaderTitle)

    def click_cancel(self):
        self.clickToElement(self.CancelBtn)

    def click_Yes(self):
        self.clickToElement(self.ConfirmBtn)

    def getRuleSelector(self):
        return self.getElementValue(self.RuleSelector)

    def setRuleSelector(self, code):
        return self.enterValueToTextbox(self.RuleSelector, code)

    def get_selectedEmployeeType(self):
        return self.get_selectedValueinDropdown(self.EmployeeType)

    def setCompanyCode(self, code):
        self.enterValueToTextbox(self.CompanyCode, code)

    def getCompanyCode(self):
        return self.getElementValue(self.CompanyCode)

    def getEmployeeDescription(self):
        return self.getElementValue(self.EmpDesc)

    def getEmployeeFirstName(self):
        return self.getElementValue(self.FirstName)

    def setEmployeeDescription(self, value):
        return self.enterValueToTextbox(self.EmpDesc, value)

    def setNotificationEmail(self, email):
        self.enterValueToTextbox(self.NotificationEmail, email)

    def click_Save(self):
        self.clickToElement(self.SaveBtn)

    def getNotificationEmail(self):
        return self.getElementValue(self.NotificationEmail)

    def set_PayRollHours(self, option):
        element_locator = (By.XPATH, "(//label[contains(.,'"+option+"')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def validate_isActiveRegularPayRollHours(self, option):
        element_locator = (By.XPATH, "(//label[contains(.,'"+option+"')]/parent::div/parent::div[contains(@class,'colBlk')])[1]")
        return self.isElementActive(element_locator)

    def click_on_Tab(self, option):
        element_locator = (By.XPATH, "(//li/a[contains(.,'" + option + "')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        print("Clicked on "+option+" Tab")

    def click_on_SettingsTab(self, option):
        element_locator = (By.XPATH, "(//li/div[contains(.,'" + option + "')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        print("Clicked on "+option+" Tab")

    def select_Trigger_Action(self, option):
        element_locator = (By.XPATH, "(//label[contains(.,'" + option + "')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        print("Clicked on "+option+" Trigger Action")

    def isSelected_Trigger_Action(self, option):
        #element_locator = (By.XPATH, "(//label[contains(.,'" + option + "')]/preceding-sibling::input)[1]")
        checkbox = self.driver.find_element(By.XPATH, "(//label[contains(.,'" + option + "')]/preceding-sibling::input)[1]")
        return checkbox.is_selected()

    def isAvailable_Tab(self, option):
        element_locator = (By.XPATH, "(//li/a[contains(.,'" + option + "')])[1]")
        return self.isElementDisplayed(element_locator)

    def select_Group(self, groupName):
        self.scrollIntoViewElement(self.GroupSelectionHeader)
        self.clickToElementByJavaScriptExecutor(self.Group_radioBtn)
        time.sleep(10)
        self.selectDropdownValueByText(self.Group_dropdown, groupName)

    def select_Employee(self, deviceName):
        self.scrollIntoViewElement(self.GroupSelectionHeader)
        self.selectDropdownValueByText(self.Employee_dropdown, deviceName)

    def select_StatusCode(self, statusCode):
        self.selectDropdownValueByText(self.StatusCode_dropdown, statusCode)

    def isAvailable_EditCancelAlert(self):
        return self.isElementDisplayed(self.CancelEditAlert)













