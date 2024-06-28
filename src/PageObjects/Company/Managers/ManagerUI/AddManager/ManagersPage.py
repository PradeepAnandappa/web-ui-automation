import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class ManagersPage(BasePage):
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    AddManagerModalTitle = (By.XPATH, "//div[contains(.,'Create a New Manager')][@class='popupHeading']")
    ManagerID = (By.NAME, "managerId")
    ManagerNumber = (By.NAME, "phoneNumber")
    Email = (By.NAME, "userEmail")
    TermsCheckbox = (By.XPATH, "//label[contains(.,'Accept service terms')]")
    DownLoadLinkCheckbox = (By.XPATH, "//label[contains(.,'send App download link')]")
    AddBtn = (By.XPATH, "//button[contains(.,'Add')][contains(@class,'okBtn')]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    FilterManagerIdBox = (By.XPATH, "(//input[@aria-label='Filter'])[2]")
    FilterNameBox = (By.XPATH, "(//input[@aria-label='Filter'])[3]")
    DeleteIcon = (By.XPATH, "(//img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditIcon = (By.XPATH, "(//img[contains(@src,'edit')])[1]")
    ViewIcon = (By.XPATH, "(//img[contains(@src,'view')])[1]")
    MultipleTab = (By.XPATH, "//li[text()='Multiple']")
    uploadBox = (By.XPATH, "//input[@type='file']")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    UserInfo = (By.XPATH, "//div/div[contains(@class,'userinfo') or contains(@class,'userInfo')]/span")
    ChildAccount = (By.XPATH, "(//li/a[contains(@class,'userChild')])[1]")
    Logout = (By.XPATH, "//a[contains(@class,'iconLogout')]")

    # Kindo table details


    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def addManager(self, mid, email, number):
        self.clickToElement(self.AddNewBtn)
        time.sleep(5)
        self.isElementDisplayed(self.AddManagerModalTitle)
        self.enterValueToTextbox(self.ManagerID, mid)
        self.enterValueToTextbox(self.Email, email)
        self.enterValueToTextbox(self.ManagerNumber, number)
        self.clickToElement(self.AddBtn)


    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)
        return flag

    def deleteManagerById(self, mid):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterManagerIdBox)
        self.enterValueToTextbox(self.FilterManagerIdBox, mid)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        self.clickToElement(self.ConfirmBtn)
        print("Manager deleted with number -", mid)


    def deleteManagerByName(self, name):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Manager deleted with name -", name)

    def click_edit_for_ManagerID(self, mid):
        time.sleep(3)
        self.clickToElementByJavaScriptExecutor(self.FilterManagerIdBox)
        self.enterValueToTextbox(self.FilterManagerIdBox, mid)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.EditIcon)

    def click_view_for_ManagerID(self, mid):
        time.sleep(3)
        self.clickToElementByJavaScriptExecutor(self.FilterManagerIdBox)
        self.enterValueToTextbox(self.FilterManagerIdBox, mid)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.ViewIcon)

    def add_multiple_employees(self, file_path):
        self.clickToElement(self.AddNewBtn)
        time.sleep(5)
        self.isElementDisplayed(self.AddEmployeeModalTitle)
        self.clickToElementByJavaScriptExecutor(self.MultipleTab)
        # self.enterValueToTextbox(self.uploadBox, filePath)
        element = self.driver.find_element(By.XPATH, "//input[@type='file']")
        element.send_keys(file_path)
        time.sleep(5)
        self.clickToElement(self.AddBtn)

    def validate_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'"+tabName+"')])[1]")
        return self.isElementDisplayed(element_locator)

    def click_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)

    def validate_Table_columnsName(self, name):
        element_locator = (By.XPATH, "//span[contains(@class,'k-column-title')][text()='"+name+"']")
        return self.isElementDisplayed(element_locator)

    def logout_user(self):
        self.clickOnElementByActionClass(self.UserInfo)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.Logout)
        time.sleep(5)


