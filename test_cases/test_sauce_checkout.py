import pickle
import time
from pathlib import Path

import pytest
from selenium.webdriver.common.by import By
from utilities.csv_reader import read_csv

BASE_DIR = Path(__file__).resolve().parent.parent

@pytest.mark.smoke
@pytest.mark.parametrize("row", read_csv(BASE_DIR / "test_data" / "user_data.csv"))
def test_sauce_dashboard(driver, row):
    value = row['first_name,last_name,postal_code']
    first_name, last_name, postal_code = value.split(",")
    driver_instance, url = driver
    driver_instance.get("https://www.saucedemo.com/")   # open the site first

    # Load cookies from a file
    with open("../cookies.pkl", "rb") as f:
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
    driver_instance.find_element(By.ID, "first-name").send_keys(first_name)
    driver_instance.find_element(By.ID, "last-name").send_keys(last_name)
    driver_instance.find_element(By.ID, "postal-code").send_keys(postal_code)
    driver_instance.find_element(By.NAME, "continue").click()
    driver_instance.find_element(By.ID, "finish").click()
    time.sleep(2)


