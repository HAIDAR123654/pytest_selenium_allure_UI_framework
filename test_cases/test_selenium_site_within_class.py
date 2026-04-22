import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.regression
class TestClass:
    def test_selenium(self, driver, class_fixture, module_fixture, package_fixture):
        driver_instance, url = driver
        driver_instance.get("https://www.selenium.dev/")
        driver_instance.find_element(By.ID, "navbarDropdown").click()
        driver_instance.find_element(By.XPATH, "//div[@class='dropdown-menu show']/a[1]").click()
        assert "About Selenium" in driver_instance.title

    def test_selenium_second(self, driver, class_fixture, module_fixture, package_fixture):
        driver_instance, url = driver
        driver_instance.get("https://www.selenium.dev/")
        driver_instance.find_element(By.ID, "navbarDropdown").click()
        WebDriverWait(driver_instance, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown-menu show']/a[1]"))).click()
        el = driver_instance.find_element(By.XPATH, "//a[contains(text(), 'Learn more')]")
        try:
            el.click()
        except Exception:
            driver_instance.execute_script("arguments[0].scrollIntoView(true);", el)
            el.click()
        element = driver_instance.find_element(By.XPATH, "//h2[text()='Sponsoring']")
        assert element.text == "Sponsoring"