import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class UploadHubPage(BasePage):
    ExportBtn = (By.XPATH, "//button[contains(.,'Export to Excel')]")
    PageHeader = (By.XPATH, "//h3[contains(.,'Upload a File')]")
    EmployeeCSVDownloadLink = (By.XPATH, "//a[@download='employee-phone-numbers']")
    EVVEmployeeCSVDownloadLink = (By.XPATH, "//a[@download='evv_employee-profile']")

    JobsiteCSVDownloadLink = (By.XPATH, "//a[@download='job-template']")
    EVVJobsiteCSVDownloadLink = (By.XPATH, "//a[@download='evv_clients_upload']")
    TaskCSVDownloadLink = (By.XPATH, "//a[@download='task_details']")
    EarningCodeCSVDownloadLink = (By.XPATH, "//a[@download='earning_codes']")
    CencelButton = (By.XPATH, "//a[contains(.,'Cancel')]")
    uploadBox = (By.XPATH, "//input[@type='file']")
    SuccessFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgSuccess")
    ErrorFloatingMSG = (By.CSS_SELECTOR, "div.floatingMessage.msgError")
    PopupMSG = (By.XPATH, "//div[@class='msgContent']")
    UploadBtn = (By.XPATH, "//button[contains(.,'Upload')]")
    FileTypeError = (By.XPATH, "//div[@class='errMsg'][contains(.,'File type unsupported.')]")
    UnMatchedColumnPopupHeader = (By.XPATH, "//label[contains(.,'The CSV upload has unmatched columns. Match them below:')]")
    UnMatchedColumn = (By.XPATH, "//tr[contains(.,'Unmatched Columns')]/following-sibling::tr[contains(.,'EmployeeName')]")
    # Kindo table details


    def __init__(self, driver):
        super().__init__(driver)

    def click_Company(self):
        self.clickToElement(self.CompanyLink)

    def click_ExportToExcel(self):
        self.clickToElementByJavaScriptExecutor(self.ExportBtn)

    def validate_PageHeader(self):
        return self.isElementDisplayed(self.PageHeader)

    def validate_FileTypeErrorMessage(self):
        return self.isElementDisplayed(self.FileTypeError)

    def select_CategoryofFileUpload(self, str):
        element_locator = (By.XPATH, "//label[contains(.,'"+str+"')]")
        self.clickToElementByJavaScriptExecutor(element_locator)

    def click_DownloadEmployeeData(self):
        self.clickToElementByJavaScriptExecutor(self.EmployeeCSVDownloadLink)

    def click_DownloadEVVEmployeeData(self):
        self.clickToElementByJavaScriptExecutor(self.EVVEmployeeCSVDownloadLink)

    def click_DownloadJobsiteData(self):
        self.clickToElementByJavaScriptExecutor(self.JobsiteCSVDownloadLink)

    def click_DownloadEVVJobsiteData(self):
        self.clickToElementByJavaScriptExecutor(self.EVVJobsiteCSVDownloadLink)

    def click_DownloadTaskData(self):
        self.clickToElementByJavaScriptExecutor(self.TaskCSVDownloadLink)

    def click_DownloadEarningCodeData(self):
        self.clickToElementByJavaScriptExecutor(self.EarningCodeCSVDownloadLink)

    def uploadCSVFile(self, filePath):
        element = self.driver.find_element(By.XPATH, "//input[@type='file']")
        element.send_keys(filePath)

    def click_company_icon(self, tabName):
        element_locator = (By.XPATH, "(//ul/li/a[contains(.,'" + tabName + "')])[1]")
        self.clickToElement(element_locator)

    def click_Upload(self):
        self.clickToElement(self.UploadBtn)

    def validate_SuccessUpdateMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.SuccessFloatingMSG)
        if value in actual:
            flag = bool(True)

        return flag

    def validate_ErrorMessage(self, value):
        flag = bool(False)
        actual = self.getElementText(self.PopupMSG)
        print(actual)
        if value in actual:
            flag = bool(True)

        return flag

    def click_Cancel(self):
        self.clickToElement(self.CencelButton)

    def validate_UnmatchedColumnPopupheader(self):
        return self.isElementDisplayed(self.UnMatchedColumnPopupHeader)

    def validate_UnmatchedColumn(self, attribute):
        element_locator = (By.XPATH, "//tr[contains(.,'Unmatched Columns')]/following-sibling::tr[contains(.,'"+attribute+"')]")
        return self.isElementDisplayed(element_locator)







