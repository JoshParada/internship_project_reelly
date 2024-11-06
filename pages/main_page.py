from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):

    SETTINGS_BTN = (By.XPATH, "//a[@href='/settings']")

    def open_main(self):
        self.open('https://soft.reelly.io/sign-in')
        # sleep(5)

    def go_to_settings(self):
        self.wait_to_be_clickable_click(*self.SETTINGS_BTN)
        sleep(5)