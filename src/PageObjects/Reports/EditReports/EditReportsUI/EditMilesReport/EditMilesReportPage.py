import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class EditMilesReportPage(BasePage):
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
    SaveChangesBtn = (By.XPATH, "//button[contains(.,'Save Changes')]")
    Employees_Droplist = (By.XPATH, "(//td/span[contains(@class,'dropdownlist')])[1]")
    FilterDropdownSearchBox = (By.XPATH, "//span[contains(@class,'searchbox')]/input")
    SearchBox = (By.XPATH, "//span[contains(@class,'searchbox')]/input")
    DeleteIcon = (By.XPATH, "(//li/img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    DistanceField = (By.XPATH, "//tr[@data-grid-row-index='0']/td[6]")
    Distance_inputbox = (By.XPATH, "//tr[@data-grid-row-index='0']/td[6]/input")
    NotesField = (By.XPATH, "//tr[@data-grid-row-index='0']/td[7]")
    Notes_inputbox = (By.XPATH, "//tr[@data-grid-row-index='0']/td[7]/input")
    FilterNameBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    AlertMessage = (By.XPATH, "//div[@class='floatingMessage ']")
    CloseAlertBtn = (By.XPATH, "//div[@class='closeMessage']")
    ManagerNote_popup_inputbox = (By.XPATH, "//input[@placeholder='Add manager notes']")
    ManagerNote_popup_SaveBtn = (By.XPATH, "//div[contains(@class,'popupBtn')]/button[contains(.,'Save')]")
    ManagerNote_popup_CancelBtn = (By.XPATH, "//div[contains(@class,'popupBtn')]/button[contains(.,'Cancel')]")
    ManagerNote_popup_YesBtn = (By.XPATH, "//div[contains(@class,'popupBtn')]/button[contains(.,'Yes')]")
    ManagerNote_popup_NoBtn = (By.XPATH, "//div[contains(@class,'popupBtn')]/button[contains(.,'No')]")

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

    def get_alertMessage(self):
        return self.getElementText(self.AlertMessage)

    def closeAlertMessage(self):
        self.clickToElementByJavaScriptExecutor(self.CloseAlertBtn)

    def searchEmployeeByName(self, name):
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(2)

    def add_Distance_in_kendo(self, distance):
        self.clickToElementByJavaScriptExecutor(self.DistanceField)
        self.enterValueToTextbox(self.Distance_inputbox, distance)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()


    def add_Notes_in_kendo(self, notes):
        self.clickToElementByJavaScriptExecutor(self.NotesField)
        self.enterValueToTextbox(self.Notes_inputbox, notes)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def enter_ManagerNoteOnPopup(self, notes):
        self.enterValueToTextbox(self.ManagerNote_popup_inputbox, notes)

    def click_SaveOnPopup(self):
        self.clickToElement(self.ManagerNote_popup_SaveBtn)

    def click_CancelOnPopup(self):
        self.clickToElement(self.ManagerNote_popup_CancelBtn)

    def click_YesOnPopup(self):
        self.clickToElement(self.ManagerNote_popup_YesBtn)

    def click_NoOnPopup(self):
        self.clickToElement(self.ManagerNote_popup_NoBtn)

    def remove_Notes(self):
        self.clickToElementByJavaScriptExecutor(self.NotesField)
        self.clear_textbox(self.Notes_inputbox)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def confirm_SaveChangesAlert(self):
        self.clickToElementByJavaScriptExecutor(self.ManagerNote_popup_YesBtn)

    def remove_distance(self):
        self.clickToElementByJavaScriptExecutor(self.DistanceField)
        self.clear_textbox(self.Distance_inputbox)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()


    def click_SaveChanges(self):
        self.clickToElement(self.SaveChangesBtn)

    def search_record(self, value):
        self.enterValueToTextbox(self.SearchBox, value)

    def delete_Record(self):
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
