import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class LoginPage(BasePage):
    AccountID = (By.ID, "account")
    UserName = (By.ID, "user")
    Password = (By.ID, "accountpassword")
    LoginBtn = (By.ID, "login_btn1")
    UserEmail = (By.ID, "userEmail")
    EmailPassword = (By.ID, "Emailpassword")
    LoginBtn2 = (By.ID, "login_btn")
    RememberMe_checkbox = (By.XPATH, "//label[contains(.,'Remember me')]")
    ErrorMsg = (By.XPATH, "//div[@class='floatingMessage msgError']")
    CookieConsentBtn =(By.XPATH, "//button[@title='Accept All Cookies']")

    def __init__(self, driver):
        super().__init__(driver)
        url = self.driver.current_url
        self.driver.get(url + "login")

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def user_login(self, account_id, user_name, password):
        time.sleep(2)
        if self.isElementDisplayed(self.CookieConsentBtn):
            self.clickToElementByJavaScriptExecutor(self.CookieConsentBtn)
        time.sleep(2)
        self.enterValueToTextbox(self.AccountID, account_id)
        self.enterValueToTextbox(self.UserName, user_name)
        self.enterValueToTextbox(self.Password, password)
        self.clickToElement(self.LoginBtn)

    def user_loginByEmail(self, user_email, password):
        time.sleep(5)
        if self.isElementDisplayed(self.CookieConsentBtn):
            self.clickToElementByJavaScriptExecutor(self.CookieConsentBtn)
        time.sleep(2)
        self.enterValueToTextbox(self.UserEmail, user_email)
        self.enterValueToTextbox(self.EmailPassword, password)
        self.clickToElement(self.LoginBtn2)

    def is_ErrorAlertPresent(self):
        flag =self.isElementDisplayed(self.ErrorMsg)
        return flag

    def tick_RememberMe(self):
        self.clickToElement(self.RememberMe_checkbox)

    def getAccountValue(self):
        return self.getElementValue(self.AccountID)

    def getUserNameValue(self):
        return self.getElementValue(self.UserName)

    def acceptCookieContent(self):
        if self.isElementDisplayed(self.CookieConsentBtn):
            self.clickToElement(self.CookieConsentBtn)






