from django.db import models


class Words(models.Model):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.

    word = models.CharField(max_length=55)
  
    class Meta:
        verbose_name = ("word")
        verbose_name_plural = ("words")

    