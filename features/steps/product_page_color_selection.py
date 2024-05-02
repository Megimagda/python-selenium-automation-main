from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I navigate to the Target product page')
def navigate_to_product_page(context):
    context.driver.get('https://www.target.com/p/A-91511634')

@when('I loop through each color option')
def loop_through_color_options(context):
    color_options = context.driver.find_elements(By.CSS_SELECTOR, "div[class='children']")
    for color_option in color_options:
        color_option.click()

@then('I should see that each color option is selected')
def verify_color_options_selected(context):
    color_options = context.driver.find_elements(By.CSS_SELECTOR, "div[class='children']")
    for color_option in color_options:
        # Check if the color option is selected
        assert 'selected' in color_option.get_attribute('class').split(), "Color option is not selected"


