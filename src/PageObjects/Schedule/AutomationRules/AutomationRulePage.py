import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class AutomationRulePage(BasePage):
    PageHeader = (By.XPATH, "//h2[contains(.,'Rules')]")
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    AddModalTitle = (By.XPATH, "//div[contains(.,'Add New Rule')][@class='popupHeading']")
    RuleId = (By.NAME, "ruleName")
    AddBtn = (By.XPATH, "//button[contains(.,'Add')][contains(@class, 'okBtn')]")
    CloseBtn = (By.CLASS_NAME, "closePopup")
    FilterNameBox = (By.XPATH, "(//input[@aria-label='Filter'])[2]")
    FilterIdBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    FilterGeoZoneBox = (By.XPATH, "(//input[@aria-label='Filter'])[3]")
    DeleteIcon = (By.XPATH, "(//img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    CancelBtn = (By.XPATH, "//a[contains(.,'Cancel')][contains(@class,'okBtn')]")
    EditIcon = (By.XPATH, "(//img[contains(@src,'edit')])[1]")
    ViewIcon = (By.XPATH, "(//img[contains(@src,'view')])[1]")
    MultipleTab = (By.XPATH, "//li[text()='Multiple']")
    uploadBox = (By.XPATH, "//input[@type='file']")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    ErrorFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgError")
    BulkDeleteBtn = (By.XPATH, "(//button[contains(.,'Bulk Delete')])[1]")
    ShowStatus_dropdown = (By.XPATH, "(//span[contains(.,'Show Status')]/following-sibling::select)[1]")
    RefreshBtn = (By.XPATH, "(//button[contains(.,'Refresh')])[1]")
    UserInfo = (By.XPATH, "//div/div[contains(@class,'userinfo') or contains(@class,'userInfo')]/span")
    ChildAccount = (By.XPATH, "(//li/a[contains(@class,'userChild')])[1]")
    Logout = (By.XPATH, "//a[contains(@class,'iconLogout')]")

    # Kindo table details


    def __init__(self, driver):
        super().__init__(driver)

    def validate_PageHeader(self):
        return self.isElementDisplayed(self.PageHeader)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def select_Status(self, status):
        self.selectDropdownValueByText(self.ShowStatus_dropdown, status)

    def close_popup(self):
        self.clickToElementByJavaScriptExecutor(self.CloseBtn)

    def click_AddNew(self):
        self.clickToElement(self.AddNewBtn)

    def validateRulesStatus(self, status):
        flag = bool(True)
        elementList = list((self.driver.find_elements(By.XPATH, '//tr/td[7]')))
        try:
            for element in elementList:
                print(element.text)
                if element.text != status:
                    flag = bool(False)
                    break
            return flag
        except:
         print("Either Element not found")
         return flag

    def addRule(self, tid):
        self.clickToElement(self.AddNewBtn)
        time.sleep(5)
        self.isElementDisplayed(self.AddModalTitle)
        self.enterValueToTextbox(self.RuleId, tid)
        time.sleep(5)
        self.clickToElement(self.AddBtn)

    def select_record_byindex(self, row):
        Checkbox_rowRecord = (By.XPATH, "(//input[@type='checkbox'])["+str(row+1)+"]")
        self.clickToElementByJavaScriptExecutor(Checkbox_rowRecord)

    def check_BulkDeleteButton_disabled(self):
        return self.isElementDisabled(self.BulkDeleteBtn)

    def click_RefreshButton(self):
        self.clickToElement(self.RefreshBtn)

    def check_BulkDeleteButton_enabled(self):
        flag = self.isElementDisabled(self.BulkDeleteBtn)
        if flag:
            flag = bool(False)
        else:
            flag = bool(True)
        return flag

    def bulk_delete(self):
        self.clickToElementByJavaScriptExecutor(self.BulkDeleteBtn)
        if self.validate_popupMessage("Are you sure you want to delete the selected records"):
             self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
             print("Selected Job sites deleted by Bulk Delete action")
        else:
            print("JobSite deleted alert not present")




    def add_multiple_tasks(self, file_path):
        self.clickToElement(self.AddNewBtn)
        time.sleep(5)
        self.isElementDisplayed(self.AddModalTitle)
        self.clickToElementByJavaScriptExecutor(self.MultipleTab)
        # self.enterValueToTextbox(self.uploadBox, filePath)
        element = self.driver.find_element(By.XPATH, "//input[@type='file']")
        element.send_keys(file_path)
        time.sleep(5)
        self.clickToElement(self.AddBtn)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)
        return flag

    def validate_ErrorAlertMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.ErrorFloatingMSG)
        if value in actual:
            flag = bool(True)
        return flag

    def deleteRuleById(self, mid):
        self.clickToElementByJavaScriptExecutor(self.FilterIdBox)
        self.enterValueToTextbox(self.FilterIdBox, mid)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)

    def validate_popupMessage(self, msg):
        element_locator = (By.XPATH, "//div[@class='msgContent']/div[contains(.,'"+msg+"')]")
        return self.isElementDisplayed(element_locator)

    def deleteRuleByName(self, name):
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)

    def confirm_DeleteAction(self):
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Rule has been deleted")

    def cancel_deleteAction(self):
        self.clickToElementByJavaScriptExecutor(self.CancelBtn)
        print("Rule deletion has been canceled")

    def click_edit_for_RuleName(self, name):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.EditIcon)

    def click_View_for_RuleName(self, name):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.ViewIcon)

    def validate_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'"+tabName+"')])[1]")
        return self.isElementDisplayed(element_locator)

    def click_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)

    def validate_Table_columnsName(self, name):
        element_locator = (By.XPATH, "//span[contains(@class,'k-column-title')][text()='"+name+"']")
        return self.isElementDisplayed(element_locator)

    def check_ActionLink_disabled(self, action_link, name):
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(2)
        flag = bool(False)
        element_locator = (By.XPATH, "(//img[contains(@src,'"+action_link+"')]/parent::li)[1]")
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




