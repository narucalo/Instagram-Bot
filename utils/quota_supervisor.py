# utils/quota_supervisor.py

import time

class QuotaSupervisor:
    def __init__(self, max_follows, max_likes, max_comments):
        self.max_follows = max_follows
        self.max_likes = max_likes
        self.max_comments = max_comments
        self.follows = 0
        self.likes = 0
        self.comments = 0

    def can_follow(self):
        return self.follows < self.max_follows

    def can_like(self):
        return self.likes < self.max_likes

    def can_comment(self):
        return self.comments < self.max_comments

    def follow_action(self):
        if self.can_follow():
            self.follows += 1
            time.sleep(2)  # Sleep to mimic human behavior

    def like_action(self):
        if self.can_like():
            self.likes += 1
            time.sleep(2)

    def comment_action(self):
        if self.can_comment():
            self.comments += 1
            time.sleep(2)
