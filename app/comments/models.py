from django.db import models

from news.models import Post
from users.models import User


class PostComment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    creator = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Comment: {self.pk}'
