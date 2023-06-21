from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config.config import ProjectConfiguration


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def custom_click(self, element):
        WebDriverWait(
            self.driver,
            ProjectConfiguration.WAIT_TIMEOUT
        ).until(
            expected_conditions.visibility_of_element_located(element)).click()

    def custom_type(self, element, text):
        WebDriverWait(
            self.driver,
            ProjectConfiguration.WAIT_TIMEOUT
        ).until(
            expected_conditions.visibility_of_element_located(element)
        ).clear()
        
        WebDriverWait(
            self.driver,
            ProjectConfiguration.WAIT_TIMEOUT
        ).until(
            expected_conditions.visibility_of_element_located(element)
        ).send_keys(text)

    def get_page_title(self):
        return self.driver.title
