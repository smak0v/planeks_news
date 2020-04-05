from django.db import models
from markdownx import models as markdown_models

from users.models import User


class Post(models.Model):
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    creator = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    body = markdown_models.MarkdownxField()

    def __str__(self):
        return f'Post {self.pk}'
