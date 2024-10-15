from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        driver.set_window_size(1500, 720)

    # Navigate to the specified URL
    def navigate_to_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    # Wait until the element is clickable and then click it
    def click_element(self, locator, timeout=60):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Wait for the iframe to be available and switch to it
    def switch_to_iframe(self, locator, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # Simulate typing slowly by sending keys one at a time
    def write_slowly(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.1)