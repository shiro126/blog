from django.db import models
from django.utils import timezone


class Entry(models.Model):
    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200,
        null=False,
        blank=False,
        default='無題',
    )
    text = models.TextField(
        verbose_name='本文',
        null=True,
        blank=True,
    )
    tag = models.ManyToManyField(
        'Tag',
        verbose_name='タグ',
        null=True,
        blank=True,
        related_name='entry',
    )
    post_dt = models.DateTimeField(
        verbose_name='作成日時',
        default=timezone.now,
    )
    publication_start_date = models.DateTimeField(
        verbose_name='公開開始日時',
        null=True,
        blank=True,
    )
    publication_end_date = models.DateTimeField(
        verbose_name='公開終了日時',
        null=True,
        blank=True,
    )
    is_private = models.BooleanField(
        verbose_name='非公開',
        default=True,
    )
    is_deleted = models.BooleanField(
        verbose_name='削除',
        default=False,
    )

    def __str__(self):
        return self.title

    @property
    def is_public(self):
        """公開されているか"""
        return True
        # if self.is_deleted or self.is_private:
        #     return False
        # else:
        #     now = timezone.now()
        #     return self.publication_start_dt < now and now < self.publication_end_dt
