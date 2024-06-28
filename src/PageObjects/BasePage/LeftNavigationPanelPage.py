import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class LeftNavigationPanelPage(BasePage):
    CompanyLink = (By.XPATH, "//a[contains(@class,'iconCompany')]")
    ReportsLink = (By.XPATH, "//a[contains(@class,'iconReport')]")
    ScheduleLink = (By.XPATH, "//a[contains(@class,'iconSchedule')]")
    MonitorLink = (By.XPATH, "//a[contains(@class,'iconMonitor')]")
    EmployeeLink = (By.XPATH, "//a[contains(@class,'iconEmployee')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElementByJavaScriptExecutor(self.CompanyLink)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.EmployeeLink)
        time.sleep(2)

    def click_Reports(self):
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.ReportsLink)
        print("Click on Report Link under left panel")

    def click_Schedule(self):
        self.clickToElementByJavaScriptExecutor(self.ScheduleLink)

    def click_Monitor(self):
        self.clickToElementByJavaScriptExecutor(self.MonitorLink)


