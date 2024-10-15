from selenium.webdriver.common.by import By
from .base_page import BasePage


class NotesPage(BasePage):
    # Locators for the Notes page elements
    NEW_NOTE_BUTTON = (By.XPATH, '//*[@id="qa-NAV"]/div/ul/li[2]/div[3]/div/div/div[1]/button[1]')
    NOTES_BUTTON = (By.XPATH, '//*[@id="qa-NAV"]/div/ul/ul/div/div/div/li[3]')

    def __init__(self, driver):
        super().__init__(driver)

    def create_new_note(self):
        self.click_element(self.NEW_NOTE_BUTTON)
    def open_notes_list(self):
        self.click_element(self.NOTES_BUTTON)
