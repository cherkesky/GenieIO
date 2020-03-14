from django.db import models


class Location(models.Model):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.

    location = models.CharField(max_length=55)
  
    class Meta:
        verbose_name = ("location")
        verbose_name_plural = ("locations")

    