from os import write

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage


class EditorPage(BasePage):
    # Locators for various elements on the note editor page
    IFRAME = (By.ID, "qa-COMMON_EDITOR_IFRAME")
    NOTE_CONTENT = (By.XPATH, '//*[@id="en-note"]')
    SELECT_HEADER = (By.XPATH, '//*[@id="qa-HEADING_DROPDOWN"]')
    SELECT_HEADER_1 = (By.XPATH, '// *[ @ id = "qa-HEADING_LARGE"]')

    SELECT_MORE = (By.XPATH, '//*[@id="qa-OVERFLOW_BTN"]')
    SELECT_BULLET_LIST = (By.XPATH, '//*[@id="insertunorderedlist"]')

    SELECT_BULLET = (By.XPATH, '//*[@id="qa-UNORDEREDLIST_BTN"]')

    SELECT_BOLD = (By.XPATH, '//*[@id="qa-BOLD_TEXT_BTN"]')
    SELECT_ITALIC = (By.XPATH, '//*[@id="qa-ITALIC_TEXT_BTN"]')

    def __init__(self, driver):
        super().__init__(driver)

    def write_element(self, content, elements, not_list):
        self.switch_to_default_content()

        # Check formatting
        for i in range(len(elements)):
            self.click_element(elements[i])

        # Switch to the editor iframe and write content
        self.switch_to_iframe(self.IFRAME)
        note_area = self.find_element(self.NOTE_CONTENT)
        self.write_slowly(note_area, content)
        note_area.send_keys(Keys.ENTER)

        # Un-check formatting
        if not_list:
            self.switch_to_default_content()
            self.click_element(elements[0])

    def write_list(self, content):
        self.switch_to_default_content()

        self.find_element(self.SELECT_MORE)
        self.click_element(self.SELECT_MORE)
        self.find_element(self.SELECT_BULLET_LIST)
        self.click_element(self.SELECT_BULLET_LIST)

        self.switch_to_iframe(self.IFRAME)
        # Write each line slowly
        for i in range(len(content)):
            line = self.find_element((By.XPATH, f'//*[@id="en-note"]/ul/li[{i + 1}]/div[2]/div'))
            self.write_slowly(line, content[i])
            line.send_keys(Keys.ENTER)

        self.switch_to_default_content()
        self.find_element(self.SELECT_MORE)
        self.click_element(self.SELECT_MORE)
        self.find_element(self.SELECT_BULLET_LIST)
        self.click_element(self.SELECT_BULLET_LIST)


    def write_note(self, content):
        self.write_element(content["header"], [self.SELECT_HEADER, self.SELECT_HEADER_1], False)
        self.write_list(content["list"])
        self.write_element(content["bold"], [self.SELECT_BOLD], True)
        self.write_element(content["italic"], [self.SELECT_ITALIC], True)

    # Retrieve and return text content by respective locators
    def get_note_content(self, element):
        self.switch_to_iframe(self.IFRAME)
        note_content_element = self.find_element(element)
        content = note_content_element.text
        self.switch_to_default_content()
        return content
