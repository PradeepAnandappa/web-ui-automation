import math
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class EmployeesPage(BasePage):
    AddNewBtn = (By.XPATH, "//button[contains(.,'Add New')]")
    AddEmployeeModalTitle = (By.XPATH, "//div[contains(.,'Add New Employee')][@class='popupHeading']")
    EmpName = (By.NAME, "employeeName")
    EmpNumber = (By.NAME, "phoneNumber")
    TermsCheckbox = (By.XPATH, "//label[contains(.,'Accept service terms')]")
    DownLoadLinkCheckbox = (By.XPATH, "//label[contains(.,'send App download link')]")
    AddBtn = (By.XPATH, "//button[contains(.,'Add')][contains(@class,'okBtn')]")
    FilterNumberBox = (By.XPATH, "(//input[@aria-label='Filter'])[1]")
    FilterNameBox = (By.XPATH, "(//input[@aria-label='Filter'])[3]")
    DeleteIcon = (By.XPATH, "(//img[contains(@src,'delete')])[1]")
    ConfirmBtn = (By.XPATH, "//button[contains(.,'Yes')]")
    EditIcon = (By.XPATH, "(//img[contains(@src,'edit')])[1]")
    ViewIcon = (By.XPATH, "(//img[contains(@src,'view')])[1]")
    MultipleTab = (By.XPATH, "//li[text()='Multiple']")
    uploadBox = (By.XPATH, "//input[@type='file']")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    ErrorFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgError")
    CloseMsg = (By.XPATH, "//div[@class='closeMessage']")
    ClosePopup = (By.XPATH, "//div[@class='closePopup']")
    ExportBtn = (By.XPATH, "//button[contains(.,'Export to Excel')]")
    UserInfo = (By.XPATH, "//div/div[contains(@class,'userinfo') or contains(@class,'userInfo')]/span")
    ChildAccount = (By.XPATH, "(//li/a[contains(@class,'userChild')])[1]")
    Logout = (By.XPATH, "//a[contains(@class,'iconLogout')]")
    EmployeeCSVDownloadLink = (By.XPATH, "//a[@download='employee-sample']")

    BulkDeleteBtn = (By.XPATH, "(//button[contains(.,'Bulk Delete')])[1]")
    CopyIcon = (By.XPATH, "(//li/img[contains(@src,'copy')])[1]")
    ShowStatus_dropdown = (By.XPATH, "(//span[contains(.,'Show Status')]/following-sibling::select)[1]")
    RefreshBtn = (By.XPATH, "(//button[contains(.,'Refresh')])[1]")
    SearchBox = (By.XPATH, "//div[@class='searchFld']/input")
    ThreeDotIcon = (By.XPATH, "(//span[contains(@class,'more-vertical')])[1]")
    SaveBtn = (By.XPATH, "(//button[contains(.,'SAVE')])[1]")
    ResetBtn = (By.XPATH, "(//button[contains(.,'Reset')])[1]")
    PagerDropDown = (By.XPATH, "//span[contains(@class,'pager')]/span")
    SaveChangesBtn = (By.XPATH, "(//button[contains(.,'Save Changes')])[1]")
    CancelChangesBtn = (By.XPATH, "(//button[contains(.,'Cancel Changes')])[1]")
    PaginationLabel = (By.XPATH, "//div[contains(@class,'pager-info')]")




    # Kindo table details


    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def validate_page_title(self):
        return self.getPageTitle("Employee")


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

    def select_pagination_items_per_page(self, option):
        self.clickToElementByJavaScriptExecutor(self.PagerDropDown)
        element_locator = (By.XPATH, "//span[@class='k-list-item-text'][contains(.,'"+option+"')]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def validate_pagination_items_per_page(self, option):
        self.clickToElementByJavaScriptExecutor(self.PagerDropDown)
        element_locator = (By.XPATH, "//span[@class='k-list-item-text'][contains(.,'"+option+"')]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        per_page = int(option)
        paginationLabel = self.getElementText(self.PaginationLabel)

        # initializing substrings
        sub1 = "of"
        sub2 = "items"

        # getting elements in between using split() and join()
        res = ''.join(paginationLabel.split(sub1)[1].split(sub2)[0])

        # printing result
        print("The extracted item count : " + res)
        count = int(res)
        pages = count / per_page
        pagecount = math.ceil(pages)
        print("page counts : " + str(pagecount))
        i = 0
        flag = True
        while True:
            elements = self.driver.find_elements(By.XPATH, "//table[@class='k-grid-table']//tr")
            num_elements = len(elements)
            if 0 < num_elements <= per_page:
                print("Records counts on page - "+str(i+1)+" :" + str(num_elements))
            else:
                flag = False
            i += 1
            if i >= pagecount:
                break
            element_locator = (By.XPATH, "//a[@title='Go to the next page']")
            self.clickToElementByJavaScriptExecutor(element_locator)
            time.sleep(2)
        return flag





    def populate_addEmployeeForm(self, name, number):
        self.isElementDisplayed(self.AddEmployeeModalTitle)
        self.enterValueToTextbox(self.EmpName, name)
        self.enterValueToTextbox(self.EmpNumber, number)

    def accept_termCheckbox(self):
        self.scrollIntoViewElement(self.TermsCheckbox)
        self.clickToElementByJavaScriptExecutor(self.TermsCheckbox)
        self.clickToElementByJavaScriptExecutor(self.DownLoadLinkCheckbox)

    def click_Add(self):
        self.clickToElement(self.AddBtn)
        time.sleep(2)
        #if self.isElementDisplayed(self.ConfirmBtn):
           # self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)

    def click_Addnew(self):
        self.clickToElement(self.AddNewBtn)

    def click_closeMSG(self):
        self.clickToElementByJavaScriptExecutor(self.CloseMsg)

    def click_closeModal(self):
        self.clickToElementByJavaScriptExecutor(self.ClosePopup)

    def searchEmployeeByNumber(self, number):
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
        time.sleep(2)

    def searchEmployeeByName(self, name):
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(2)

    def click_refresh(self):
        self.clickToElement(self.RefreshBtn)

    def deleteEmployee(self, number):
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        self.clickToElement(self.ConfirmBtn)
        print("Employee deleted with number -", number)

    def deleteEmployeeByName(self, name):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterNameBox)
        self.enterValueToTextbox(self.FilterNameBox, name)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.DeleteIcon)
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Employee deleted with name -", name)

    def confirm_Delete(self):
        self.clickToElementByJavaScriptExecutor(self.ConfirmBtn)
        print("Selected Employees has been deleted")

    def click_edit_for_employee(self, number):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
        time.sleep(5)
        self.clickToElementByJavaScriptExecutor(self.EditIcon)

    def click_view_for_employee(self, number):
        time.sleep(10)
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
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

    def uploadCSVFile(self, file_path):
        element = self.driver.find_element(By.XPATH, "//input[@type='file']")
        element.send_keys(file_path)
        time.sleep(5)

    def click_MutipleTab(self):
        self.isElementDisplayed(self.AddEmployeeModalTitle)
        self.clickToElementByJavaScriptExecutor(self.MultipleTab)

    def click_DownloadEmployeeData(self):
        self.clickToElement(self.EmployeeCSVDownloadLink)

    def getColorOfAddButton(self):
        return self.get_CSSAttributeValue(self.AddBtn, 'background-color')

    def validate_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'"+tabName+"')])[1]")
        return self.isElementDisplayed(element_locator)

    def click_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)

    def isAvailable_leftPanelOption(self, tabName ):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        return self.isElementDisplayed(element_locator)

    def validate_Table_columnsName(self, name):
        element_locator = (By.XPATH, "//span[contains(@class,'k-column-title')][text()='"+name+"']")
        return self.isElementDisplayed(element_locator)

    def check_AddButton_disabled(self):
        return self.isElementDisabled(self.AddBtn)

    def check_ActionLink_disabled(self, action_link, number):
        self.clickToElementByJavaScriptExecutor(self.FilterNumberBox)
        self.enterValueToTextbox(self.FilterNumberBox, number)
        time.sleep(2)
        flag = bool(False)
        element_locator = (By.XPATH, "(//img[contains(@src,'" + action_link + "')]/parent::div/parent::li)[1]")
        attr_value = self.get_AttributeValue(element_locator, "class")
        if attr_value == "disabled":
            flag = bool(True)
        return flag

    def logout_user(self):
        self.clickOnElementByActionClass(self.UserInfo)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.Logout)
        time.sleep(5)


    def check_ActionLink_enabled(self, action_link, name):
        flag = self.check_ActionLink_disabled(action_link, name)
        if flag:
            flag = bool(False)
        else:
            flag = bool(True)
        return flag

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

    def apply_sorting_on_Column(self, colNo):
        element_locator = (By.XPATH, "(//span[contains(@class,'column-title')])["+str(colNo+1)+"]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def click_ExportToExcel(self):
        self.clickToElementByJavaScriptExecutor(self.ExportBtn)

    def dragAndDrop_columns(self, col1, col2):
        element_source = self.driver.find_element("xpath", "(//span[contains(@class,'k-column-title')])[" + str(col1 + 1) + "]")
        element_target = self.driver.find_element("xpath", "(//span[contains(@class,'k-column-title')])[" + str(col2 + 1) + "]")
        action = ActionChains(self.driver)
        action.drag_and_drop(element_source, element_target).perform()
        time.sleep(2)
        return element_target.text

    def select_ThreeDotMenuColumnsOption(self, option):
        self.clickToElementByJavaScriptExecutor(self.ThreeDotIcon)
        time.sleep(2)
        element_locator = (By.XPATH, "//div[@class='k-columnmenu-item '][contains(.,'Columns')]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        time.sleep(2)
        element_locator = (By.XPATH, "//label[contains(.,'"+option+"')]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        self.clickToElementByJavaScriptExecutor(self.SaveBtn)

    def reset_ThreeDotSelection(self):
        self.clickToElementByJavaScriptExecutor(self.ThreeDotIcon)
        time.sleep(2)
        element_locator = (By.XPATH, "//div[@class='k-columnmenu-item '][contains(.,'Columns')]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.ResetBtn)

    def global_Search(self, str):
        self.enterValueToTextbox(self.SearchBox, str)

    def validate_SearchResult(self, str):
        element_locator = (By.XPATH, "(//td[contains(.,'"+str+"')])[1]")
        return self.isElementDisplayed(element_locator)

    def edit_KendoDetail(self, oldValue, newValue):
        element_locator = (By.XPATH, "(//td[contains(.,'" + oldValue + "')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)
        time.sleep(1)
        element_locator = (By.XPATH, "(//input[contains(@value,'" + oldValue + "')])[1]")
        self.enterValueToTextbox(element_locator, newValue)
        time.sleep(1)
        self.clickToElementByJavaScriptExecutor(self.SearchBox)
        time.sleep(1)
        self.clickToElement(self.SaveChangesBtn)


















