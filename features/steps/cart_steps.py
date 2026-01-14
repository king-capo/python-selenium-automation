from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then ('Cart is empty')
def verify_empty_cart(context):
    #expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in actual_text, f'Expected "Your cart is empty" not in {actual_text}'


@then ('Verify {expected_product} is in cart')
def verify_product_in_cart(context,expected_product):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='close']").click()
    actual_text = expected_product
    assert expected_product in actual_text, f'Expected {expected_product} not in {actual_text}'