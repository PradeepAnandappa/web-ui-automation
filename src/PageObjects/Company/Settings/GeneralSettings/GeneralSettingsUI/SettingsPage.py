import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class SettingsPage(BasePage):
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    EmployeeTitle = (By.XPATH, "//label[contains(.,'Employee Title')]/following-sibling::input")
    GroupAlternate = (By.XPATH, "//label[contains(.,'Group Alternate')]/following-sibling::input")
    AddressAlternate = (By.XPATH, "//label[contains(.,'Address Alternate')]/following-sibling::input")
    WorkOrderAlternate = (By.XPATH, "//label[contains(.,'Work Order Alternate')]/following-sibling::input")
    BusinessEntityID = (By.XPATH, "//label[contains(.,'Business Entity ID')]/following-sibling::input")
    UserID = (By.XPATH, "//label[contains(.,'User ID')]/following-sibling::input")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    PrimaryEmail = (By.XPATH, "//label[contains(.,'Primary Contact Email')]/following-sibling::input")
    PrimaryContactPhone = (By.XPATH, "//label[contains(.,'Primary Contact Phone')]/following-sibling::input")
    NotificationEmail = (By.XPATH, "//label[contains(.,'Notifications Email')]/following-sibling::input")
    NotificationEmailLink = (By.XPATH, "//span[contains(.,'Same as Primary Contact')]")
    TimeZone_dropdown = (By.NAME, "basic_details.timezone")
    OrganizationName = (By.NAME, "basic_details.description")
    PopupCancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')][contains(@class,'okBtn')])[2]")



    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_account_details(self, attribute, value):
        element_locator = (By.XPATH, "//label[contains(.,'"+attribute+"')]/following-sibling::div/span[1]")
        attr = self.getElementText(element_locator)
        if attr == value:
            return bool(True)
        else:
            return bool(False)

    def validate_settings_tab(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'"+tabName+"')])[1]")
        return self.isElementDisplayed(element_locator)

    def click_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)

    def click_settings_tab(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)


    def update_EmployeeNomenclature(self, name):
        self.enterValueToTextbox(self.EmployeeTitle, name)
        self.clickToElement(self.SaveBtn)

    def set_PrimaryEmail_AsNotificationEmail(self):
        self.clickToElementByJavaScriptExecutor(self.NotificationEmailLink)

    def get_primaryEmailContactValue(self):
        return self.getElementValue(self.PrimaryEmail)

    def set_primaryEmailContact(self, email):
        self.enterValueToTextbox(self.PrimaryEmail, email)
        self.clickToElement(self.SaveBtn)

    def set_TimeZone(self, value):
        self.selectDropdownValueByText(self.TimeZone_dropdown, value)

    def get_timeZone(self):
        return self.get_selectedValueinDropdown(self.TimeZone_dropdown)

    def get_primaryContactNumber(self):
        return self.getElementValue(self.PrimaryContactPhone)

    def set_primaryContactNumber(self, phone):
        self.enterValueToTextbox(self.PrimaryContactPhone, phone)
        self.clickToElement(self.SaveBtn)

    def get_NotificationEmailValue(self):
        return self.getElementValue(self.NotificationEmail)

    def clear_organization_name(self):
        element = self.driver.find_element(By.NAME, "basic_details.description")
        element.click()
        element.clear()

    def dismiss_popup(self):
        self.clickToElement(self.PopupCancelBtn)

    def validate_popupMessage(self, msg):
        element_locator = (By.XPATH, "(//div[@class='msgContent']/div[contains(.,'"+msg+"')])[2]")
        return self.isElementDisplayed(element_locator)

    def get_selected_Date_format(self):
        elements = self.driver.find_elements(By.XPATH, "//label[contains(.,'Date Format')]/following-sibling::div/div/input")
        for element in elements:
           if element.is_selected():
               break

        return element.get_attribute('value')






