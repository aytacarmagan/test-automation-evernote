from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators for the Login page elements
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    HOME_TITLE = (By.ID, "qa-HOME_TITLE")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        email_field = self.find_element(self.EMAIL_FIELD)
        self.write_slowly(email_field, email)

    def enter_password(self, password):
        password_field = self.find_element(self.PASSWORD_FIELD)
        self.write_slowly(password_field, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.find_element(self.HOME_TITLE) is not None

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        return self.is_login_successful()
