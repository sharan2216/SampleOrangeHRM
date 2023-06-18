import time
import pytest as pytest
import selenium.webdriver.common.driver_finder
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import tests


class TestScrolldown:
    def test_scrolldown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://omayo.blogspot.com/")
        time.sleep(3)
        dropdown_element = self.driver.find_element(By.XPATH,"//div[@class='dropdown']")
        self.driver.execute_script("arguments[0].scrollIntoView(true)",dropdown_element)
        time.sleep(3)
        self.driver.get_screenshot_as_file("./ScreenShots/Dropdown_Button1.png")
        # self.driver.get_screenshot_as_file("C:\\Users\\shashi\\PycharmProjects\\ORANGEHRM_23\\ScreenShots\\DropDown_Button.png")