import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config.settings import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, HEADLESS_BROWSER, MAX_FOLLOW_PER_DAY, MAX_LIKES_PER_DAY, MAX_COMMENTS_PER_DAY
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage
from utils.quota_supervisor import QuotaSupervisor
from utils.relationship_bounds import should_interact_with_user
from ai.analyze_posts import analyze_post_content

# Setup WebDriver
options = Options()
options.headless = HEADLESS_BROWSER
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Firefox(options=options)

# Initialize Pages
login_page = LoginPage(driver)
user_profile_page = UserProfilePage(driver)
quota_supervisor = QuotaSupervisor(MAX_FOLLOW_PER_DAY, MAX_LIKES_PER_DAY, MAX_COMMENTS_PER_DAY)

# Login
login_page.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

# Target user to interact with
target_user = "daggydags"

# Check if we should interact with the target user
if should_interact_with_user(driver, target_user):
    # Navigate to User Profile
    driver.get(f"https://www.instagram.com/{target_user}/")

    # Follow, Like, and Comment
    if quota_supervisor.can_follow():
        user_profile_page.follow_user()
        quota_supervisor.follow_action()

    if quota_supervisor.can_like():
        user_profile_page.like_first_post()
        quota_supervisor.like_action()

    if quota_supervisor.can_comment():
        post_content = "I love the new features in the latest update! 😊"  # Replace with actual post content
        comment = analyze_post_content(post_content)
        user_profile_page.comment_on_first_post(comment)
        quota_supervisor.comment_action()

# Close WebDriver
driver.quit()
