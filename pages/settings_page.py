from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):

    SETTINGS_OPTIONS = (By.XPATH, "//*[@class='page-setting-block w-inline-block']")
    CTC_BTN = (By.XPATH, "//a[@href='/payment/personal']")
    CTC_BTN_MOBILE = (By.XPATH, "//div[@wized='clientModeButton']")

    def verify_settings_url(self):
        self.verify_url("https://soft.reelly.io/settings")

    def verify_options_count(self, n):
        cell_count = len(self.find_elements(*self.SETTINGS_OPTIONS))
        assert cell_count == int(n), f'Expected {n} benefit cells, got {cell_count}'

    def verify_connect_the_company(self):
        self.wait_to_be_clickable(*self.CTC_BTN)

    def verify_connect_the_company_mobile(self):
        self.wait_to_be_clickable(*self.CTC_BTN_MOBILE)