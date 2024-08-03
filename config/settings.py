# config/settings.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
HEADLESS_BROWSER = os.getenv('HEADLESS_BROWSER', 'True').lower() in ('true', '1', 't')
MAX_FOLLOW_PER_DAY = int(os.getenv('MAX_FOLLOW_PER_DAY', 50))
MAX_LIKES_PER_DAY = int(os.getenv('MAX_LIKES_PER_DAY', 100))
MAX_COMMENTS_PER_DAY = int(os.getenv('MAX_COMMENTS_PER_DAY', 20))
