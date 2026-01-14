from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then ('Search results for {expected_product} are shown')
def verify_search_results(context,expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]").text
    print(actual_text)
    assert expected_product in actual_text, f'Expected {expected_product} not in {actual_text}'


@then ('Add {expected_product} to cart')
def verify_search_results(context,expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]").text
    assert expected_product in actual_text, f'Expected {expected_product} not in {actual_text}'
    context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor14455606']").click()


