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
