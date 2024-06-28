import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class EditJobSiteMapPage(BasePage):
    ModalTitle = (By.XPATH, "//div[contains(.,'GeoZone')][@class='popupHeading']")
    SiteName = (By.XPATH, "//label[contains(.,'Site Name')]/following-sibling::input")
    Address = (By.XPATH, "//textarea[@name='address']")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    PopupCancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')][contains(@class,'okBtn')])[2]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteIcon = (By.XPATH, "(//li/img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditIcon = (By.XPATH, "(//li/img[contains(@src,'edit')])[1]")
    HeaderTitle = (By.XPATH, "//h2[contains(.,'Edit Jobsite Information')]")


    def __init__(self, driver):
        super().__init__(driver)


    def validateModalHeaderTitle(self):
        return self.isElementDisplayed(self.ModalTitle)

    def editJobSiteName(self, name):
        self.enterValueToTextbox(self.SiteName)

    def clearJobSiteName(self):
        element = self.driver.find_element(By.XPATH, "//label[contains(.,'Site Name')]/following-sibling::input")
        element.click()
        element.clear()

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




