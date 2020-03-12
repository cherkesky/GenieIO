from django.db import models


class Grants(models.Model):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.

    wisher = models.ForeignKey('Wisher', on_delete=models.DO_NOTHING)
    wish = models.ForeignKey('Wishes', on_delete=models.DO_NOTHING)
    memo = models.CharField(max_length=55)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)


    class Meta:
        verbose_name = ("grant")
        verbose_name_plural = ("grants")

    