from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

PRODUCT_NAME=(By.CSS_SELECTOR, "[data-test='cartItem-title']")
SIDE_NAV_PRODUCT_NAME=(By.CSS_SELECTOR, "h4[data-test='content-wrapper']")
TOTAL_TXT=(By.CSS_SELECTOR, "span[class*='styles_cart-summary-span']")



@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then ('Cart is empty')
def verify_empty_cart(context):
    #expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in actual_text, f'Expected "Your cart is empty" not in {actual_text}'


@then ('Verify cart has {amount} item(s')
def verify_cart_item(context, amount):
    context.driver.wait.until(
        EC.presence_of_element_located(*TOTAL_TXT),
        message='Subtotal did not appear'
    )

    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f'Expected {amount} item, but got {cart_summary}'


@then ('Verify product is in cart')
def verify_product(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='close']").click()
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'Expected product {expected[:20]}, but got {product_in_cart[:20]}'