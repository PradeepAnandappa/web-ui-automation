import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class MonitorPage(BasePage):
    TrackingSchedularTab = (By.XPATH, "//a[contains(.,'Tracking Scheduler')]")
    UserInfo = (By.XPATH, "//div/div[contains(@class,'userinfo') or contains(@class,'userInfo')]/span")
    ChildAccount = (By.XPATH, "(//li/a[contains(@class,'userChild') or contains(@id,'child')])[1]")
    Logout = (By.XPATH, "//a[contains(@class,'iconLogout')]")
    threeDot_menu_firstColumnHeader = (By.XPATH, "(//div[contains(@class, 'k-grid-header-menu')])[1]")
    Filter_Columns_option = (By.XPATH, "(//div[contains(., 'Columns')][@class='k-columnmenu-item '])[1]")


    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def logout_user(self):
        self.clickToElement(self.UserInfo)
        time.sleep(5)
        self.clickToElement(self.Logout)
        time.sleep(5)

    def validate_parent_child_tree_under_user_profile(self):
        self.clickToElement(self.UserInfo)
        time.sleep(2)
        return self.isElementDisplayed(self.ChildAccount)

    def switch_to_ChildAccount(self):
        self.clickOnElementByActionClass(self.UserInfo)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.ChildAccount)

    def click_TrackingSchedularTab(self):
        time.sleep(5)
        self.clickToElement(self.TrackingSchedularTab)
        time.sleep(30)

    def logout_user(self):
        self.clickOnElementByActionClass(self.UserInfo)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.Logout)
        time.sleep(5)

    def validate_Table_columnsName(self, name):
        element_locator = (By.XPATH, "//span[contains(@class,'k-column-title')][contains(.,'"+name+"')]")
        return self.isElementDisplayed(element_locator)


    def validate_columnName_under_filter(self, name):
        self.clickToElementByJavaScriptExecutor(self.threeDot_menu_firstColumnHeader)
        self.clickToElementByJavaScriptExecutor(self.Filter_Columns_option)
        time.sleep(1)
        element_locator = (By.XPATH, "//label[contains(., '"+name+"')][@class='k-checkbox-label']")
        return self.isElementDisplayed(element_locator)


