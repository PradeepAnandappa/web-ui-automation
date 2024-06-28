import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class EditEmployeesPage(BasePage):
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    AddEmployeeModalTitle = (By.XPATH, "//div[contains(.,'Add New Employees')][@class='popupHeading']")
    EmpName = (By.NAME, "employeeName")
    EmpNumber = (By.NAME, "phoneNumber")
    EmpId = (By.NAME, "employeeId")
    CompanyCode = (By.NAME, "companyCode")
    EmployeeType = (By.NAME, "phoneType")
    EmpDesc = (By.NAME, "employeeDescription")
    NotificationEmail = (By.NAME, "emailNotified")
    TermsCheckbox = (By.XPATH, "//label[contains(.,'Accept service terms')]")
    DownLoadLinkCheckbox = (By.XPATH, "//label[contains(.,'send App download link')]")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteIcon = (By.XPATH, "(//li/img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditIcon = (By.XPATH, "(//li/img[contains(@src,'edit')])[1]")
    HeaderTitle = (By.XPATH, "//h2[contains(.,'Edit Employee Information')]")
    ShortName = (By.NAME, "employeeShortName")
    FirstName = (By.NAME, "employeeFirstName")
    RegularDailyHours = (By.NAME, "dailyRegularHrs")
    RegularDailyMinutes = (By.NAME, "dailyRegularMinutes")
    RegularEarningCode = (By.NAME, "reguerEarningCode")
    OTEarningCode = (By.NAME, "otEarningCode")
    DoubleOTEarningCode = (By.NAME, "doubleOTEarningCode")
    MileageDailyMinutes = (By.NAME, "mileageEarningcode")
    ActiveStatusToggle = (By.XPATH, "//label[@for='activeEmployee']")
    PayDataADPToggle = (By.XPATH, "//label[@for='PayData']")
    PayDataCheckbox = (By.ID, "PayData")
    AttendanceADPToggle = (By.XPATH, "//label[@for='Attendance']")
    AttendanceCheckbox = (By.ID, "Attendance")

    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def editEmployee(self, name, number):
        self.clickToElement(self.AddNewBtn)
        time.sleep(5)
        self.isElementDisplayed(self.AddEmployeeModalTitle)
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

    def validateHeaderTitle(self):
        return self.isElementDisplayed(self.HeaderTitle)

    def click_cancel(self):
        self.clickToElement(self.CancelBtn)

    def getEmployeeCode(self):
        return self.getElementValue(self.EmpId)

    def setEmployeeCode(self, code):
        return self.enterValueToTextbox(self.EmpId, code)

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

    def isAvailable_Tab(self, option):
        element_locator = (By.XPATH, "(//li/a[contains(.,'" + option + "')])[1]")
        return self.isElementDisplayed(element_locator)


    def enter_Daily_Regular_hours(self, str):
        self.enterValueToTextboxByJavascriptExecutor(self.RegularDailyHours, str)

    def enter_Daily_Regular_minutes(self, str):
        self.enterValueToTextboxByJavascriptExecutor(self.RegularDailyMinutes, str)

    def setRegularEarningCode(self, code):
        self.enterValueToTextbox(self.RegularEarningCode, code)

    def setOTEarningCode(self, code):
        self.enterValueToTextbox(self.RegularEarningCode, code)

    def getRegularEarningCode(self, code):
        return self.getElementValue(self.RegularEarningCode)

    def setMileageEarningCode(self, code):
        self.enterValueToTextbox(self.MileageDailyMinutes, code)

    def getMileageEarningCode(self, code):
        return self.getElementValue(self.MileageDailyMinutes)

    def click_Status_Toggle(self):
        self.clickToElementByJavaScriptExecutor(self.ActiveStatusToggle)

    def click_PayData_Toggle(self):
        self.clickToElementByJavaScriptExecutor(self.PayDataADPToggle)

    def click_Attendance_Toggle(self):
        self.clickToElementByJavaScriptExecutor(self.AttendanceADPToggle)

    def get_PayData_Toggle_Enabled(self):
        return self.PayDataCheckbox.is_enabled()

    def get_Attendance_Toggle_Enabled(self):
        return self.AttendanceADPToggle.is_enabled()

















