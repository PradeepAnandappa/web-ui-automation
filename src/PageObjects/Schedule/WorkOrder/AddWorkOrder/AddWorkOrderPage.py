import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class AddWorkOrderPage(BasePage):
    Title = (By.XPATH, "//div[@class='main_heading'][contains(.,'Upload Work Order')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    ManualUploadTab = (By.XPATH, "//li[@class='manual_tab']/a")
    BulkUploadTab = (By.XPATH, "//li[@class='bulk_tab ']/a")
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    SaveBtn = (By.XPATH, "//button[contains(.,'Save')]")
    Employees_Droplist = (By.XPATH, "(//td/span[contains(@class,'dropdownlist')])[1]")
    CancelBtn = (By.XPATH, "//button[contains(.,'Cancel')]")


    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.getElementText(self.Title)

    def isAvailable_ManualUploadTab(self):
        return self.isElementDisplayed(self.ManualUploadTab)

    def click_BulkUploadButton(self):
        self.clickToElement(self.BulkUploadTab)

    def select_Export_option(self, value):
        self.clickToElementByJavaScriptExecutor(self.ExportBtn)
        time.sleep(1)
        element_locator = (By.XPATH, "//li[contains(.,'" + value + "')]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def click_AddNew(self):
        self.clickToElement(self.AddNewBtn)

    def click_Save(self):
        self.clickToElementByJavaScriptExecutor(self.SaveBtn)

    def enterFieldvalue(self, fieldName, fieldValue):
        if fieldName == 'Work Order Id':
            element_locator = (By.XPATH, "(//div[@class='emp_table_block']/div//tr[1]/td/input)[1]")
            self.enterValueToTextbox(element_locator, fieldValue)
        elif fieldName == 'Employee Name':
            element_locator = (By.XPATH, "//div[@class='emp_table_block']/div//tr[1]/td[3]//button")
            self.clickToElement(element_locator)
            element_locator = (By.XPATH, "(//span[contains(.,'"+fieldValue+"')])[1]")
            self.clickToElementByJavaScriptExecutor(element_locator)
        elif fieldName == 'Start Time':
            element_locator = (By.XPATH, "//div[@class='emp_table_block']/div//tr[1]/td[5]//input")
            self.enterValueToTextboxByJavascriptExecutor(element_locator, fieldValue)
        elif fieldName == 'Stop Time':
            element_locator = (By.XPATH, "//div[@class='emp_table_block']/div//tr[1]/td[6]//input")
            self.enterValueToTextboxByJavascriptExecutor(element_locator, fieldValue)


    def click_Manually(self):
        self.clickToElement(self.ManuallyBtn)

    def search_record(self, value):
        self.enterValueToTextbox(self.SearchBox, value)

    def delete_Record(self):
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)

