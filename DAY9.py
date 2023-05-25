#day-9
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()
driver.maximize_window()
driver.get(r"file:///C:/Users/NAVA/Downloads/Locator%20Practice/Locator%20Practice/locatorPractice.html")
# multidropdown=driver.find_element(By.CSS_SELECTOR,"select[id='mul-projectName' ]>option[value='Project-4']").click()
# multidropdown=driver.find_element(By.ID,'mul-projectName')
# mdrop=Select(multidropdown)
# mdrop.select_by_value(option.g)
#mdrop.select_by_index(4)
# mdrop.select_by_visible_text('Project-3')
# print(mdrop.first_selected_option.text)
# # for select in mdrop.all_selected_options:
# #     print(select.text)
#
# print(mdrop.is_multiple)
# for select in mdrop.options:# print all options
#     print(select.text)

# for option in mdrop.options:
#     mdrop.select_by_visible_text(option.text)
#KEYS
# TEXTAREA=driver.find_element(By.ID,"description")
# TEXTAREA.send_keys("hello world", Keys.ENTER,"how are you")
# time.sleep(4)
# TEXTAREA.clear()

# MULTIDROPDOWN without select class
# ACTIONCHAINS
time.sleep(4)
driver.quit()