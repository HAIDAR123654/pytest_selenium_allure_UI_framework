from selenium.webdriver.common.by import By

from base_pages.base_page import BaseClass


class ProductsPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    products_locator = (By.CLASS_NAME, "title")

    def verify_products_page (self, expected_products_name) -> bool:
        return self.verify_text_on_page(self.products_locator, expected_products_name)
