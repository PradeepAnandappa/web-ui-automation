import time

from selenium.webdriver.common.by import By

from src.PageObjects.BasePage.BasePage import BasePage


class AddEditTrackingSchedulePage(BasePage):
    AddSchedulerModalTitle = (By.XPATH, "//div[contains(.,'Add New Tracking Scheduler')][@class='popupHeading']")
    EditSchedulerModalTitle = (By.XPATH, "//div[contains(.,'Edit Tracking Scheduler')][@class='popupHeading']")
    StatusToggle = (By.XPATH, "//input[@id='StatusActive']/following-sibling::label")
    ScheduleID =(By.NAME, "scheduleId")
    SaveBtn = (By.XPATH, "//button[contains(.,'SAVE')]")
    DoneBtn = (By.XPATH, "//button[contains(.,'Done')]")
    TrackFrequency = (By.XPATH, "//input[@name='frequency']")
    RepeatDropdown = (By.XPATH, "//select[@name='repeat']")
    TrackStartInputbox = (By.XPATH, "(//label[contains(.,'Track from')]/following-sibling::div/div/span/input)[1]")
    EndDateInputbox = (By.XPATH, "(//label[contains(.,'Ends')]/following-sibling::div/span/span/input)[1]")
    StartDateInputbox = (By.XPATH, "(//label[contains(.,'Start Date')]/following-sibling::div/span/span/input)[1]")
    Reccuring_checkbox = (By.XPATH, "(//input[@id='Recurring']/following-sibling::label)[1]")
    Employee_radioBtn = (By.XPATH, "(//input[@id='Employee']/following-sibling::label)[1]")
    Manual_radioBtn = (By.XPATH, "(//input[@id='Manual']/following-sibling::label)[1]")
    Continuously_radioBtn = (By.XPATH, "(//input[@id='Continuously']/following-sibling::label)[1]")
    TimeZone_dropdown = (By.NAME, "timezone")
    HelpIcon = (By.XPATH, "//span[@class='helpTip']")
    Tooltip = (By.XPATH, "//div[@class='k-tooltip-content']")
    Employee_Group_dropdown = (By.XPATH, "(//label[contains(.,'Select')]/following-sibling::select)[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_AddNewTrackingScheduleModal(self):
        return self.isElementDisplayed(self.AddSchedulerModalTitle)

    def validate_EditTrackingScheduleModal(self):
        return self.isElementDisplayed(self.EditSchedulerModalTitle)

    def editTrackingScheduleStatus(self):
        self.clickToElementByJavaScriptExecutor(self.StatusToggle)
        self.clickToElement(self.SaveBtn)
        time.sleep(3)

    def addTrackingSchedule(self, sid):
        self.enterValueToTextbox(self.ScheduleID, sid)
        self.clickToElement(self.DoneBtn)
        time.sleep(3)

    def enter_ScheduleName(self, sid):
        self.enterValueToTextbox(self.ScheduleID, sid)

    def get_StartDate(self):
        return self.getElementValue(self.StartDateInputbox)

    def set_StartDate(self, value):
        self.enterValueToTextboxByJavascriptExecutor(self.StartDateInputbox, value)

    def get_EndDate(self):
        return self.getElementValue(self.EndDateInputbox)

    def set_EndDate(self, value):
        self.enterValueToTextboxByJavascriptExecutor(self.EndDateInputbox, value)

    def get_TrackFrom(self):
        return self.getElementValue(self.TrackStartInputbox)

    def get_TrackFrequency(self):
        return self.getElementValue(self.TrackFrequency)

    def set_TrackFrequency(self, value):
        return self.enterValueToTextbox(self.TrackFrequency, value)

    def get_timeZone(self):
        return self.get_selectedValueinDropdown(self.TimeZone_dropdown)

    def set_timeZone(self, value):
        self.selectDropdownValueByText(self.TimeZone_dropdown, value)

    def click_Status_toggle(self):
        self.clickToElementByJavaScriptExecutor(self.StatusToggle)

    def click_Done(self):
        self.clickToElement(self.DoneBtn)


    def click_Save(self):
        self.clickToElement(self.SaveBtn)


    def select_Employee(self):
        self.clickToElementByJavaScriptExecutor(self.Employee_radioBtn)

    def select_Manual(self):
        self.clickToElementByJavaScriptExecutor(self.Manual_radioBtn)

    def select_Continuously(self):
        self.clickToElementByJavaScriptExecutor(self.Continuously_radioBtn)

    def select_ReccuringSchedule(self):
        self.clickToElementByJavaScriptExecutor(self.Reccuring_checkbox)

    def select_Group(self, groupName):
        self.selectDropdownValueByText(self.Employee_Group_dropdown, groupName)

    def get_Help_tooltip(self):
        self.mouseHoverOnElement(self.HelpIcon)
        return self.getElementText(self.Tooltip)

    def set_repeat(self, option):
        self.scrollIntoViewElement(self.RepeatDropdown)
        self.selectDropdownValueByText(self.RepeatDropdown, option)

    def select_weekly_day(self, day):
        element_locator = (By.XPATH, "(//span[contains(@value,'"+day+"')])[1]")
        self.clickToElementByJavaScriptExecutor(element_locator)


    def get_repeat_selected_value(self):
        return self.get_selectedValueinDropdown(self.RepeatDropdown)












