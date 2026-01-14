from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then ('Find story cards on Target Circle')
def find_story_cards(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/circlecard']")
    context.driver.find_element(By.CSS_SELECTOR, "[href='/l/target-circle-360/-/N-2rguk']")