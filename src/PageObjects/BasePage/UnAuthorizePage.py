from selenium.webdriver.common.by import By
from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class UnAuthorizePage(BasePage):
    PageHeader = (By.XPATH, "//h2[contains(.,'Unauthorized')]")
    BackLink = (By.XPATH, "//a[contains(.,'Back')]")
    ScheduleLink = (By.XPATH, "//li/a[contains(@href,'workorder')]")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_pageHeader(self):
        return self.isElementDisplayed(self.PageHeader)

    def click_back(self):
        self.clickToElementByJavaScriptExecutor(self.BackLink)