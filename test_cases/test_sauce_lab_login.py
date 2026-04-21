import pickle

import pytest
from base_pages.products_page import ProductsPage

@pytest.mark.order(2)
@pytest.mark.regression
def test_valid_login(driver, login):
    driver_instance, url = driver
    driver_instance.get("https://www.saucedemo.com/")
    product_page = ProductsPage(driver_instance)
    # Load cookies from a file
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
    # Add cookies to the browser
    for cookie in cookies:
        driver_instance.add_cookie(cookie)
    driver_instance.refresh()
    driver_instance.get("https://www.saucedemo.com/inventory.html")
    assert "inventory.html" in driver_instance.current_url
    assert product_page.verify_products_page("Products")

@pytest.mark.order(1)
@pytest.mark.sanity
@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"), ("standard_user1", "secret_sauce1")
])
def test_parameterized(username,password):
    print(username,password)









