from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class DriverFactory:
    @staticmethod
    def get_driver(browser: str = "chrome", headless: bool = False):
        browser = browser.lower()
        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")
            return webdriver.Firefox(options=options)

        elif browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            return webdriver.Edge(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")