import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class DebugReportPage(BasePage):
    UserInfo = (By.XPATH, "//h1[contains(.,' Reports Category ')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    DebugLogTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Debug Logs')]")




    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_DebugReportsPage(self):
        self.switchToWindow()
        return self.isElementDisplayed(self.DebugLogTab)

    def validate_Top_tab(self, tabName):
        element_locator = (By.XPATH, "//li[contains(.,'" + tabName + "')]")
        return self.isElementDisplayed(element_locator)
