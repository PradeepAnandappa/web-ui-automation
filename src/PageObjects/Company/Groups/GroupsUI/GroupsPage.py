import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class GroupsPage(BasePage):
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    FilterNameBox = (By.XPATH, "(//input[@aria-label='Filter'])[2]")
    DeleteIcon = (By.XPATH, "(//img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditIcon = (By.XPATH, "(//img[contains(@src,'edit')])[1]")
    ViewIcon = (By.XPATH, "(//img[contains(@src,'view')])[1]")
    No_records_Message = (By.XPATH, "//td[contains(.,'No records available')]")
    UserInfo = (By.XPATH, "//div/span[contains(@class,'userAvatar')]")
    Logout = (By.XPATH, "//a[contains(@class,'Logout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.getPageTitle("Group")

    def click_AddNew(self):
        self.clickToElement(self.AddNewBtn)

    def deleteGroupById(self, number):
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Employee deleted with number -", number)


    def deleteGroupByName(self, name):
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Employee deleted with name -", name)

    def click_edit_for_GroupId(self, number):
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.EditIcon)

    def click_view_for_GroupId(self, number):
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.ViewIcon)

    def check_DeletedGroup(self, gid):
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, gid)
        time.sleep(5)
        return self.isElementDisplayed(self.No_records_Message)

    def check_ActionLink_disabled(self, action_link, gid):
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, gid)
        time.sleep(2)
        flag = bool(False)
        element_locator = (By.XPATH, "(//img[contains(@src,'" + action_link + "')]/parent::li)[1]")
        attr_value = self.get_AttributeValue(element_locator, "class")
        if attr_value == "disabled":
            flag = bool(True)
        return flag

    def check_ActionLink_enabled(self, action_link, name):
        flag = self.check_ActionLink_disabled(action_link, name)
        if flag:
            flag = bool(False)
        else:
            flag = bool(True)
        return flag

    def logout_user(self):
        self.clickOnElementByActionClass(self.UserInfo)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.Logout)
        time.sleep(5)