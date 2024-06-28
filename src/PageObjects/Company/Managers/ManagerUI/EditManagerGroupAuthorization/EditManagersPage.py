import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class EditManagersPage(BasePage):
    saveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    CancelBtn = (By.XPATH, "(//a[contains(.,'Cancel')])[1]")
    AddEmployeeModalTitle = (By.XPATH, "//div[contains(.,'Add New Employees')][@class='popupHeading']")
    EmpName = (By.NAME, "employeeName")
    EmpNumber = (By.NAME, "phoneNumber")
    TermsCheckbox = (By.XPATH, "//label[contains(.,'Accept service terms')]")
    DownLoadLinkCheckbox = (By.XPATH, "//label[contains(.,'send App download link')]")
    AddBtn = (By.XPATH, "//button[contains(.,'Add')][contains(@class,'okBtn')]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteIcon = (By.XPATH, "(//img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditIcon = (By.XPATH, "(//img[contains(@src,'edit')])[1]")
    HeaderTitle = (By.XPATH, "//h2[contains(.,'Edit Managers')]")
    ShortName = (By.NAME, "employeeShortName")
    GroupAuthorizationSettings = (By.XPATH, "//h3[contains(.,'Group Authorization Settings')]")
    UserInfo = (By.XPATH, "//div[contains(@class,'userInfo')]")
    Logout = (By.XPATH, "//a[contains(@class,'Logout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def editManager(self, name, number):
        self.clickToElement(self.AddNewBtn)
        time.sleep(5)
        self.isElementDisplayed(self.AddEmployeeModalTitle)
        self.enterValueToTextbox(self.EmpName, name)
        self.enterValueToTextbox(self.EmpNumber, number)
        self.scrollIntoViewElement(self.TermsCheckbox)
        self.clickToElementByJavaScriptExecutor(self.TermsCheckbox)
        self.clickToElementByJavaScriptExecutor(self.DownLoadLinkCheckbox)
        self.clickToElement(self.AddBtn)
        if self.isElementDisplayed(self.ConfirmBtn):
            time.sleep(2)
            self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Employee Added -", name)

    def validateHeaderTitle(self):
        return self.isElementDisplayed(self.HeaderTitle)

    def validate_GroupAuthorizationSettings(self):
        return self.isElementDisplayed(self.GroupAuthorizationSettings)

    def set_ACL_for(self,entity, control):
        element_locator = (By.XPATH, "(//tr[contains(.,'"+entity+"')]/td/div/label[contains(@for,'"+control+"')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def click_saveBtn(self):
        self.clickToElement(self.saveBtn)

    def click_Cancel(self):
        self.clickToElementByJavaScriptExecutor(self.CancelBtn)

    def logout_user(self):
        self.clickToElementByJavaScriptExecutor(self.UserInfo)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.Logout)
        time.sleep(5)






