from django.db import models


class Wishes_Words(models.Model):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.

    wish = models.ForeignKey('Wishes', on_delete=models.DO_NOTHING)
    word = models.ForeignKey('Words', on_delete=models.DO_NOTHING)
   
    
    class Meta:
        verbose_name = ("Wishes_Word")
        verbose_name_plural = ("Wishes_Words")

    