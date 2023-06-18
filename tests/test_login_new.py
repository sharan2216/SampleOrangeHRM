import time

import allure
import pytest as pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestLogin:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("sksharan666@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("155113412")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("")
        self.driver.find_element(By.ID,"input-password").send_keys("")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        expected_warning_message="Warning: No match for E-Mail Address and/or Password.abc"
        assert self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
