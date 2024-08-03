"""
The Instagram Bot project is an automated tool designed to interact with Instagram accounts seamlessly and efficiently using the instabot library. This bot is configured to perform tasks such as following a user, liking their most recent post, and commenting on that post with a predefined message. The project is structured to be simple and maintainable, utilizing Python for scripting and automation. The core functionalities are encapsulated within a single script (insta_bot.py), which leverages environment variables for securely storing Instagram credentials. By switching from Selenium-based web scraping to the more stable and efficient Instagram API via instabot, the bot ensures reliable interactions with Instagram accounts. The project is organized to facilitate easy deployment and configuration, with dependencies managed through a requirements.txt file and environment variables loaded using python-dotenv. This bot serves as a practical example of automating social media interactions while adhering to Instagram's API usage policies.
                                                              """



# Instagram Bot

This Instagram bot automates the process of following users, liking their posts, and commenting on them. It uses Selenium for browser automation and InstaPy for Instagram-specific actions.

## Features
- Follow a user
- Like their post
- Comment on the post
- Quota supervision to avoid detection
- Headless browser mode
- AI analysis of posts

## Project Structure
- `config/`: Configuration settings.
- `pages/`: Page Object Pattern for Instagram pages.
- `ai/`: AI analysis of posts.
- `scripts/`: Main script to run the bot.
- `utils/`: Utility functions for quota supervision and relationship bounds.

## Installation
1. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Configure the settings in `config/settings.py`.

3. Run the bot:
    ```
    python scripts/main.py
    ```
