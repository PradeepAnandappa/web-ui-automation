import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class EditFormsPage(BasePage):
    EditModalTitle = (By.XPATH, "//div[contains(.,'Edit Form')][@class='popupHeading']")
    FormName = (By.NAME, "formName")
    CancelBtn = (By.XPATH, "//a[contains(.,'Cancel')][contains(@class,'okBtn')]")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    ErrorFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgError")
    RefreshBtn = (By.XPATH, "(//button[contains(.,'Refresh')])[1]")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')][contains(@class,'okBtn')]")
    StatusToggle = (By.XPATH, "//input[@id='activeStatus']/following-sibling::label")



    def __init__(self, driver):
        super().__init__(driver)

    def click_StatusToggle(self):
        self.clickToElementByJavaScriptExecutor(self.StatusToggle)

    def click_closeModal(self):
        self.clickToElementByJavaScriptExecutor(self.ClosePopup)

    def editFormName(self, name):
        self.isElementDisplayed(self.EditModalTitle)
        time.sleep(2)
        self.enterValueToTextbox(self.FormName, name)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)
        return flag

    def validate_popupMessage(self, msg):
        element_locator = (By.XPATH, "//div[@class='msgContent']/div[contains(.,'"+msg+"')]")
        return self.isElementDisplayed(element_locator)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)

        return flag

    def validate_ErrorMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.ErrorFloatingMSG)
        print(actual)
        if value in actual:
            flag = bool(True)

        return flag

    def click_Save(self):
        self.clickToElement(self.SaveBtn)




