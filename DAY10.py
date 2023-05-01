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
# datepicker/calender
# approach 1 by giving the date in the text box
# datepicker=driver.find_element(By.CSS_SELECTOR,"input[id=my_date_picker]")
# datepicker.click()
# time.sleep(3)
# datepicker.send_keys("09/05/2023")
# time.sleep(5)
# datepicker.send_keys(Keys.ENTER)
# time.sleep(5)
# # approach 2 by selecting the date by calender
# # dateinput="01/04/2023"
# dateinput=date(2023,9,1)
# datepicker=driver.find_element(By.ID,"my_date_picker")
# datepicker.click()
# time.sleep(5)
# nextmonth= lambda: driver.find_element(By.CLASS_NAME, "ui-datepicker-prev").click()
# prevmonth= lambda: driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
# def datepicker():
#     while True:
#         currentyear:int=int(driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text)# typecasting (converting the the text into integer)and we are retriuve the text of an element
#         currentmonth:str=driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text.strip()
#     # striop=elemenate the spaces(reeling snd traling spaces)
#         calenderDate = datetime.strptime(f"{currentyear} {currentmonth}","%Y %B").date()
#
#         if calenderDate.year>dateinput.year:
#             driver.find_element(By.CLASS_NAME, "ui-datepicker-prev").click()
#             continue
#         elif calenderDate.year<dateinput.year:
#             driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
#             continue
#
#         if calenderDate.month>dateinput.month:
#             driver.find_element(By.CLASS_NAME, "ui-datepicker-prev").click()
#             continue
#         elif calenderDate.month<dateinput.month:
#             driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
#             continue
#
#         driver.find_element(By.XPATH,f"//table(@class='ui-datepicker-calender']//a[text()='{dateinput.day}']/parent::td")
#         break
# datepicker()

#alert

# driver.find_element(By.ID,"test-alert").click()
# alert=driver.switch_to.alert
# time.sleep(4)
# print(alert.text)
# alert.accept()

# prompt
#

#fileupload
driver.find_element(By.ID,"uploadFile").send_keys("C:\\Users\\NAVA\\Desktop\\hemanth.txt.txt")
time.sleep(3)
fileupload=driver.switch_to.alert
fileupload.accept()
time.sleep(5)
driver.quit()