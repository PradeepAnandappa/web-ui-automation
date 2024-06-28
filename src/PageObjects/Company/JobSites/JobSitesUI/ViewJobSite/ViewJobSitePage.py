import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class ViewJobSitePage(BasePage):
    SiteName = (By.XPATH, "//label[contains(.,'Site Name')]/following-sibling::input")
    Address = (By.XPATH, "//textarea[@name='address']")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    PopupCancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')][contains(@class,'okBtn')])[1]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteLink = (By.XPATH, "//a[@class='deleteGrp']")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditLink = (By.XPATH, "//a[@class='editGrp']")
    HeaderTitle = (By.XPATH, "//h2[contains(.,'View Jobsite Information')]")
    ShortName = (By.NAME, "employeeShortName")
    GroupAuthorizationSettings = (By.XPATH, "//h3[contains(.,'Group Authorization Settings')]")
    BackButton = (By.XPATH, "//button[contains(.,'Back')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def validateHeaderTitle(self):
        return self.isElementDisplayed(self.HeaderTitle)

    def editJobSite(self):
        self.clickToElementByJavaScriptExecutor(self.EditLink)


    def validate_EditLink_enabled(self, name):
        flag = self.isElementDisabled(self.EditLink)
        if flag:
            flag = bool(False)
        else:
            flag = bool(True)
        return flag

    def validate_EditLink_disabled(self, name):
        return self.isElementDisabled(self.EditLink)

    def deleteJobSite(self):
        self.clickToElementByJavaScriptExecutor(self.DeleteLink)
        self.clickToElement(self.ConfirmBtn)

    def click_Save(self):
        self.clickToElement(self.SaveBtn)

    def click_Cancel(self):
        self.clickToElement(self.CancelBtn)

    def click_Back(self):
        self.clickToElement(self.BackButton)

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




