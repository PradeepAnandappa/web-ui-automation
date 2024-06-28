import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class EmployeeReportPage(BasePage):
    UserInfo = (By.XPATH, "//h1[contains(.,' Reports Category ')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    AccountReportsTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Account Reports')]")
    SummaryReportsTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Summary Reports')]")



    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_EmployeeReportsPage(self):
        self.switchToWindow()
        return self.isElementDisplayed(self.AccountReportsTab)
