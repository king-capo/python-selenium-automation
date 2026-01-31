from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

from features.steps.search_results_page_steps import store_product_name

SELECTED_COLOR=(By.CSS_SELECTOR, "[data-test='@web/variationComponent']div")
COLOR_OPTIONS=(By.CSS_SELECTOR, "li[class*='CarouselItem'] img")


@given('Open Target product A-90534123')
def open_product(context):
    context.driver.get(f'https://www.target.com/p/wrangler-men-39-s-atg-synthetic-straight-utility-pants/-/A-90534123?preselect=89856072#lnk=sametab')


@then('Verify user can select different colors')
def verify_color_selection(context):
    expected_colors=['Blue Nights', 'Caviar', 'Morel','Dark Shadow']
    actual_colors=[]

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for c in colors:
        c.click()
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color: ', selected_color)

        selected_color = selected_color.split('\n')[1:]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match {actual_colors}'