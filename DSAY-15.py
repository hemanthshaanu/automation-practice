
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
driver.set_page_load_timeout(10)
print(driver.timeouts.page_load)
# driver.maximize_window()driver.set_network_conditions(
#     offline=False,
#     latency=5,
#     download_throughput=1 * 1024,
#     upload_throughput=1 * 1024,
#
# )
driver.get(r"https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# method1 using actionchains
leftbutton =driver.find_element(By.ID,"left-click")
# ActionChains(driver).scroll_to_element(leftbutton).perform()
# time.sleep(5)
# print(driver.get_network_conditions())
# driver.quit()
# method2 USING location_once_scrolled_into_view *(WEBELEMENT)
leftbutton.location_once_scrolled_into_view
time.sleep(3)
driver.quit()
print("dghuihgfdfghjkjhgfd")