from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=55)
    class Meta:
        ordering = ("word", )
        verbose_name = ("word")
        verbose_name_plural = ("words")

