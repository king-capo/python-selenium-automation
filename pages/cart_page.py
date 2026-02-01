from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/cartIcon']")

    def open_cart_page(self):
        self.click(self.CART_ICON)

    def verify_empty_cart(self):
        expected_text = 'Your cart is empty'
        actual_text = self.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
        assert expected_text in actual_text, f'Expected "{expected_text}" not in {actual_text}'
