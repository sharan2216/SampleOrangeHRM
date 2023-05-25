# import pytest
import time
from itertools import count

# import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager



class Oneline:
    def getall(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.flipkart.com/")
        time.sleep(3)
        pop_up=driver.find_element("xpath","//button[@class='_2KpZ6l _2doB4z']")
        pop_up.click()
        # driver.implicityl_wait(10)
        # time.sleep(3)
        elements = driver.find_elements("xpath","//div[@class='eFQ30H']")

        return [element.text for element in elements if element.text.endswith("s")]


    # if element.text.endswith("s")


oneline = Oneline()
element_text=oneline.getall()
print(element_text)
