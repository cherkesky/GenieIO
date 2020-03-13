from django.db import models


class Category(models.Model):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.

    category = models.CharField(max_length=55)
  
    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    