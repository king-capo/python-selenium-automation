from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIDE_NAV_PRODUCT_NAME=(By.CSS_SELECTOR, "h4[class^='styles_ndsHeading']")
TOTAL_TXT=(By.CSS_SELECTOR, "span[class*='styles_cart-summary-span']")
PRODUCT_NAME=(By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then ('Search results for {expected_product} are shown')
def verify_search_results(context,expected_product):
    actual_text = context.driver.find_element(By.ID, 'item-title-0d7f4bf0-f11c-11f0-a561-ff89e2e51f2b').text
    print(actual_text)
    assert expected_product in actual_text, f'Expected {expected_product} not in {actual_text}'


@when ('Click on Add to Cart button')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[id^='addToCart']").click()


@when ('Click on Add to Cart button on sidebar')
def add_to_cart_sidebar(context):
    context.driver.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME))
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='shippingButton']").click()


@when ('Store product name')
def store_product_name(context):
    context.product_before_adding = context.driver.find_element(By.XPATH, "//h4").text
    print('Name saved: ')
    print(context.product_before_adding)


@then ('Verify cart has {amount} item')
def verify_cart_item(context, amount):
    context.driver.wait.until(
        EC.presence_of_element_located(TOTAL_TXT),
        message='Subtotal did not appear'
    )

    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f'Expected {amount} item, but got {cart_summary}'

@then ('Verify product in cart is correct')
def verify_product_in_cart(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'Expected product {expected[:20]}, but got {product_in_cart[:20]}'
