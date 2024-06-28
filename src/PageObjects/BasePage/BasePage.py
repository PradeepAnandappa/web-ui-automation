import math
import os
import random
import string
import time

import openpyxl
import pytest
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

""" This class contains all the generic methods & utilities for all pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def clickToElement(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 50).until(ec.element_to_be_clickable(by_locator))
            elementText = element.text
            element.click()
            print("Clicked on element - ", elementText)
        except:
            print("Element not found")

    def mouseHoverOnElement(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            a = ActionChains(self.driver)
            # hover over element
            a.move_to_element(element).perform()
            print("Hover on element")
        except:
            print("Element not found")

    def clickOnElementByActionClass(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            action = ActionChains(self.driver)
            action.click(on_element=element)
            action.perform()
            print("click on element")
        except:
            print("Element not found")

    def clickToElementByJavaScriptExecutor(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
            print("Clicked on element")
        except:
            self.driver.get_screenshot_as_file("screenshot.png")
            print("Element not found")

    def uploadFile(self, by_locator, filePath):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            element.send_keys(filePath)
            print("File upload -using file path: "+filePath)
        except:
            print("Element not found")


    def scrollIntoViewElement(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            print("Element found")
        except:
            print("Element not found")

    def enterValueToTextbox(self, by_locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
            print("Enter value in textbox :", text)
        except:
            print("Element not found")

    def enterValueToTextboxByJavascriptExecutor(self, by_locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            value_to_enter = text
            self.driver.execute_script("arguments[0].value = arguments[1]", element, value_to_enter)
            print("Enter value in textbox :", text)
        except:
            print("Element not found")

    def clear_textbox(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        element.clear()

    def getElementText(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            print("Extracted element text: ", element.text)
            return element.text
        except:
            print("Element not found")
            return None

    def getElementValue(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            print("Extracted Element value - ", element.get_attribute('value'))
            return element.get_attribute('value')
        except:
            print("Element not found")
            return None

    def isElementDisplayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            print("Element found")
            return bool(element)
        except:
            print("Element not displayed")
            return False

    def isElementDisabled(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            print("Element found")
            return element.get_property('disabled')
        except:
            print("Either Element not found OR not disabled")
            return False

    def get_AttributeValue(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)

    def get_CSSAttributeValue(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.value_of_css_property(attribute)


    def isElementActive(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            print("Element found")
            return element.get_property('active')
        except:
            print("Either Element not found OR not active")
            return False

    def isCheckbox_selected(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
            print("Element found")
            return element.is_selected()
        except:
            print("Either Element not found OR not selected")
            return False

    def selectDropdownValueByText(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        select = Select(element)
        select.select_by_visible_text(text)
        print("Dropdown selected with value - ", text)

    def get_selectedValueinDropdown(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        select = Select(element)
        return select.first_selected_option.text

    def switchToWindow(self):
        try:
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
            print("Switch to window")
        except:
            print("Window not found")

    def getPageTitle(self, titleText):
        try:
            flag = WebDriverWait(self.driver, 60).until(ec.title_contains(titleText))
            print("Page Title: ", self.driver.title)
            return flag
        except:
            print("Expected Title word - " + titleText + " not found in page title: " + self.driver.title)
            return False

    def getPageURL(self):
        try:
            url = self.driver.current_url
            print("Current page URL: ", url)
            return url
        except:
            print("Page not displayed")
            return None

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

    def get_alertText(self):
        try:
         alert = WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        except UnexpectedAlertPresentException as e:
         alert = WebDriverWait(self.driver, 5).until(ec.alert_is_present())
         return alert.text

    def accept_alert(self):
        alert = WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        alert.accept()

    def generate_random_phone_number(self):
        area_code = random.randint(100, 999)
        prefix = random.randint(100, 999)
        line_number = random.randint(1000, 9999)
        return f"{prefix}{line_number}"

    def generate_random_string(self, len):
        return ''.join(random.choices(string.ascii_letters, k=len))

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

    def get_excel_cell_value(file_path, sheet_name, row, column):
        try:
            # Load the Excel workbook
            workbook = openpyxl.load_workbook(file_path)

            # Select the worksheet by name
            sheet = workbook[sheet_name]

            # Get the cell value from the specified row and column
            cell_value = sheet.cell(row=row, column=column).value

            # Close the workbook
            workbook.close()

            return cell_value
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def is_ascending_Order(values):
        # Check if the list is empty or has only one element (it's considered ascending)
        if len(values) <= 1:
            return True

        # Iterate through the list to check if each string is less than or equal to the next one
        for i in range(len(values) - 1):
            if values[i] > values[i + 1]:
                return False

        return True

    def is_descending_Order(values):
        # Check if the list is empty or has only one element (it's considered descending)
        if len(values) <= 1:
            return True

        # Iterate through the list to check if each string is greater than or equal to the next one
        for i in range(len(values) - 1):
            if values[i] < values[i + 1]:
                return False

        return True
