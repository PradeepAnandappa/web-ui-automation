import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class FormsPage(BasePage):
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    AddModalTitle = (By.XPATH, "//div[contains(.,'Add New Form')][@class='popupHeading']")
    FormName = (By.NAME, "formName")
    TaskId = (By.XPATH, "//label[contains(.,'Task ID')]/following-sibling::input")
    AddBtn = (By.XPATH, "//button[contains(.,'Add')][contains(@class,'okBtn')]")
    FilterNameBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    FilterAddressBox = (By.XPATH, "(//input[@aria-label='Filter'])[2]")
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

    # Kindo table details


    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def select_Status(self, status):
        self.selectDropdownValueByText(self.ShowStatus_dropdown, status)

    def validateScheduleStatus(self, status):
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

    def click_Add(self):
        self.clickToElement(self.AddBtn)
        ##if self.isElementDisplayed(self.ConfirmBtn):
          ##  time.sleep(2)
          ##  self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)

    def click_Addnew(self):
        self.clickToElement(self.AddNewBtn)

    def click_closeMSG(self):
        self.clickToElementByJavaScriptExecutor(self.CloseMsg)

    def click_closeModal(self):
        self.clickToElementByJavaScriptExecutor(self.ClosePopup)

    def enterFormName(self, name):
        self.isElementDisplayed(self.AddModalTitle)
        self.enterValueToTextbox(self.FormName, name)

    def uploadHTML(self, file_path):
        element = self.driver.find_element(By.XPATH, "//input[@type='file']")
        element.send_keys(file_path)


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

    def deleteTaskById(self, mid):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterManagerIdBox)
        self.enterValueToTextbox(self.FilterManagerIdBox, mid)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        self.clickToElement(self.ConfirmBtn)
        print("Manager deleted with number -", mid)

    def validate_popupMessage(self, msg):
        element_locator = (By.XPATH, "//div[@class='msgContent']/div[contains(.,'"+msg+"')]")
        return self.isElementDisplayed(element_locator)

    def deleteFormByName(self, name):
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)

    def confirm_DeleteAction(self):
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Selected Form has been deleted")

    def cancel_deleteAction(self):
        self.clickToElementByJavaScriptExecutor(self.CancelBtn)

    def click_edit_for_TaskName(self, name):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.EditIcon)

    def click_View_for_TaskName(self, name):
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

    def check_AddButton_disabled(self):
        return self.isElementDisabled(self.AddBtn)

    def check_AddButton_enabled(self):
        flag = self.isElementDisabled(self.AddBtn)
        if flag:
            flag = bool(False)
        else:
            flag = bool(True)
        return flag

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)

        return flag

    def validate_ErrorMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.ErrorFloatingMSG)
        print(actual)
        if value in actual:
            flag = bool(True)

        return flag




