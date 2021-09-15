import pyautogui as py
#print(py.position())

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="enter path of chromedriver")
driver.get("http://gmail.com")

    
driver.find_element_by_id("identifierId").send_keys('enter emailid')
driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys('enter password')
driver.find_element_by_id("passwordNext").click()
time.sleep(10)


items = driver.find_elements_by_xpath("//*[@class='y6']/span")
    
for i in items:
        # print(i.text)
        if "ttendance" in i.text:
            i.click()
            time.sleep(5)
            driver.find_element_by_link_text("Open").click()
            new = driver.find_element_by_link_text("Open").text
            
#imports pyautogui for clicking final buttons use pyautogui.position() on your screen to find position of buttons
from click import *
clicknow()
driver.quit()
