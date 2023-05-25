# ALLURE REPORT GENERATION LINK : #tutorials 39 || Selenium Pytest Allure report || Python Selenium (YOUTUBE VIDEO)

import pytest
import time
import allure
from selenium import webdriver


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()


@allure.description("Validate OrangeHRM with correct credentials")
@allure.severity(severity_level="CRITICAL")
def test_valid_Login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.find_element("xpath", "//input[@name='username']").clear()
    enter_username("Admin")
    driver.find_element("xpath", "//input[@name='password']").clear()
    enter_password("admin123")
    time.sleep(5)
    driver.find_element("xpath", "//button[normalize-space()='Login']").click()
    time.sleep(5)
    assert "dashboard" in driver.current_url
    time.sleep(3)


@allure.description("Validate OrangeHRM with incorrect credentials")
@allure.severity(severity_level="NORMAL")
def test_invalid_Login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.find_element("xpath", "//input[@name='username']").clear()
    enter_username("Admin")
    driver.find_element("xpath", "//input[@name='password']").clear()
    enter_password("admin123123")
    time.sleep(3)
    driver.find_element("xpath", "//button[normalize-space()='Login']").click()
    time.sleep(3)

    try:
        assert "dashboard" in driver.current_url
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(),
                          name="SCREENSHOT FOR : Invalid Credentials", attachment_type=allure.attachment_type.PNG)


@allure.step("Entering username as {0}")
def enter_username(username):
    driver.find_element("xpath", "//input[@name='username']").send_keys(username)


@allure.step("Entering password as {0}")
def enter_password(password):
    driver.find_element("xpath", "//input[@name='password']").send_keys(password)

# under Genearl >click on Advanced  > Use custom workspace >Directory >
# and copy and paste ur Pycharm project location Path :(C:\Users\shashi\PycharmProjects\ORANGEHRM_23)
#-----------------------------------------------------------------------------------------------------------
# put these 2 lines in Jenkins under Build Steps >Execute Windows batch command> Command BOX:--------

# call ./venv/Scripts/activate.bat
# pytest -v -s operations/test_login.py --alluredir=Report
#---------------------------------------------------------------------------------------------------------

# OR :--------

# call ./venv/Scripts/activate.bat
# pytest -v -s --alluredir='reports' operations/test_login.py
# pytest selenium-python --alluredir=Report --junitxml=Result.xml --html=Report.html
