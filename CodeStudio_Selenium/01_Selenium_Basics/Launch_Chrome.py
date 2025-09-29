import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.in")
print("Google page opened...")
time.sleep(5)

driver.refresh()
print("Page refreshed..")

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)
print("Automation practice page opened...")

driver.get("https://www.saucedemo.com/")
print("SauceDemo opened..")

# Locate username field and enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")
print("Username entered...")

time.sleep(3)

# Locate password field and enter password
driver.find_element(By.ID,"password").send_keys("secret_sauce")
print("Password entered...")

# Click on login button
driver.find_element(By.ID, "login-button").click()
print("Clicked on Login button")

# Browser will stay open unless we press enter button in console
input("Press Enter to exit...")
