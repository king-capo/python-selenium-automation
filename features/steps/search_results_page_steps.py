from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then ('Search results for {expected_product} are shown')
def verify_search_results(context,expected_product):
    actual_text = context.driver.find_element(By.ID, 'item-title-0d7f4bf0-f11c-11f0-a561-ff89e2e51f2b').text
    print(actual_text)
    assert expected_product in actual_text, f'Expected {expected_product} not in {actual_text}'


@when ('Add {product} to cart')
def add_to_cart(context,product):
    context.driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Add to cart']").click()


