import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class PayRollSettingsPage(BasePage):
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "//button[contains(.,'SAVE')]/preceding-sibling::a")
    LocationOptIn = (By.XPATH, "//label[contains(.,'Location Opt-in')]")
    PageHeader = (By.XPATH, "//h3[contains(.,'Payroll Profile')]")
    CompanyCode_textbox = (By.XPATH, "//label[contains(.,'Company Code')]/following-sibling::input")
    PayrollID_textbox = (By.XPATH, "//label[contains(.,'Payroll ID')]/following-sibling::input")
    EmployeeWageTypes_box = (By.XPATH, "//label[contains(.,'Employee Wage Types')]/following-sibling::div/input")
    EmployeeSkills_box = (By.XPATH, "//label[contains(.,'Employee Skills')]/following-sibling::div/input")
    CloseBtn = (By.XPATH, "//button[contains(.,'Close')]")
    OT_EarningCode_textbox = (By.XPATH, "//label[contains(.,'OT Earning code')]/following-sibling::input")
    DoubleOT_EarningCode_textbox = (By.XPATH, "//label[contains(.,'Double OT Earning code')]/following-sibling::input")
    Regular_EarningCode_textbox = (By.XPATH, "//label[contains(.,'Regular Earning code')]/following-sibling::input")
    Mileage_EarningCode_textbox = (By.XPATH, "//label[contains(.,'Mileage Earning code')]/following-sibling::input")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_pageHeader(self):
        return self.isElementDisplayed(self.PageHeader)

    def click_SaveBtn(self):
        self.clickToElement(self.SaveBtn)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value == actual:
            flag = bool(True)

        return flag

    def enterCompanyCode(self, code):
        self.enterValueToTextbox(self.CompanyCode_textbox, code)

    def getCompanyCode(self):
        return self.getElementValue(self.CompanyCode_textbox)

    def enterPayRollId(self, id):
        self.enterValueToTextbox(self.PayrollID_textbox, id)

    def getPayRollId(self):
        return self.getElementValue(self.PayrollID_textbox)

    def enterOT_EarningCode(self, code):
        self.enterValueToTextbox(self.OT_EarningCode_textbox, code)

    def getOT_EarningCode(self):
        return self.getElementValue(self.OT_EarningCode_textbox)

    def enterRegular_EarningCode(self, code):
        self.enterValueToTextbox(self.Regular_EarningCode_textbox, code)

    def clear_Regular_EarningCode(self):
        self.clear_textbox(self.Regular_EarningCode_textbox)

    def getRegular_EarningCode(self):
        return self.getElementValue(self.Regular_EarningCode_textbox)

    def enterMileage_EarningCode(self, code):
        self.enterValueToTextbox(self.Mileage_EarningCode_textbox, code)

    def clear_Mileage_EarningCode(self):
        self.clear_textbox(self.Mileage_EarningCode_textbox)

    def getMileage_EarningCode(self):
        return self.getElementValue(self.Mileage_EarningCode_textbox)

    def enterDoubleOT_EarningCode(self, code):
        self.enterValueToTextbox(self.DoubleOT_EarningCode_textbox, code)

    def getDoubleOT_EarningCode(self):
        return self.getElementValue(self.DoubleOT_EarningCode_textbox)

    def enterEmployeeWageType(self, type):
        self.enterValueToTextbox(self.EmployeeWageTypes_box, type)
        element = self.driver.find_element(By.XPATH, "//label[contains(.,'Employee Wage Types')]/following-sibling::div/input")
        element.send_keys(keys.Keys.ENTER)

    def validateEmployeeWageType(self, type):
        flag = bool(False)
        elementList = list((self.driver.find_elements(By.XPATH, "//label[contains(.,'Employee Wage Types')]/following-sibling::div/ul/li")))
        try:
            for element in elementList:
                print(element.text)
                if type in element.text:
                    flag = bool(True)
                    break
            return flag
        except:
         print("Entered EmployeeWageType - " +type+" not found")
         return flag

    def click_Hours_Interval(self, type):
        element_locator = (By.XPATH, "//label[contains(.,'Hours Interval')]/following-sibling::div/div/label[contains(.,'"+type+"')]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def get_active_interval(self):
        elementList = list((self.driver.find_elements(By.XPATH, "//label[contains(.,'Employee Wage Types')]/following-sibling::div/ul/li")))
        try:
            for element in elementList:
                print(element.text)
                if element.text == type:
                    flag = bool(True)
                    break
            return flag
        except:
         print("Active Interval - not found")
         return flag
