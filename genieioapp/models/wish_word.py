from django.db import models
from .wish import Wish
from .word import Word

class Wish_Word(models.Model):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.

    wish = models.ForeignKey('Wish', on_delete=models.DO_NOTHING)
    word = models.ForeignKey('Word', on_delete=models.DO_NOTHING)
   
    
    class Meta:
        verbose_name = ("Wish_Word")
        verbose_name_plural = ("Wishes_Words")

    