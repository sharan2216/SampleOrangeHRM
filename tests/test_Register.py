import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestRegister:
    def test_create_account_with_mandate_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Arun")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Lal")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_timestamp())
        print(self.generate_email_timestamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("1234546")
        self.driver.find_element(By.ID, "input-confirm").send_keys("123456")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        # time.sleep(3)
        expected_text = "Register Account"
        print("-------------")
        print(self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text)
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)

    def test_create_account_with_all_fields(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://tutorialsninja.com/demo/")
        driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        driver.find_element(By.LINK_TEXT, "Register").click()
        driver.find_element(By.ID, "input-firstname").send_keys("Arun")
        driver.find_element(By.ID, "input-lastname").send_keys("Lal")
        driver.find_element(By.ID, "input-email").send_keys("self.generate_email_timestamp()")
        print(self.generate_email_timestamp())
        driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        driver.find_element(By.ID, "input-password").send_keys("1234546")
        driver.find_element(By.ID, "input-confirm").send_keys("123456")
        driver.find_element(By.XPATH, "//input[@value=1][@name='newsletter']").click()
        driver.find_element(By.NAME, "agree").click()
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        # time.sleep(3)
        expected_text = "Register Account"
        print("-------------")
        print(driver.find_element(By.XPATH, "//div[@id='content']/h1").text)
        assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)

        def test_register_with_dupliacte_email(self):
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://tutorialsninja.com/demo/")
            driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            driver.find_element(By.LINK_TEXT, "Register").click()
            driver.find_element(By.ID, "input-firstname").send_keys("Arun")
            driver.find_element(By.ID, "input-lastname").send_keys("Lal")
            driver.find_element(By.ID, "input-email").send_keys(self.generate_email_timestamp())
            print(self.generate_email_timestamp())
            driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
            driver.find_element(By.ID, "input-password").send_keys("1234546")
            driver.find_element(By.ID, "input-confirm").send_keys("123456")
            driver.find_element(By.XPATH, "//input[@value=1][@name='newsletter']").click()
            driver.find_element(By.NAME, "agree").click()
            driver.find_element(By.XPATH, "//input[@value='Continue']").click()
            # time.sleep(3)
            expected_text = "Register Account"
            print("-------------")
            print(driver.find_element(By.XPATH, "//div[@id='content']/h1").text)
            assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)


    def generate_email_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "arun" + timestamp + "@gmail.com"
