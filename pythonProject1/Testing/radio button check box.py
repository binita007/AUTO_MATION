#import the necessary module as:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import  time

#set the chrome webdriver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url as:
website_url="https://formy-project.herokuapp.com/form"
#open the website:
driver.get(website_url)
#maximize the window size
driver.maximize_window()
time.sleep(1)
#locate the form fill locator:
first_name=driver.find_element(By.XPATH,"//input[@id='first-name']")
last_name=driver.find_element(By.XPATH,"//input[@id='last-name']")
Job_title=driver.find_element(By.XPATH,"//input[@id='job-title']")



#handle the radio button as:
Level_of_education=driver.find_element(By.XPATH,"//input[@id='radio-button-2']")

#handle the checkbox:
female=driver.find_element(By.XPATH,"//input[@id='checkbox-2']")
#fill the content:
first_name.send_keys("Binita")
last_name.send_keys("Tamang")
Job_title.send_keys("QA learner")
Level_of_education.click()
female.click()
time.sleep(2)

#handle the drop down element as:
select_options=driver.find_element(By.XPATH,"//select[@id='select-menu']")
select_options.click()
first_options=driver.find_element(By.XPATH,"//option[@value='3']")
first_options.click()

#handle the date picker as:
datepicker=driver.find_element(*(By.XPATH,"//input[@id='datepicker']"))
datepicker.send_keys()
time.sleep(1)

#handle the submit
submit=driver.find_element(*(By.XPATH,"//a[normalize-space()='Submit']"))
submit.click()
time.sleep(3)

#extract the title as:
website_title=driver.title
print(f"Website title:{website_title}")

#close the webdriver instance
driver.quit()