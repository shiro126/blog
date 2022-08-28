from django.db import models


class Tag(models.Model):
    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'

    name = models.CharField(
        verbose_name='タグ',
        max_length=200,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name
