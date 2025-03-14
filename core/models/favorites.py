from django.db import models
from user.models.user import User
from project.models.news import News


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    news = models.ForeignKey(News, on_delete=models.PROTECT, null=False, blank=False)
