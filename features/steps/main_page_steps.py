from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@given ('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when ('Click on Sign in')
def click_account(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()


@then ('Sign in page is shown')
def verify_signin_page(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//div[@tabindex='-1']").text
    assert expected_text in actual_text


@when ('Search and add {product} to cart')
def search_add_to_cart(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    context.driver.find_element()