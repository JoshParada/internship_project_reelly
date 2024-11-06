from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Sign_In_Page(Page):

    EMAIL = ""
    PASSWORD = ""
    EMAIL_INPUT = (By.ID, "email-2")
    PASSWORD_INPUT = (By.ID, "field")
    SIGN_IN_BTN = (By.CLASS_NAME, "login-button")

    def sign_in(self):
        self.input_text(self.EMAIL, *self.EMAIL_INPUT)
        self.input_text(self.PASSWORD, *self.PASSWORD_INPUT)
        self.wait_to_be_clickable_click(*self.SIGN_IN_BTN)
        sleep(8)