from pages.base_page import Page
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import Sign_In_Page


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = Sign_In_Page(driver)
        self.settings_page = SettingsPage(driver)
