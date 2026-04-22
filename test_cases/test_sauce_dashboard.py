import pickle
import time
from pathlib import Path

import pytest
from selenium.webdriver.common.by import By

BASE_DIR = Path(__file__).resolve().parent.parent

@pytest.mark.smoke
def test_sauce_dashboard(driver, login):
    driver_instance, url = driver
    driver_instance.get("https://www.saucedemo.com/")   # open the site first
    # Load cookies from a file
    with open(BASE_DIR / "cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
    # Add cookies to the browser
    for cookie in cookies:
        driver_instance.add_cookie(cookie)
    # Refresh to apply cookies
    driver_instance.refresh()
    driver_instance.get("https://www.saucedemo.com/inventory.html")
    driver_instance.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver_instance.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']").click()
    driver_instance.find_element(By.ID, "checkout").click()
    time.sleep(2)