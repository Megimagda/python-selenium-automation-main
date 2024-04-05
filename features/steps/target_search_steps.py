from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target main page')
def open_target_main_page(context):
    (context.driver.get('https://www.target.com/')

@when('Click on Cart icon')
def click_on_cart_icon(context):
    (context.driver.find_element(By.XPATH, "//div[@data-test=@web/CartIcon]").click

@then('verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    (context.driver.find_element(By.XPATH, "div[@data-test=boxEmptyMsg]")