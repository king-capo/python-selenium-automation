from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given ('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when ('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@then ('Search results for tea are shown')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'
