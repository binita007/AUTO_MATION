#import the necessary module as:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))

#open the website as:
driver.get("https://demoqa.com/text-box")

#maximize the window
driver.maximize_window()
time.sleep(4)

#find or locate the element by their xpath method
full_name =driver.find_element(*(By.XPATH,"//input[@id='userName']"))
email_field=driver.find_element(*(By.XPATH,"//input[@id='userEmail']"))
current_address=driver.find_element(*(By.XPATH,"//textarea[@id='currentAddress']"))
permanent_address=driver.find_element(*(By.XPATH,"//textarea[@id='permanentAddress']"))

#fill the form as:
full_name.send_keys("Binita")
email_field.send_keys("binita@gmail.com")
current_address.send_keys("Bhaktapur")
permanent_address.send_keys("kavre")
time.sleep(5)

#close the webdriver instance as:
driver.quit()
print("finally code sucessfully ")