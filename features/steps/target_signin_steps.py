from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given ('From target main page click Account')
def open_main(context):
    context.driver.get('https://www.target.com/')
    context.driver.find_element(By.ID, "account-sign-in").click()

@when ('Click on Sign in')
def click_account(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()


@then ('Sign in page is shown')
def verify_signin_page(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//div[@tabindex='-1']").text
    assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'