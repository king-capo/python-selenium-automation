from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given ('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when ('Click on Account')
def click_account(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNavSignIn']").click()


@then ('Sign in page is shown')
def verify_signin_page(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNavSignIn']").text
    assert expected_text == actual_text, f'Expected {expected_text} not in {actual_text}'