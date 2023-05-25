#day-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get(r"file:///C:/Users/NAVA/Downloads/Locator%20Practice/Locator%20Practice/locatorPractice.html")

#textarea
# time.sleep(29)
# textarea=driver.find_element(By.ID,"description")
# textarea.send_keys("hemanth")
# time.sleep(19)
# print(textarea.get_attribute("value")) # used to get text from the text box and textarea
# time.sleep(3)
# driver.quit()

#normal dropdown(without using selector class)

# dropdown=driver.find_element(By.CSS_SELECTOR,"#projectName>option[value='Project-3']").click()
# time.sleep(5)
# driver.quit()
#normal dropdown( using selector class)

projectdropdown=driver.find_element(By.ID,"projectName")
dropdown=select(projectdropdown)
dropdown