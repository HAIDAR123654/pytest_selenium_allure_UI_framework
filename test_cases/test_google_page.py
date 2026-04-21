import logging

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest

logger = logging.getLogger(__name__)

@pytest.mark.sanity
def test_google(driver, class_fixture, module_fixture, package_fixture):
    driver_instance, url = driver
    logger.info(f"Going to https://www.google.com")
    allure.attach("Navigated to https://www.google.com", name="Step 1", attachment_type=allure.attachment_type.TEXT)
    driver_instance.get("https://www.google.com")
    searchbox = driver_instance.find_element(By.NAME, "q")
    logger.info(f"Searching for {searchbox.text} locator")
    allure.attach(f"Searching for {searchbox.text} locator", name="Step 2", attachment_type=allure.attachment_type.TEXT)
    searchbox.send_keys(Keys.ENTER)
    logger.info(f"Entering 'Enter' button in searchbox")
    allure.attach(f"Entering 'Enter' button in searchbox", name="Step 3", attachment_type=allure.attachment_type.TEXT)
    searchbox.send_keys("python")
    logger.info(f"Entering 'python' button in searchbox")
    allure.attach(f"Entering 'python' button in searchbox", name="Step 4", attachment_type=allure.attachment_type.TEXT)
    assert "Google" in driver_instance.title
    logger.info("test got passed")
    allure.attach("test got passed", name="Step 5", attachment_type=allure.attachment_type.TEXT)
