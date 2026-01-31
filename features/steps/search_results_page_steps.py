from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

SIDE_NAV_PRODUCT_NAME=(By.CSS_SELECTOR, "h4[class^='styles_ndsHeading']")
PRODUCT_NAME=(By.CSS_SELECTOR, "[data-test='cartItem-title']")
ADD_TO_CART_BTN=(By.CSS_SELECTOR, "button[id^='addToCart']")
SIDE_NAV_ADD_TO_CART_BTN=(By.CSS_SELECTOR, "button[data-test='shippingButton']")
SEARCH_RESULTS_TEXT=(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")



@then ('Search results for {expected_product} are shown')
def verify_search_results(context,expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_product in actual_text, f'Expected {expected_product} not in {actual_text}'


@when ('Click on Add to Cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

    context.driver.wait.until(
        EC.element_to_be_clickable(*SIDE_NAV_ADD_TO_CART_BTN),
        message='Add to cart button not clickable'
    )

@when ('Click on Add to Cart button on sidebar')
def add_to_cart_sidebar(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()


@when ('Store product name')
def store_product_name(context):
    context.product_before_adding = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    #print('Name saved: ')
    #print(context.product_before_adding)


@then ('Verify product in cart is correct')
def verify_product_in_cart(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'Expected product {expected[:20]}, but got {product_in_cart[:20]}'
