import time

from selenium.webdriver.common.by import By

from Configuration.config import config
from src.PageObjects.BasePage.BasePage import BasePage


class SignupPage(BasePage):
    FirstName = (By.ID, "firstName")
    Company = (By.ID, "company")
    PhoneNumber = (By.ID, "phoneNumber")
    Email = (By.ID, "email")
    StartTrailBtn = (By.ID, "startMyTrial")
    RememberMe_checkbox = (By.XPATH, "//label[contains(.,'Remember me')]")
    ErrorMsg = (By.XPATH, "//div[@class='floatingMessage msgError']")
    TrialAccountLink = (By.XPATH, "//a[contains(.,'Start your free trial')]")
    DismissBtn = (By.XPATH, "//div[@aria-label='Dismiss']")
    ChatPanel = (By.XPATH, "//div[contains(@class,'intercom-block')]")
    TimezoneDropdown = (By.XPATH, "//select[@name='a_tmz']")
    flagSelectArrow = (By.XPATH, "//div[@aria-label='Dismiss']")

    def __init__(self, driver):
        super().__init__(driver)

    def signup_user(self, fname, comp, number, email, timezone):
        self.enterValueToTextbox(self.FirstName, fname)
        self.enterValueToTextbox(self.Company, comp)
        self.enterValueToTextbox(self.PhoneNumber, number)
        self.enterValueToTextbox(self.Email, email)
        self.selectDropdownValueByText(self.TimezoneDropdown, timezone)
        time.sleep(2)
        self.clickToElementByJavaScriptExecutor(self.StartTrailBtn)

    def get_ValidationAlertText(self):
        flag = bool(False)
        alert_text = self.get_alertText()
        return alert_text



    def close_chatpanel(self):
        self.mouseHoverOnElement(self.ChatPanel)
        self.clickToElementByJavaScriptExecutor(self.DismissBtn)

