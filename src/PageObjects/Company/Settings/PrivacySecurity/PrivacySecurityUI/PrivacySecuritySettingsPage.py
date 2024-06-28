import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class PrivacySecuritySettingsPage(BasePage):
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "//button[contains(.,'SAVE')]/preceding-sibling::a")
    LocationOptIn = (By.XPATH, "//label[contains(.,'Location Opt-in')]")
    PageHeader = (By.XPATH, "//h3[contains(.,'Security Settings')]")
    TwoFactorTag = (By.XPATH, "//input[@id='towFactor']/following-sibling::label")
    SmsOptinTag = (By.XPATH, "//input[@id='smsOptin']/following-sibling::label")
    TwoFactorDisableModalTitle = (By.XPATH, "//div[contains(.,'Two Factor Authentication is disabled for')][@class='msgContent']")
    TwoFactorEnableModalTitle = (By.XPATH, "//div[contains(.,'Two Factor Authentication is now enabled for')][@class='msgContent']")
    CloseBtn = (By.XPATH, "//button[contains(.,'Close')]")
    TwoFactor_popupHeader = (By.XPATH, "//div[contains(.,'Two-Factor Authentication')][@class='popupHeading']")
    TwoFactor_popupContent = (By.XPATH, "//div[contains(.,'Some of the managers do not have an email id or mobile number added')][@class='popupContent']")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Okay, I understand')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_pageHeader(self):
        return self.isElementDisplayed(self.PageHeader)

    def validate_settings_tab(self, tabName):
        element_locator = (By.XPATH, "//div[contains(.,'"+tabName+"')][@class='optionHeading']")
        return self.isElementDisplayed(element_locator)

    def click_settings_tab(self, tabName):
        element_locator = (By.XPATH, "//div[contains(.,'" + tabName + "')][@class='optionHeading']")
        self.clickToElement(element_locator)

    def check_SettingTab_Highlited(self, tabName):
        element_locator = (By.XPATH, "//div[contains(.,'" + tabName + "')][@class='optionHeading']/parent::th")
        return self.isElementActive(element_locator)

    def select_SMSOptin(self):
        self.clickToElementByJavaScriptExecutor(self.SmsOptinTag)

    def validate_selectedOptInValue_inDropdown(self, value):
        flag = bool(False)
        actual = self.get_selectedValueinDropdown(self.OptIn_dropdown)
        if value == actual:
            flag = bool(True)

        return flag

    def select_TwofactorToggle(self):
        self.clickToElementByJavaScriptExecutor(self.TwoFactorTag)

    def validate_TwoFactorDisable_Modals(self):
        flag = bool(False)
        if self.isElementDisplayed(self.TwoFactorDisableModalTitle):
            self.clickToElement(self.CloseBtn)
            flag = bool(True)
        return flag

    def validate_TwoFactorEnable_Modals(self):
        flag = bool(False)
        if self.isElementDisplayed(self.TwoFactor_popupHeader):
            self.clickToElement(self.ConfirmBtn)
            time.sleep(2)
            if self.isElementDisplayed(self.TwoFactorEnableModalTitle):
                self.clickToElement(self.CloseBtn)
                flag = bool(True)
        return flag

    def validate_selectedAutoTrackValue_inDropdown(self, value):
        flag = bool(False)
        actual = self.get_selectedValueinDropdown(self.AutoTrack_dropdown)
        if value == actual:
            flag = bool(True)

        return flag


    def click_SaveBtn(self):
        self.clickToElement(self.SaveBtn)

    def click_SMS_Geo_Toggle(self):
        self.clickToElementByJavaScriptExecutor(self.SMS_GeoTag)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value == actual:
            flag = bool(True)

        return flag


