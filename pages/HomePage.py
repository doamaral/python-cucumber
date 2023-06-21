from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
