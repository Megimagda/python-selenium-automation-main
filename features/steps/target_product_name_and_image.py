from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I navigate to the Target website')
def navigate_to_target_website(context):
    context.driver.get('https://www.target.com')


@when('I search for a product on Target')
def search_for_product(context):
    search_input = context.driver.find_element(By.CSS_SELECTOR, "[data-test='search']")
    search_input.clear()
    search_input.send_keys('nail polish')
    search_input.submit()


@then('I should see product name and image for each product on the search results page')
def verify_product_name_and_image(context):
    product_names = context.driver.find_elements(By.CSS_SELECTOR, "[class='styles__StyledItemTitleDiv-sc-15suhkx-2']")
    product_images = context.driver.find_elements(By.CSS_SELECTOR, "[class='styles__StyledDiv-sc-14g6sh1-0']")

    assert len(product_names) == len(product_images), "Number of product names and product images don't match"

    for product_name, product_image in zip(product_names, product_images):
        assert product_name.text, "Product name is missing"
        assert product_image.get_attribute('src'), "Product image is missing"
