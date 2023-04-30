#how to send input to an text box
# submitbutton= driver.find_element(By.NAME,'emp_name')
# submitbutton.send_keys("hemanth")
# # how to get attribute value of element
# submitbutton= driver.find_element(By.TAG_NAME,"a")
# href=submitbutton.get_attribute("href")
# print(href)
# # how to fetch text from the text boxfrom selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# driver= webdriver.Chrome()
# driver.maximize_window()
# driver.get("D:\Downloads\locatorPractice.html")
# chromepage =driver.title
# print(chromepage)
# submitbutton= driver.find_element(By.NAME,'emp_name')
# submitbutton.send_keys("hemanth")
# print(f'{submitbutton.get_attribute("value")}')
#
#
# time.sleep(10)
# driver.quit()