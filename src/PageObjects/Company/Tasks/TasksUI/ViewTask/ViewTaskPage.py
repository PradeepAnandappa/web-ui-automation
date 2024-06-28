import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class ViewTaskPage(BasePage):
    SiteName = (By.XPATH, "//label[contains(.,'Site Name')]/following-sibling::input")
    Address = (By.XPATH, "//textarea[@name='address']")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    DoneBtn = (By.XPATH, "//button[contains(.,'Done')][contains(@class,'okBtn')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    PopupCancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')][contains(@class,'okBtn')])[1]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteLink = (By.XPATH, "//a[@class='deleteGrp']")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditLink = (By.XPATH, "//a[@class='editGrp']")
    HeaderTitle = (By.XPATH, "//span[contains(.,'View Task')]")
    ShortName = (By.NAME, "employeeShortName")
    GroupAuthorizationSettings = (By.XPATH, "//h3[contains(.,'Group Authorization Settings')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def validateHeaderTitle(self):
        return self.isElementDisplayed(self.HeaderTitle)

    def click_editLink(self):
        self.clickToElementByJavaScriptExecutor(self.EditLink)

    def validate_EditLink(self):
        return self.isElementDisplayed(self.EditLink)

    def validate_DeleteLink(self):
        return self.isElementDisplayed(self.DeleteLink)

    def click_Done(self):
        self.clickToElement(self.DoneBtn)

    def click_deleteLink(self):
        self.clickToElementByJavaScriptExecutor(self.DeleteLink)

    def confirm_DeleteAction(self):
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Jobsite has been deleted")

    def cancel_deleteAction(self):
        self.clickToElementByJavaScriptExecutor(self.CancelBtn)

    def click_Save(self):
        self.clickToElement(self.SaveBtn)

    def click_Cancel(self):
        self.clickToElement(self.CancelBtn)

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

    def validate_GroupAuthorizationSettings(self):
        return self.isElementDisplayed(self.GroupAuthorizationSettings)

    def validate_Compnents(self, label):
        element_locator = (By.XPATH, "(//label[contains(.,'" + label + "')])[1]")
        return self.isElementDisplayed(element_locator)



