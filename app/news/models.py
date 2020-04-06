from django.db import models
from markdownx import models as markdown_models

from users.models import User

POST_STATUSES = (
    ('-------', '------'),
    ('APPROVE', 'APPROVE'),
    ('DECLINE', 'DECLINE'),
)


class Post(models.Model):
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    creator = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    body = markdown_models.MarkdownxField()
    status = models.CharField(
        choices=POST_STATUSES,
        max_length=7,
        default='-------',
    )

    def __str__(self):
        return f'Post {self.pk}'
