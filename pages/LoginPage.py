from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    emailInput = (By.ID, "email")
    passwordInput = (By.ID, "senha")
    submitButton = (By.TAG_NAME, "button")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_login_form(self, user_email, user_password):
        self.custom_type(self.emailInput, user_email)
        self.custom_type(self.passwordInput, user_password)

    def submit_login_form(self):
        self.custom_click(self.submitButton)
