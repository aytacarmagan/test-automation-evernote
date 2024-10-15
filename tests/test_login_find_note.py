import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from pages.editor_page import EditorPage

def test_login_find_note(driver, config, user_credentials, note_example):
    expected_content = note_example

    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)
    editor_page = EditorPage(driver)

    try:
        # Reopen the Page
        base_page.navigate_to_page(config['evernote']['login_url'])
        assert login_page.login(user_credentials[0], user_credentials[1]), "Login failed"

        notes_page.open_notes_list()

        # Verify the Note's Persistence and Format
        actual_content = editor_page.get_note_content((By.XPATH, '//*[@id="en-note"]/h1'))
        assert expected_content["header"] in actual_content, f"chrExpected '{expected_content['header']}' to be in '{actual_content}'"

        actual_content = editor_page.get_note_content((By.XPATH, '//*[@id="en-note"]/div[1]/b'))
        assert expected_content["bold"] in actual_content, f"Expected '{expected_content['bold']}' to be in '{actual_content}'"

        actual_content = editor_page.get_note_content((By.XPATH, '//*[@id="en-note"]/div[2]/i'))
        assert expected_content["italic"] in actual_content, f"Expected '{expected_content['italic']}' to be in '{actual_content}'"

        actual_content = editor_page.get_note_content((By.XPATH, '//*[@id="en-note"]'))
        for item in expected_content["list"]:
            assert item in actual_content, f"Expected '{item}' to be in '{actual_content}'"

    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")