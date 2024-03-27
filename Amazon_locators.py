from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


# By XPATH
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "(//h1[@class='a-spacing-small']")

# By IDs
driver.find_element(By.ID, " ap_email")
driver.find_element(By.ID, "continue").click()

# By XPATH

driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-top-medium a-size-small']")

# By IDs
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.ID, "ap-other-signin-issues-link")

# By ID for Create Your Amazon Account Button
driver.find_element(By.ID, "createAccountSubmit")

driver.quit()