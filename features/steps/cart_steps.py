from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given ('Open Target main page')


@when ('Click on Cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then ('Cart is empty')
def verify_empty_cart(context):
    #expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in actual_text, f'Expected {expected_text} not in {actual_text}'