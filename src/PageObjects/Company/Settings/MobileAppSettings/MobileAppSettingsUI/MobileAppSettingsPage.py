import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class MobileAppSettingsPage(BasePage):
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "//button[contains(.,'SAVE')]/preceding-sibling::a")
    OptIn_dropdown = (By.XPATH, "//select[@name='mobileApp.default_optin']")
    AutoTrack_dropdown = (By.XPATH, "//select[@name='mobileApp.autotrack']")
    SMS_GeoTag = (By.XPATH, "//input[@id='SMSGeoTag']/following-sibling::label")
    CustomerMandatoryTag = (By.XPATH, "//input[@id='mandatorySelection']/following-sibling::label")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    ZoneRadius = (By.XPATH, "//input[@name='mobileApp.default_zone_radius']")
    PageHeader = (By.XPATH, "//h3[contains(.,'Location Tracking')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_MobileAppSettingPageHeader(self):
        return self.isElementDisplayed(self.PageHeader)

    def validate_account_details(self, attribute, value):
        AddNewBtn = (By.XPATH, "//label[contains(.,'"+attribute+"')]/following-sibling::div/span[1]")
        attr = self.getElementText(AddNewBtn)
        if attr == value:
            return bool(True)
        else:
            return bool(False)


    def get_ZoneRadius(self):
        return self.get_AttributeValue(self.ZoneRadius, "value")

    def validate_settings_tab(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'"+tabName+"')])[1]")
        return self.isElementDisplayed(element_locator)

    def click_settings_tab(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)

    def select_Optin(self, option):
        self.selectDropdownValueByText(self.OptIn_dropdown, option)

    def validate_selectedOptInValue_inDropdown(self, value):
        flag = bool(False)
        actual = self.get_selectedValueinDropdown(self.OptIn_dropdown)
        if value == actual:
            flag = bool(True)

        return flag

    def select_AutoTrack(self, option):
        self.selectDropdownValueByText(self.AutoTrack_dropdown, option)

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

    def validate_SuccessUpdateMessage(self, value ):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value == actual:
            flag = bool(True)

        return flag

    def select_requiredAttachmentForAttribute(self, attributeName, attachmentName):
        element_locator = (By.XPATH, "//tr[contains(.,'"+attributeName+"')]/td/div[@class='attachmentWrap']/div/div/input")
        option_locator = (By.XPATH, "//label/span[contains(.,'"+attachmentName+"')]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        time.sleep(2)
        self.getElementText(option_locator)
        self.clickToElementByJavaScriptExecutor(option_locator)

    def remove_selected_requiredAttachmentForAttribute(self, attributeName, attachmentName):
        element_locator = (By.XPATH, "//tr[contains(.,'" + attributeName + "')]/td/div[@class='attachmentWrap']/div/div/div/span[contains(.,'"+attachmentName+"')]/following-sibling::span/span[contains(@class, 'chip-remove-action')]/span")
        self.clickToElementByJavaScriptExecutor(element_locator)


    def validate_requiredAttachmentForAttribute(self, attributeName, attachmentName):
        element_locator = (By.XPATH, "//tr[contains(.,'" + attributeName + "')]/td/div[@class='attachmentWrap']/div/div/div/span/li[contains(.,'"+attachmentName+"')]")
        return self.isElementDisplayed(element_locator)







