from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def send_key_in_element(self, element, key):
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(key)

    def click_element(self, element):
        self.driver.find_element(*element).click()

    def verify_text_on_page (self, element ,expected_products_name) -> bool:
        return self.driver.find_element(*element).text == expected_products_name

    def wait_for_click(self, element , time : int = 10):
        (WebDriverWait(self.driver, time).
         until(EC.element_to_be_clickable(*element)).click())
