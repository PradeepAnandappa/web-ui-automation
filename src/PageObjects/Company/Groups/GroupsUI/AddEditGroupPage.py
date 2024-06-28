import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class AddEditGroupPage(BasePage):
    AddGroup_popupHeader = (By.XPATH, "//div[contains(.,'Add New Group')][@class='popupHeading']")
    GroupId_textbox = (By.XPATH, "//label[contains(.,'Phone Group ID')]/following-sibling::input")
    GroupName_textbox = (By.XPATH, "//label[contains(.,'Employee Group Name')]/following-sibling::input")
    NextBtn = (By.XPATH, "//button[contains(.,'Next')]")
    DoneBtn = (By.XPATH, "//button[contains(.,'Done')]")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    SearchBox1 = (By.XPATH, "(//input[@type='search'])[1]")
    PlusIcon = (By.XPATH, "//span[@class='addRemoveBtn']")
    SearchBox2 = (By.XPATH, "(//input[@type='search'])[2]")
    RemoveIcon = (By.XPATH, "//span[@class='addRemoveBtn addedItem']")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "//button[contains(.,'SAVE')]/preceding-sibling::a")
    EditPageHeader = (By.XPATH, "//h3[contains(.,'Edit Group')]")
    ErrorMessage = (By.XPATH, "//div[@class='fldMsg']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.getPageTitle("Group")

    def validate_EditPageHeader(self):
        return self.isElementDisplayed(self.EditPageHeader)

    def validate_Add_Group_Modal(self):
        return self.isElementDisplayed(self.AddGroup_popupHeader)

    def add_group(self, gid, name):
        self.enterValueToTextbox(self.GroupId_textbox, gid)
        self.enterValueToTextbox(self.GroupName_textbox, name)
        self.clickToElement(self.NextBtn)
        time.sleep(10)
        self.clickToElement(self.DoneBtn)

    def click_Done(self):
        self.clickToElement(self.DoneBtn)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)

        return flag

    def assignEmployeeToGroup(self, empid):
        self.scrollIntoViewElement(self.SearchBox1)
        time.sleep(2)
        self.enterValueToTextbox(self.SearchBox1, empid)
        self.clickToElementByJavaScriptExecutor(self.PlusIcon)

    def unassignEmployeeFromGroup(self, empid):
        self.enterValueToTextbox(self.SearchBox2, empid)
        self.clickToElementByJavaScriptExecutor(self.RemoveIcon)



    def validate_assignedEmployeeToGroup(self, empid):
        element_locator = (By.XPATH, "//div[contains(.,'Assigned Employee')]/following-sibling::div/div/table//td[contains(.,'"+empid+"')]")
        return self.isElementDisplayed(element_locator)

    def edit_GroupName(self, name):
        self.enterValueToTextbox(self.GroupName_textbox, name)
        time.sleep(10)

    def click_Save(self):
        self.clickToElement(self.SaveBtn)

    def click_Cancel(self):
        self.clickToElement(self.CancelBtn)

    def getErrorMessage(self):
        return self.getElementText(self.ErrorMessage)




