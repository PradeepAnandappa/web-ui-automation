import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class EditTaskPage(BasePage):
    EditModalTitle = (By.XPATH, "//div[contains(.,'Edit Task')][@class='popupHeading']")
    TaskName = (By.XPATH, "//label[contains(.,'Task Name')]/following-sibling::input")
    TaskId = (By.XPATH, "//label[contains(.,'Task ID')]/following-sibling::input")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')][contains(@class,'okBtn')]")
    StatusToggle = (By.XPATH, "//label[@for='activeStatus']")
    AdvancedSetup = (By.XPATH, "//span[contains(.,'Advanced Setup')]")
    ReferenceId = (By.XPATH, "//label[contains(.,'Reference ID')]/following-sibling::input")
    SourceId = (By.XPATH, "//label[contains(.,'Source ID')]/following-sibling::input")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    CancelBtn = (By.XPATH, "//a[contains(.,'Cancel')][contains(@class,'okBtn')]")
    EditIcon = (By.XPATH, "(//li/img[contains(@src,'edit')])[1]")
    ViewIcon = (By.XPATH, "(//li/img[contains(@src,'view')])[1]")
    MultipleTab = (By.XPATH, "//li[text()='Multiple']")
    uploadBox = (By.XPATH, "//input[@type='file']")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    ErrorFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgError")
    BulkDeleteBtn = (By.XPATH, "(//button[contains(.,'Bulk Delete')])[1]")
    ShowStatus_dropdown = (By.XPATH, "(//span[contains(.,'Show Status')]/following-sibling::select)[1]")
    RefreshBtn = (By.XPATH, "(//button[contains(.,'Refresh')])[1]")

    # Kindo table details


    def __init__(self, driver):
        super().__init__(driver)


    def select_Status(self):
        self.clickToElementByJavaScriptExecutor(self.StatusToggle)

    def validate_modalTitle(self):
        return self.isElementDisplayed(self.EditModalTitle)

    def click_Save(self):
        self.clickToElement(self.SaveBtn)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)
        return flag

    def validate_ErrorAlertMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.ErrorFloatingMSG)
        if value in actual:
            flag = bool(True)
        return flag

    def validate_popupMessage(self, msg):
        element_locator = (By.XPATH, "//div[@class='msgContent']/div[contains(.,'"+msg+"')]")
        return self.isElementDisplayed(element_locator)

    def validate_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'"+tabName+"')])[1]")
        return self.isElementDisplayed(element_locator)

    def click_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)

    def validate_Table_columnsName(self, name):
        element_locator = (By.XPATH, "//span[contains(@class,'k-column-title')][text()='"+name+"']")
        return self.isElementDisplayed(element_locator)

    def editTaskName(self, name):
        self.enterValueToTextbox(self.TaskName, name)

    def editTaskId(self, tid):
        self.enterValueToTextbox(self.TaskId, tid)

    def click_AdvanceSetup(self):
        self.clickToElementByJavaScriptExecutor(self.AdvancedSetup)

    def editReferenceID(self, ref):
        self.enterValueToTextbox(self.ReferenceId, ref)

    def editSourceId(self, sid):
        self.enterValueToTextbox(self.SourceId, sid)




