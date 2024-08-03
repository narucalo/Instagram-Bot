# utils/relationship_bounds.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def should_interact_with_user(driver, username):
    """
    Determines whether to interact with a user based on certain criteria.
    :param driver: Selenium WebDriver instance
    :param username: Instagram username to analyze
    :return: Boolean indicating whether to interact with the user
    """
    try:
        # Navigate to the user's profile
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(5)  # Wait for the page to fully load

        # Debug: log the current page URL
        print(f"Current URL: {driver.current_url}")

        # Print the outer HTML of the body to understand the structure
        body = driver.find_element(By.TAG_NAME, 'body')
        print(f"Body HTML: {body.get_attribute('outerHTML')[:10000]}")  # Print the first 10,000 characters to avoid too much output

        # Extract user metrics (followers, following, posts)
        followers_element = driver.find_element(By.XPATH, "//ul/li[2]//span")
        following_element = driver.find_element(By.XPATH, "//ul/li[3]//span")
        posts_element = driver.find_element(By.XPATH, "//ul/li[1]//span")

        # Debug: log the found elements and surrounding HTML
        print(f"Followers Element: {followers_element}")
        print(f"Followers Element HTML: {followers_element.get_attribute('outerHTML')}")
        print(f"Following Element: {following_element}")
        print(f"Following Element HTML: {following_element.get_attribute('outerHTML')}")
        print(f"Posts Element: {posts_element}")
        print(f"Posts Element HTML: {posts_element.get_attribute('outerHTML')}")

        followers = followers_element.get_attribute('title').replace(',', '')
        following = following_element.text.replace(',', '')
        posts = posts_element.text.replace(',', '')

        # Debug: log the extracted values
        print(f"Followers: {followers}")
        print(f"Following: {following}")
        print(f"Posts: {posts}")

        followers = int(followers)
        following = int(following)
        posts = int(posts)

        # Define criteria for interaction
        min_followers = 100
        max_followers = 10000
        min_posts = 10
        max_following_to_followers_ratio = 2

        # Logic to decide whether to interact with the user
        if followers > min_followers and followers < max_followers and posts > min_posts:
            if following / followers < max_following_to_followers_ratio:
                return True
    except NoSuchElementException as e:
        print(f"Error: {e}")
    return False


