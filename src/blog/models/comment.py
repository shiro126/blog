from django.db import models
from django.utils import timezone


class Comment(models.Model):
    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'

    entry = models.ForeignKey(
        'Entry',
        verbose_name='記事',
        on_delete=models.CASCADE,
        related_name='comment',
    )
    name = models.CharField(
        verbose_name='名前',
        max_length=200,
        null=False,
        blank=False,
        default='NO NAME',
    )
    text = models.TextField(
        verbose_name='本文',
        null=True,
        blank=True,
    )
    post_dt = models.DateTimeField(
        verbose_name='投稿日時',
        default=timezone.now,
    )
    is_deleted = models.BooleanField(
        verbose_name='削除',
        default=False,
    )

    def __str__(self):
        return f'{self.entry.title} comment:{self.id}'
