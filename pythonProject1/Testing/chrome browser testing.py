#import the necessary module as:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))

# Get the website URL
website_url = "https://www.mindrisers.com.np"

# Open the website
driver.get(website_url)

#maximize the window size
driver.maximize_window()
time.sleep(5)

#extract the website title:
web_site_title = driver.title
print(f"website title is:,{web_site_title}")

# Close the WebDriver
driver.quit()


