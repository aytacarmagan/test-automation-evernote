import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from pages.editor_page import EditorPage

def test_login_create_note(driver, config, user_credentials, note_example):
    note_content = note_example

    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)
    editor_page = EditorPage(driver)

    try:
        # Login to evernote
        base_page.navigate_to_page(config['evernote']['login_url'])
        assert login_page.login(user_credentials[0], user_credentials[1]), "Login failed"

        # Create a New Note
        notes_page.create_new_note()

        # Enter the formatted note
        editor_page.write_note(note_content)
    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")
