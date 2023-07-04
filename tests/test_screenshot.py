import time
import pytest as pytest
import selenium.webdriver.common.driver_finder
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

import tests



class Testscreenshot:
    def test_login_screenshot(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tutorialsninja.com/demo/")
        time.sleep(3)

        # self.driver.save_screenshot("SShot2.png")
        # self.driver.get_screenshot_as_file("C:\\Users\\shashi\\PycharmProjects\\ORANGEHRM_23\\ScreenShots\\SShot1.png")
        width=1920
        height=9050
        self.driver.set_window_size(width,height)
        bodysuit = self.driver.find_element(By.TAG_NAME,"body")
        bodysuit.screenshot("fullpage11.png")
