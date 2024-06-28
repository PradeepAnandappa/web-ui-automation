import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class AccountReportPage(BasePage):
    UserInfo = (By.XPATH, "//h1[contains(.,' Reports Category ')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    AccountReportsTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Account Reports')]")
    SummaryReportsTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Summary Reports')]")
    RunReportBtn = (By.XPATH, "//button[contains(.,'Run Report')]")
    Employee_radio = (By.XPATH, "//input[@id='Employee']/following-sibling::label")
    SelectDevice_dropdown = (By.XPATH, "//label[contains(.,'Select Device')]/following-sibling::span/span/span")
    SelectGroup_dropdown = (By.XPATH, "//label[contains(.,'Select Group')]/following-sibling::span/span/span")
    EmployeeReport = (By.XPATH, "(//td/a[contains(.,'Employee')])[1]")
    Timezone = (By.XPATH, "//select[@name='timezone']")


    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_AccountReportsPage(self):
        self.switchToWindow()
        return self.isElementDisplayed(self.AccountReportsTab)

    def isAvailable_RunReportBtn(self):
        return self.isElementDisplayed(self.RunReportBtn)

    def click_RunReportButton(self):
        self.clickToElement(self.RunReportBtn)
