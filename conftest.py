import pytest
from utilities.driver_factory import DriverFactory
import yaml
import tkinter as tk
from tkinter import simpledialog


@pytest.fixture(scope="session")
def config():
    # Load configuration from YAML file
    with open("config/config.yaml", "r") as config_file:
        return yaml.safe_load(config_file)


@pytest.fixture(scope="session")
def user_credentials(config):

    if config['use_manual_open']:
        root = tk.Tk()
        root.withdraw()
        email = simpledialog.askstring("Login", "Enter your email:", parent=root)
        password = simpledialog.askstring("Login", "Enter your password:", show='*', parent=root)
        root.destroy()
    else:
        email = config['user_credentials']['email']
        password = config['user_credentials']['password']

    return email, password

@pytest.fixture(scope="session")
def note_example():
    return {
        "header": "Dear Innovator!",
        "list1": [
            "We welcome you to the Findest Universe! Here, you can accelerate your research, technology scouting, and reporting process.",
            "Increase your R&D success by making faster and more informed decisions to ultimately reduce time-to-market.",
            "With an ever-expanding Universe, tap into the wealth of your organization's past research and findings, becoming aware of each other's breakthroughs and preventing the reinvention of the wheel.",
            "Get Started and accelerate your innovative potential."
        ],
        "list": [
            "1"
        ],
        "bold": "Warm regards,",
        "italic": "Findest"
    }

@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    driver = DriverFactory.get_driver(browser)
    yield driver
    driver.quit()