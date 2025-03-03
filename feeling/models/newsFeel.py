from django.db import models
from user.models.user import User
from project.models.news import News
from feeling.models.feeling import Feeling


class NewsFeel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="news_feels")
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name="news_feels")
    feeling = models.ForeignKey(
        Feeling, on_delete=models.PROTECT, related_name="news_feels"
    )

    def __str__(self):
        return f"{self.user} {self.feeling}"
