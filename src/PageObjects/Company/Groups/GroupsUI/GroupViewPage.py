import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class GroupViewPage(BasePage):
    AddGroup_popupHeader = (By.XPATH, "//div[contains(@class,'popupHeading')]/span[contains(.,'View Group')]")
    GroupId = (By.XPATH, "//label[contains(.,'Employee Group ID')]/following-sibling::div")
    GroupName = (By.XPATH, "//label[contains(.,'Employee Group Name')]/following-sibling::div")
    DoneBtn = (By.XPATH, "//a[contains(.,'Done')]")
    SearchBox1 = (By.XPATH, "(//input[@type='search'])[1]")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "//button[contains(.,'SAVE')]/preceding-sibling::a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.getPageTitle("Group")

    def validate_View_Group_Modal(self):
        return self.isElementDisplayed(self.AddGroup_popupHeader)

    def validate_Employee_Group_Name(self):
        return self.isElementDisplayed(self.GroupName)

    def validate_Employee_Group_Id(self):
        return self.isElementDisplayed(self.GroupId)

    def click_Done(self):
        self.clickToElement(self.DoneBtn)
