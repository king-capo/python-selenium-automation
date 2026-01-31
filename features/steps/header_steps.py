from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/UtilityNav']")


@when ('Click on Cart')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when ('Search for {product}')
def search_product(context,product):
    context.driver.find_element(*SEARCH_FIELD).send_keys({product})
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(10)


@when ('Click on Target Circle')
def click_header_menu(context):
    context.driver.find_element(By.ID, "utilityNav-circle").click()


@then ('Verify top header links are shown')
def verify_header_links(context):
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
