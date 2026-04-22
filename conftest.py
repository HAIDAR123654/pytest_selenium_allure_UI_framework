import pickle
import allure
import pytest
from selenium.webdriver import edge

from base_pages.login_page import LoginPage
from utilities.read_config_file import read_config
from utilities.driver_factory import DriverFactory
from pathlib import Path
import logging

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store", default="false")
    parser.addoption("--env", action="store", default="DEV")

@pytest.fixture(scope="session", autouse=True)
def load_config(request):
    config = read_config(request.config.getoption("--env"))
    config["browser"] = request.config.getoption("--browser")
    config["headless"] = request.config.getoption("--headless") == "true"
    return config

@pytest.fixture(scope="function")
def driver(load_config):
    browser = load_config["browser"]
    headless = load_config["headless"]
    driver = DriverFactory.get_driver(browser, headless)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver, load_config["url"]
    driver.quit()

BASE_DIR = Path(__file__).resolve().parent

@pytest.fixture(scope="session", autouse=True)
def login(load_config):
    driver_instance = DriverFactory.get_driver(load_config["browser"])
    driver_instance.get(load_config["url"])
    login_page = LoginPage(driver_instance)
    login_page.login("standard_user", "secret_sauce")
    with open(BASE_DIR / "cookies.pkl", "wb") as f:
        pickle.dump(driver_instance.get_cookies(), f)
    with open(BASE_DIR / "cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        print(cookies)
    driver_instance.quit()

@pytest.fixture(scope="package")
def package_fixture():
    return {"DB connection": "Active"}

@pytest.fixture(scope="module")
def module_fixture():
    data_from_module_fixture = "data from module fixture"
    return data_from_module_fixture

@pytest.fixture(scope="class")
def class_fixture():
    data_from_class_fixture = "data from class fixture"
    return data_from_class_fixture

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

import pytest
import time

# Hook: runs after each test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # Only act on test failures
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            driver_instance, _ = driver_fixture
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshots_dir = Path(__file__).parent / "screenshots"
            screenshots_dir.mkdir(exist_ok=True)
            screenshot_name = f"screenshot_{item.name}_{timestamp}.png"
            screenshot_path = screenshots_dir / screenshot_name
            driver_instance.save_screenshot(str(screenshot_path))
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            print(f"\n[!] Screenshot saved: {screenshot_name}")




