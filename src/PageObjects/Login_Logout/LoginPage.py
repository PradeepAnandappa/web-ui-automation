import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class LoginPage(BasePage):
    AccountID = (By.ID, "account_id")
    UserName = (By.ID, "user_name")
    UserEmail =(By.ID, "email")
    Password = (By.ID, "password")
    LoginBtn = (By.XPATH, "//button[contains(.,'LOGIN')]")
    RememberMe_checkbox = (By.XPATH, "//label[contains(.,'Remember me')]")
    ErrorMsg = (By.XPATH, "//div[@class='floatingMessage msgError']")
    TrialAccountLink = (By.XPATH, "//a[contains(.,'Start your free trial')]")
    LoginWithEmail = (By.XPATH, "//button[contains(@class, 'emailID')]")

    def __init__(self, driver):
        super().__init__(driver)
        url = self.driver.current_url
        #self.driver.get(url+"ngui/login")
        #self.driver.get(url + "login")
        self.driver.maximize_window()

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def user_login(self, account_id, user_name, password):
        self.enterValueToTextbox(self.AccountID, account_id)
        self.enterValueToTextbox(self.UserName, user_name)
        self.enterValueToTextbox(self.Password, password)
        self.clickToElement(self.LoginBtn)

    def user_loginByEmail(self, user_email, password):
        self.clickToElement(self.LoginWithEmail)
        time.sleep(2)
        self.enterValueToTextbox(self.UserEmail, user_email)
        self.enterValueToTextbox(self.Password, password)
        self.clickToElement(self.LoginBtn)

    def is_ErrorAlertPresent(self):
        flag =self.isElementDisplayed(self.ErrorMsg)
        return flag

    def tick_RememberMe(self):
        self.clickToElement(self.RememberMe_checkbox)

    def getAccountValue(self):
        return self.getElementValue(self.AccountID)

    def getUserNameValue(self):
        return self.getElementValue(self.UserName)

    def click_TrailAccountLink(self):
        self.clickToElement(self.TrialAccountLink)





