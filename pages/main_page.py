from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):

    SETTINGS_BTN = (By.XPATH, "//a[@href='/settings']")
    SETTINGS_BTN_MOBILE = (By.XPATH, "//a[@class='menu-photo_avatar w-inline-block']")
    MAIN_PAGE_BTN_MOBILE = (By.XPATH, "//a[@class='assistant-button w-inline-block']")

    def open_main(self):
        self.open('https://soft.reelly.io/sign-in')
        # sleep(5)

    def go_to_settings(self):
        self.wait_to_be_clickable_click(*self.SETTINGS_BTN)
        sleep(5)

    def go_to_settings_mobile(self):
        self.wait_to_be_clickable_click(*self.SETTINGS_BTN_MOBILE)
        sleep(8)

    def go_to_main_menu_mobile(self):
        self.wait_to_be_clickable_click(*self.MAIN_PAGE_BTN_MOBILE)
        sleep(5)

