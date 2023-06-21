from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config.config import ProjectConfiguration


class FirefoxDriver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:

            options = Options()
            options.binary_location = ProjectConfiguration.FIREFOX_EXECUTABLE_PATH
            cls._driver = webdriver.Firefox(options=options)

        return cls._driver

    def __init__(self):
        if self._driver is not None:
            raise ValueError("An instance of this class already exists.")
