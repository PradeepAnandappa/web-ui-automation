import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class ViewAutomationRulePage(BasePage):
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    PopupCancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')][contains(@class,'okBtn')])[1]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteLink = (By.XPATH, "//a[@class='deleteGrp']")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditLink = (By.XPATH, "//a[@class='editGrp']")
    HeaderTitle = (By.XPATH, "//h2[contains(.,'View Rules Information')]")
    BackBtn = (By.XPATH, "//button[contains(.,'Back')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def validateHeaderTitle(self):
        return self.isElementDisplayed(self.HeaderTitle)

    def editRule(self):
        self.clickToElementByJavaScriptExecutor(self.EditLink)

    def deleteRule(self):
        self.clickToElementByJavaScriptExecutor(self.DeleteLink)
        self.clickToElement(self.ConfirmBtn)

    def click_Save(self):
        self.clickToElement(self.SaveBtn)

    def click_Cancel(self):
        self.clickToElement(self.CancelBtn)

    def click_Back(self):
        self.clickToElement(self.BackBtn)

    def dismiss_popup(self):
        self.clickToElement(self.PopupCancelBtn)

    def validate_popupMessage(self, msg):
        element_locator = (By.XPATH, "(//div[@class='msgContent']/div[contains(.,'"+msg+"')])[2]")
        return self.isElementDisplayed(element_locator)

    def validate_FloatingMessage(self, msg):
        element_locator = (By.XPATH, "//div[contains(@class,'floatingMessage')][contains(.,'"+msg+"')]")
        return self.isElementDisplayed(element_locator)

    def click_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)





