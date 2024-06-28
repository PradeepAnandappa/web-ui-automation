import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class MyReportPage(BasePage):
    UserInfo = (By.XPATH, "//h1[contains(.,' Reports Category ')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    CustomReportsTab = (By.XPATH, "//li[@class='TabbedPanelsTab'][contains(.,'Custom')]")




    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validate_MyReportsPage(self):
        self.switchToWindow()
        return self.isElementDisplayed(self.CustomReportsTab)
