#day-7
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get(r"file:///C:/Users/NAVA/Downloads/Locator%20Practice/Locator%20Practice/locatorPractice.html")
time.sleep(3)
# buttonsubmit=driver.find_element(By.NAME,'submit_button')
# print(buttonsubmit.text)
# print(buttonsubmit.get_attribute("qa"))
# buttonsubmit.click()
employetextbox=driver.find_element(By.XPATH,"//input[@name='emp_name']")
employetextbox.send_keys("hemanth")
print(employetextbox.get_attribute("value")) # used to get text from the text box and textarea
# find element
# buttons=driver.find_element(By.TAG_NAME,"button")
# print(buttons)
# print(type(buttons))
# find elements
# buttons=driver.find_elements(By.TAG_NAME,"button")
# for button in buttons:

# print(button.is_displayed())

#  print(button.text)
# print(type(buttons))
# checkboxes
# hemanth=driver.find_element(By.XPATH,"//input[@TYPE='checkbox' and @value='project-1']")
# hemanth.click()
# print(hemanth.is_selected())
# time.sleep(3)
#  radiobuttons

# hemanth=driver.find_element(By.XPATH,"//input[@TYPE='radio' and @value='project-3']")
# hemanth.click()
# print(hemanth.is_selected())
# n9time.sleep(3)
# chromepage =driver.title
# print(chromepage)
# driver.quit()
