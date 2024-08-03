# ai/analyze_posts.py

# Import necessary libraries
import re
from textblob import TextBlob

def clean_text(text):
    """
    Clean the input text by removing special characters and unnecessary whitespace.
    
    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    text = text.strip()
    return text

def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text using TextBlob.

    Args:
        text (str): The text to be analyzed.

    Returns:
        str: The sentiment of the text (Positive, Negative, Neutral).
    """
    analysis = TextBlob(text)
    # Determine the sentiment polarity
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_post_content(post):
    """
    Analyze the content of a social media post and provide feedback.

    Args:
        post (str): The content of the post to be analyzed.

    Returns:
        str: Feedback based on the analysis.
    """
    # Clean the post content
    cleaned_post = clean_text(post)
    
    # Analyze the sentiment of the cleaned post
    sentiment = analyze_sentiment(cleaned_post)
    
    # Provide feedback based on the sentiment
    if sentiment == "Positive":
        feedback = "Great post! Keep sharing positive vibes!"
    elif sentiment == "Negative":
        feedback = "It seems like you're having a tough time. Hang in there!"
    else:
        feedback = "Nice post! Thanks for sharing."

    # Debug statements
    print(f"Original post: {post}")
    print(f"Cleaned post: {cleaned_post}")
    print(f"Sentiment: {sentiment}")
    print(f"Feedback: {feedback}")

    return feedback

# Example usage
if __name__ == "__main__":
    example_post = "I love the new features in the latest update! 😊"
    print(analyze_post_content(example_post))
