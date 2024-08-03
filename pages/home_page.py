# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    PROFILE_ICON = (By.XPATH, "//span[@data-testid='user-avatar']")

    def go_to_profile(self):
        self.wait_for_element(self.PROFILE_ICON).click()
