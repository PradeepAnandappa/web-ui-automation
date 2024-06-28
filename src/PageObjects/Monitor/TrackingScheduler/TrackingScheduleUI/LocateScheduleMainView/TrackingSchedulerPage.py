import os
import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class TrackingSchedulerPage(BasePage):
    UserInfo = (By.XPATH, "//div[@class='topheader']/div[contains(@class,'userinfo2')]")
    Logout = (By.XPATH, "//a[contains(@class,'account_logout')]")
    ChildAccount = (By.XPATH, "(//span[@class='childacc'])[1]")
    TrackingSchedularTab = (By.ID, "monitor_locate_tab")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    ErrorFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgError")
    AddNewBtn = (By.XPATH, "(//button[contains(.,'Add New')])[1]")
    BulkDeleteBtn = (By.XPATH, "(//button[contains(.,'Bulk Delete')])[1]")
    AddSchedulerModalTitle = (By.XPATH, "//div[contains(.,'Add New Tracking Scheduler')][@class='popupHeading']")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    DeleteIcon = (By.XPATH, "(//img[contains(@src,'delete')])[1]")
    EditIcon = (By.XPATH, "(//img[contains(@src,'edit')])[1]")
    ViewIcon = (By.XPATH, "(//img[contains(@src,'view')])[1]")
    CopyIcon = (By.XPATH, "(//img[contains(@src,'copy')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    CancelBtn = (By.XPATH, "//a[contains(.,'Cancel')]")
    ShowStatus_dropdown = (By.XPATH, "(//span[contains(.,'Show Status')]/following-sibling::select)[1]")
    RefreshBtn = (By.XPATH, "(//button[contains(.,'Refresh')])[1]")
    UserInfo = (By.XPATH, "//div/span[contains(@class,'userAvatar')]")
    Logout = (By.XPATH, "//a[contains(@class,'Logout')]")
    ExportBtn = (By.XPATH, "//button[contains(.,'Export to Excel')]")
    SearchBox = (By.XPATH, "//div[@class='searchFld']/input")



    def __init__(self, driver):
        super().__init__(driver)

    def click_AddNew(self):
        self.clickToElementByJavaScriptExecutor(self.AddNewBtn)

    def click_ExportToExcel(self):
        self.clickToElementByJavaScriptExecutor(self.ExportBtn)

    def validate_AddNewTrackingScheduleModal(self):
        return self.isElementDisplayed(self.AddSchedulerModalTitle)

    def check_BulkDeleteButton_disabled(self):
        return self.isElementDisabled(self.BulkDeleteBtn)

    def check_BulkDeleteButton_enabled(self):
        flag = self.isElementDisabled(self.BulkDeleteBtn)
        if flag:
            flag = bool(False)
        else:
            flag = bool(True)
        return flag

    def select_record_byindex(self, row):
        Checkbox_rowRecord = (By.XPATH, "(//input[@type='checkbox'])["+str(row+1)+"]")
        self.clickToElementByJavaScriptExecutor(Checkbox_rowRecord)

    def click_BulkDelete(self):
        self.clickToElement(self.BulkDeleteBtn)

    def click_CancelAction(self):
        self.clickToElementByJavaScriptExecutor(self.CancelBtn)

    def edit_schedule(self, scheduleId):
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, scheduleId)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.EditIcon)

    def copy_schedule(self, scheduleId):
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, scheduleId)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.CopyIcon)

    def delete_schedule(self, name):
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)

    def confirm_DeleteAction(self):
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Schedule has been deleted")

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

    def click_RefreshButton(self):
        self.clickToElement(self.RefreshBtn)

    def click_view_icon_for_schedule(self, name):
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, name)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.ViewIcon)


    def check_ActionLink_disabled(self, action_link, name):
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, name)
        time.sleep(2)
        flag = bool(False)
        element_locator = (By.XPATH, "(//img[contains(@src,'" + action_link + "')]/parent::div/parent::li)[1]")
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

    def deleteFile(self, filepath):
        flag = bool(False)
        file_path = filepath
        if os.path.isfile(file_path):
            os.remove(file_path)
            flag = bool(True)
            print("File has been deleted")
        else:
            print("File does not exist")
        return flag

    def validate_SearchRecord(self, str):
        self.enterValueToTextbox(self.SearchBox, str)
        time.sleep(2)
        element_locator = (By.XPATH, "(//td[contains(.,'"+str+"')])[1]")
        return self.isElementDisabled(element_locator)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)
        return flag




