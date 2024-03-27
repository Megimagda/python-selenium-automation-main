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
driver.get('https://www.target.com/')
sleep(3)

# Click SignIn button
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
sleep(2)

# Click SignIn from side navigation
driver.find_element(By.ID, "listaccountNav-signIn").click()

sleep(2)

# sign login into your target account
driver.find_element(By.ID, "username").send_keys()
driver.find_element(By.ID,"password").send_keys()

# signIn button is shown
driver.find_element(By.ID, "login").click()
