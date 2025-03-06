from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)  # Wait for the page to load

# Find the search bar and enter the query
search_box = driver.find_element(By.NAME, "username")
search_box.send_keys("Admin")
search_box = driver.find_element(By.NAME, "password")
search_box.send_keys("admin123")
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for results to load

# Close the browser
driver.quit()