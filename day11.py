# day-9
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime,date

driver= webdriver.Chrome()
driver.maximize_window()
driver.get(r"file:///C:/Users/NAVA/Downloads/Locator%20Practice/Locator%20Practice/locatorPractice.html")

# #iframe
# driver.switch_to.frame("test_iframe")#id,name
# # driver.switch_to.frame(0)
# #driver.find_element(By.NAME,"frame_submit_button").click()
# driver.find_element(By.NAME,"frame_submit_button")
# driver.switch_to.default_content()
# driver.find_element(By.ID,"test-alert").click()
## find element and find elements
   #HANDLING TABS AND WINDOWS
#tabs
# driver.find_element(By.XPATH,"//button[@class='tabs' and text()='New Tab']").click()
# print(driver.title)
# # driver.current_window_handle
# tabs=driver.window_handles
#
# print(tabs)
# driver.switch_to.window(tabs[1])
#
# driver.find_element(By.XPATH,"//a[text()='Courses']").click()
# time.sleep(5)
#windows

driver.find_element(By.XPATH,"//button[@class='tabs' and text()='New Window']").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
driver.find_element(By.XPATH,"//a[text()='Courses']").click()

time.sleep(5)

driver.quit()