from selenium.webdriver.common.by import By
from base_pages.base_page import BaseClass

class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")

    def login(self, username, password):
        self.send_key_in_element(self.username_locator, username)
        self.send_key_in_element(self.password_locator, password)
        self.click_element(self.login_button_locator)

