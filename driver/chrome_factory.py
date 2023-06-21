from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class ChromeDriver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()

        return cls._driver

    def __init__(self):
        if self._driver is not None:
            raise ValueError("An instance of this class already exists.")