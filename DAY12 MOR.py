
# day-12
# tool tip
    #    title
    #    dynamic


# webdriver
    # name
    # current url
    # fullscreen window
    # minimize window
    # back
    # forward
    # refresh
    # screenshot

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime,date
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()
driver.get(r"https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# # title
# expectedresult="Please enter your full name"
# actualresult=driver.find_element(By.NAME,'emp_name').get_attribute('title')
# assert expectedresult==actualresult
# time.sleep(10)
# driver.quit()


# driver.find_element(By.LINK_TEXT,'QA Circle').click()
# driver.back()
# time.sleep(5)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# driver.quit()


# print(driver.name)
# print(driver.current_url)
# driver.fullscreen_window()
# time.sleep(3)
# driver.minimize_window()
# time.sleep(3)
# driver.quit()
#
# #webdriver screenshot
# driver.save_screenshot("screenshot.png")
# driver.quit()                                                                                                                                                                                                                                                     

# #webelement screenshot
# driver.find_element(By.ID,'buttons').screenshot("buttons.png")
# # driver.quit()
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.ID, 'send-sms'))).click()
time.sleep(4)
driver.quit()
# ((By.ID, '3.send-sms')))







