import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class EditTimeClockReportPage(BasePage):
    Title = (By.XPATH, "//h1[contains(.,'Edit Reports')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    AccountReportsTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Account Reports')]")
    SummaryReportsTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Summary Reports')]")
    RunReportBtn = (By.XPATH, "//button[contains(.,'Run Report')]")
    Employee_radio = (By.XPATH, "//input[@id='Employee']/following-sibling::label")
    SelectDevice_dropdown = (By.XPATH, "//label[contains(.,'Select Device')]/following-sibling::span/span/span")
    SelectGroup_dropdown = (By.XPATH, "//label[contains(.,'Select Group')]/following-sibling::span/span/span")
    EmployeeReport = (By.XPATH, "(//td/a[contains(.,'Employee')])[1]")
    Timezone = (By.XPATH, "//select[@name='timezone']")
    ExportBtn = (By.XPATH, "//button[contains(.,'Export')]")
    EditTimeClockTab = (By.XPATH, "//a[contains(., 'Edit Time Clock')]")
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    DoneBtn = (By.XPATH, "//button[contains(.,'Done')]")
    Employees_Droplist = (By.XPATH, "(//td/span[contains(@class,'dropdownlist')])[1]")
    FilterDropdownSearchBox = (By.XPATH, "//span[contains(@class,'searchbox')]/input")
    SearchBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteIcon = (By.XPATH, "(//img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    ManuallyBtn = (By.XPATH, "(//div[contains(@class,'dropdownBlk')]/ul/li[contains(.,'Manually')])")
    Global_SearchBox = (By.XPATH, "//div[@class='searchFld']/input")
    SaveChangesBtn = (By.XPATH, "//button[contains(.,'Add New')]")


    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_AccountReportsPage(self):
        self.switchToWindow()
        return self.isElementDisplayed(self.AccountReportsTab)

    def isAvailable_RunReportBtn(self):
        return self.isElementDisplayed(self.RunReportBtn)

    def click_RunReportButton(self):
        self.clickToElement(self.RunReportBtn)

    def validate_EditReportPage(self):
        return self.isElementDisplayed(self.EditTimeClockTab)

    def validate_EditReports_tabs(self, tabName):
        element_locator = (By.XPATH, "//a[contains(.,'" + tabName + "')]")
        return self.isElementDisplayed(element_locator)

    def select_Export_option(self, value):
        self.clickToElementByJavaScriptExecutor(self.ExportBtn)
        time.sleep(1)
        element_locator = (By.XPATH, "//li[contains(.,'" + value + "')]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def click_AddNew(self):
        self.clickToElement(self.AddNewBtn)

    def click_Done(self):
        self.clickToElement(self.DoneBtn)

    def click_Manually(self):
        self.clickToElement(self.ManuallyBtn)

    def add_Employee_in_kendo(self, value):
        self.clickToElement(self.Employees_Droplist)
        time.sleep(1)
        self.enterValueToTextbox(self.FilterDropdownSearchBox, value)
        time.sleep(1)
        element_locator = (By.XPATH, "(//span[contains(.,'" + value + "')][contains(@class,'list-item-text')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def add_Start_Stage_in_kendo(self, value):
        element_locator = (By.XPATH, "(//td/span[contains(@class,'dropdownlist')])[3]")
        self.clickToElement(element_locator)
        time.sleep(1)
        element_locator = (By.XPATH, "(//span[contains(.,'" + value + "')][contains(@class,'list-item-text')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def add_End_Stage_in_kendo(self, value):
        element_locator = (By.XPATH, "(//td/span[contains(@class,'dropdownlist')])[4]")
        self.scrollIntoViewElement(element_locator)
        time.sleep(1)
        self.clickToElement(element_locator)
        time.sleep(1)
        element_locator = (By.XPATH, "(//span[contains(.,'" + value + "')][contains(@class,'list-item-text')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def add_ManagerNote_in_kendo(self, value):
        element_locator = (By.XPATH, "//td[14]/input")
        self.clickToElementByJavaScriptExecutor(element_locator)
        time.sleep(1)
        self.enterValueToTextbox(element_locator, value)

    def search_record(self, value):
        self.enterValueToTextbox(self.SearchBox, value)

    def delete_Record(self):
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)

    def edit_distance(self, value):
        element_locator = (By.XPATH, "(//td[13])[2]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        time.sleep(1)
        element_locator = (By.XPATH, "(//td[13]/input)[1]")
        self.enterValueToTextbox(element_locator, value)
        self.clickToElementByJavaScriptExecutor(self.Global_SearchBox)
