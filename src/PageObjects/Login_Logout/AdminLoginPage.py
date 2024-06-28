from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class AdminLoginPage(BasePage):
    AccountID = (By.ID, "supportReqAccountId")
    UserEmail = (By.XPATH, "//input[@type='email']")
    Password = (By.XPATH, "//input[@type='password']")
    NextBtn = (By.XPATH, "//button[contains(.,'Next')]")
    LoginBtn = (By.XPATH, "//button[contains(.,'Login with Google')]")
    ErrorMsg = (By.XPATH, "//div[@class='floatingMessage msgError']")

    def __init__(self, driver):
        super().__init__(driver)
        url = self.driver.current_url
        self.driver.get(url + "admin-login")

    def get_page_title(self, title):
        return self.getPageTitle(title)

    def validateComponents(self):
        self.isElementDisplayed(self.AccountID)
        self.isElementDisplayed(self.LoginBtn)

    def admin_login(self, account_id, user_name, password):
        self.enterValueToTextbox(self.AccountID, account_id)
        self.clickToElement(self.LoginBtn)
        self.switchToWindow()
        self.enterValueToTextbox(self.UserEmail, user_name)
        self.clickToElement(self.NextBtn)
        self.enterValueToTextbox(self.Password, password)
        self.clickToElement(self.NextBtn)