# pages/user_profile_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UserProfilePage(BasePage):
    FOLLOW_BUTTON = (By.XPATH, "//button[text()='Follow']")
    FIRST_POST = (By.XPATH, "//article//a")
    LIKE_BUTTON = (By.XPATH, "//button[@aria-label='Like']")
    COMMENT_INPUT = (By.XPATH, "//textarea[@aria-label='Add a comment…']")
    COMMENT_BUTTON = (By.XPATH, "//button[text()='Post']")

    def follow_user(self):
        self.wait_for_element(self.FOLLOW_BUTTON).click()

    def like_first_post(self):
        self.wait_for_element(self.FIRST_POST).click()
        self.wait_for_element(self.LIKE_BUTTON).click()

    def comment_on_first_post(self, comment):
        self.wait_for_element(self.COMMENT_INPUT).send_keys(comment)
        self.wait_for_element(self.COMMENT_BUTTON).click()
