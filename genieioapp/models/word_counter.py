from django.db import models


class Word_Counter(models.Model):

    word = models.CharField(max_length=55)
    value = models.IntegerField()
  
    class Meta:
        verbose_name = ("word_counter")
        verbose_name_plural = ("words_counter")
