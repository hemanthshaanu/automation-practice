import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime,date
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.implicitly_wait(5)

driver.get(r"https://www.flipkart.com/")
driver.find_element(By.CSS_SELECTOR,"button[class='_2KpZ6l _2doB4z']").click()
search=driver.find_element(By.NAME,"q")
search.send_keys("laptops")
searchbutton=driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)
driver.quit()
